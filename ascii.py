import os
import time
import cv2
def getText(filename):
    if not os.path.exists('ascii'):
        os.makedirs('ascii')
    cap = cv2.VideoCapture(filename)
    frame_num = cap.get(cv2.CAP_PROP_FRAME_COUNT)
    t=0
    while(cap.isOpened() and t < frame_num - 1):
        x=os.system('cls')
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rows, cols = gray.shape
        gray = cv2.resize(gray, (100, 30), interpolation=cv2.INTER_AREA)
        binary = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

        fp=open('ascii/'+str(t)+'.txt','a')
        for i in gray:
            for j in i:
                if j == 0:
                    fp.write('#')
                else:
                    fp.write('@')
            fp.write('\n')
        fp.close()
        t=t+1;
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if cv2.waitKey(1000) >= 0:
            break;
getText('bad-apple.mp4')
for i in range(5256):
    x=os.system('cls')
    fp = open('ascii/'+str(i)+'.txt','r')
    print(fp.read())
    fp.close()
    time.sleep(0.05)
