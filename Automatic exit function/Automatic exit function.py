import pyautogui
import time

# print(time.time())

timePre = time.time()
timeElapsed = 0
timeElapsedPre = 0

while True:
    timeElapsed = int(time.time() - timePre)
    if timeElapsed > 3:
        print('3초')
        timePre = time.time() # 여기는 3초가 완료되면 "3초" 라는 문자를 나오게 알려줌
        pyautogui.hotkey('win', 'q')
        pyautogui.typewrite('chrome',interval=0.1)
        pyautogui.typewrite(['enter'])
        time.sleep(1)
        pyautogui.typewrite('https://online.spartacodingclub.kr/nbcamp/records',interval=0.1)
        pyautogui.typewrite(['enter'])
        time.sleep(3)
        
        poi = pyautogui.locateCenterOnScreen(, confidence=0.8)
        print(poi)
        pyautogui.doubleClick(poi, duration=0.5)
        break
    else:
        if(timeElapsed != timeElapsedPre):
            print(timeElapsed) 
            timeElapsedPre = timeElapsed #여기는 3초가 지나가는것을 알려주고있음