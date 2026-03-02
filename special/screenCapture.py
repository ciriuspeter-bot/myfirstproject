import pyautogui
import pyscreeze
import time
from datetime import datetime
import os
from PIL import Image

# 저장할 폴더 생성
os.makedirs("screenshots", exist_ok=True)

print("화면 캡처 시작 (10초 간격) - 종료하려면 Ctrl+C 누르세요")

try:
    while True:
        # 현재 시간으로 파일명 생성
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/screenshot_{timestamp}.png"
        
        # 화면 캡처
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        
        print(f"✅ 저장됨: {filename}")
        
        # 10초 대기
        time.sleep(10)
        
except KeyboardInterrupt:
    print("\n⏹️  프로그램 종료")
except pyscreeze.PyScreezeException:
    print("Error")