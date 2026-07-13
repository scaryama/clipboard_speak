import asyncio
import edge_tts

async def main():
    text = "안녕하세요. 한국어 음성 테스트입니다."

    voice = "ko-KR-SunHiNeural" # 여성, 부드러움
    #voice = "ko-KR-InJoonNeural" # 남성, 차분함
    #voice = "ko-KR-HyunsuMultilingualNeural" # 남성, 차분함
    
    print(f"'{text}'를 읽는 중...")
    # 속도와 높낮이 조정: rate는 +20% (역으로 20%), pitch는 +8Hz
    communicate = edge_tts.Communicate(text, voice, rate="+20%", pitch="+8Hz")
    
    # 임시 파일로 저장 후 재생하는 대신, 즉시 출력을 위해 비동기 스트리밍 사용
    # 여기서는 간단히 파일로 저장하는 테스트입니다.
    await communicate.save("test_edge.mp3")
    print("완료: test_edge.mp3 파일이 생성되었습니다.")

if __name__ == "__main__":
    asyncio.run(main())
