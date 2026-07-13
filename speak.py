import pyperclip
import asyncio
import edge_tts
import io
import pygame
import random

async def get_audio_data(sentence, voice, index, queue):
    print(f"DEBUG: [{index+1}] 오디오 생성 요청")
    communicate = edge_tts.Communicate(sentence, voice, rate="+20%", pitch="+8Hz")
    audio_data = io.BytesIO()
    async for chunk in communicate.stream():
        if chunk["type"] == "audio":
            audio_data.write(chunk["data"])
    audio_data.seek(0)
    # 큐에 문장 인덱스와 함께 저장
    await queue.put((index, audio_data))
    print(f"DEBUG: [{index+1}] 오디오 준비 완료")

async def speak_text(text):
    # 3가지 보이스를 리스트로 정의
    voices = [
        "ko-KR-SunHiNeural",          # 0: 여성, 부드러움
        "ko-KR-InJoonNeural",         # 1: 남성, 차분함
        "ko-KR-HyunsuMultilingualNeural" # 2: 남성, 다국어엔진
    ]
    
    # 문장 분할 (마침표나 줄바꿈 기준)
    # 정규표현식 사용하여 여러 구분자로 분할 후 다시 합치기
    import re
    # 마침표나 줄바꿈을 기준으로 분할
    parts = re.split(r'[.\n]+', text)
    sentences = [s.strip() + "." for s in parts if s.strip()]
    
    print(f"[{text}]")
    print(f"DEBUG: 총 {len(sentences)}개의 문장으로 분할되었습니다.")
    
    # 인덱스 랜덤 선택
    voice_index = random.randint(0, 2)
    voice = voices[voice_index]
    print(f"DEBUG: 선택된 음성: {voice}")

    # pygame 초기화
    pygame.mixer.init()
    
    # 생성과 재생을 위한 큐 생성
    queue = asyncio.Queue()
    
    # 1. 병렬 생성 작업 시작 (모든 문장에 대해)
    tasks = [asyncio.create_task(get_audio_data(s, voice, i, queue)) for i, s in enumerate(sentences)]
    
    # 2. 순차 재생 루프
    results = {}
    next_to_play = 0
    
    # 문장 개수만큼 큐에서 결과를 받음
    for _ in range(len(sentences)):
        index, audio_data = await queue.get()
        results[index] = audio_data
        
        # 만약 방금 도착한 데이터가 다음에 재생할 데이터라면 즉시 재생 루프 진입
        # 혹은 이미 도착해있던 데이터들을 순서대로 재생
        while next_to_play in results:
            audio_data = results[next_to_play]
            print(f"DEBUG: [{next_to_play+1}/{len(sentences)}] 재생 시작")
            
            pygame.mixer.music.load(audio_data, "mp3")
            pygame.mixer.music.play()
            
            while pygame.mixer.music.get_busy():
                await asyncio.sleep(0.1)
                
            print(f"DEBUG: [{next_to_play+1}/{len(sentences)}] 재생 완료")
            next_to_play += 1

def main():
    import argparse
    parser = argparse.ArgumentParser(description="텍스트를 한국어 음성으로 읽어줍니다.")
    parser.add_argument("text", nargs="?", type=str, help="읽을 텍스트 (옵션)")
    args = parser.parse_args()

    # 인자가 입력되었으면 사용하고, 없으면 클립보드 사용
    if args.text:
        text = args.text
    else:
        try:
            text = pyperclip.paste()
        except pyperclip.PyperclipException:
            print("클립보드에서 텍스트를 가져올 수 없습니다.")
            return

    stripped = text.strip()
    # 마크다운의 ** (볼드) 등을 제거
    import re
    stripped = re.sub(r'\*\*', '', stripped)
    
    if not stripped:
        print("읽을 텍스트가 없습니다.")
        return

    asyncio.run(speak_text(stripped))

if __name__ == "__main__":
    main()
