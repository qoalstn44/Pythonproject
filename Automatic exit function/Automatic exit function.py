import pyautogui
import time

# print(time.time())
filename = ['test1.png', 'test2.png', 'test3.png', 'test4.png']

timePre = time.time()
timeElapsed = 0
timeElapsedPre = 0

while True:
    timeElapsed = int(time.time() - timePre)
    if timeElapsed > 1:
        print('1초')
        pyautogui.hotkey('win', 'q')
        pyautogui.typewrite('chrome')#interval=0.1)# interval는 사람이 타자를 치는것처럼 시간간격을 두는 함수 0.1은 100ms 으로 한글자를 적을때마다 100ms으로 타핑을 치게된다.
        pyautogui.typewrite(['enter']) #pyautogui.typewrite([])치는 이유는 엔터나 스페이스바를 칠때 대갈호를 써서 사용해야한다.
        time.sleep(2) #time.sleep 말그대로 대기시간을 준다. (1) = 초단위
        pyautogui.typewrite('https://online.spartacodingclub.kr/nbcamp/records')
        pyautogui.typewrite(['enter'])
        time.sleep(2)
        
        isSuccess = True # isSuccess라는 함수를 만들어 만약 페이지에 None뜨면 자동으로 웹페이지를 닫을수 있도록 만듬
        for i, name in  enumerate(filename):#enumerate 은 filename안에 있는 리스트들을 index형태로 만들어준다. [ ex) test1.png를 0을로 표시하고 test2.png를 1로 표시한다. ]
            poi = pyautogui.locateCenterOnScreen(name, confidence=0.79) #pyautogui.locateCenterOnScreen는 해당 웹페이지에 좌표를 가져오는 변수이다. confidence는 해당 웹페이지와 png파일의 이미지가 비슷하면 그 좌표를알려준다 0.5니 50%라고 한다.
            print(name, poi)
            if poi != None:
                pyautogui.doubleClick(poi, duration=0.1)
                time.sleep(2)
                if i==0:
                    pyautogui.scroll(-1000)
                    time.sleep(2)
            else:
                isSuccess = False #else None가 뜨면 Fales뜨고 
        if isSuccess:  
            break #break를 하지않으면 무한반복되기 떄문에 마지막에 무조건 적어두도록 합시다.
        else:
            pyautogui.hotkey('alt', 'f4') #Fales가 뜨고 여기서 pyautogui.hotkey 함수를 이용해 alt, f4를 눌러 웹페이지를 종료한다.
        timePre = time.time()
    else:
        if(timeElapsed != timeElapsedPre):
            print(timeElapsed) 
            timeElapsedPre = timeElapsed#여기는 3초가 지나가는것을 알려주고있음
                