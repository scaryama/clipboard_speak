import pyttsx3

def test_pyttsx3_voices():
    # 엔진 초기화
    engine = pyttsx3.init()
    
    # 설치된 모든 음성 목록 출력
    voices = engine.getProperty("voices")
    print(f"설치된 음성 개수: {len(voices)}")
    
    for i, voice in enumerate(voices):
        print(f"[{i}] 이름: {voice.name}, ID: {voice.id}")
    
    # 한국어 음성 설정 시도 (기존 방식)
    selected = False
    for voice in voices:
        voice_id = voice.id.lower()
        voice_name = voice.name.lower()
        
        # 한국어 음성 조건 확인
        if "ko" in voice_id or "korean" in voice_name or "한국" in voice.name:
            print(f"\n한국어 음성 발견: {voice.name}")
            engine.setProperty("voice", voice.id)
            selected = True
            break
            
    if selected:
        text = "안녕하세요. 한국어 음성 테스트입니다."
        print(f"\n파일 저장 중: test_pyttsx3.wav")
        engine.save_to_file(text, "test_pyttsx3.wav")
        engine.runAndWait()
        print("완료.")
    else:
        print("\n한국어 음성을 찾지 못했습니다.")

if __name__ == "__main__":
    test_pyttsx3_voices()
