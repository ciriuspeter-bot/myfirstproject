import whisper
import pyaudio
import wave
import os
import time

def record_audio_chunk(duration=5):
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000
    
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                   input=True, frames_per_buffer=CHUNK)
    
    print(f"Recording for {duration} seconds...")
    frames = []
    for _ in range(0, int(RATE / CHUNK * duration)):
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except Exception as e:
            print(f"Error reading audio: {e}")
            stream.stop_stream()
            stream.close()
            p.terminate()
            return None
    
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    # Save to temp file
    temp_file = f"temp_audio_{int(time.time())}.wav"  # 고유한 파일명 생성
    wf = wave.open(temp_file, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    
    return temp_file

# 메인 실행 부분
try:
    print("Loading Whisper model...")
    model = whisper.load_model("small")  # 필요에 따라 모델 크기 변경 가능
    print("Model loaded. Speak now!")

    while True:
        audio_file = record_audio_chunk(3)  # 3초 녹음
        if audio_file is None:
            continue
            
        print("Transcribing...")
        result = model.transcribe(audio_file, language="ko")  
        print(f"You said: {result['text']}")
        
        # 임시 파일 삭제
        os.remove(audio_file)
        
        # 종료 조건 (예: "종료"라고 말하면 빠져나가기)
        if "종료" in result['text']:
            print("Exiting program.")
            break

except KeyboardInterrupt:
    print("\nProgram interrupted by user.")
except Exception as e:
    print(f"An error occurred: {e}")