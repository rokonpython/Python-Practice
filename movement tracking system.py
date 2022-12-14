#import winsound
import cv2
#import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, Frame1 = cam.read()
    ret, Frame2 = cam.read()
    diff = cv2.absdiff(Frame1,Frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,( 5, 5), 0)
    _, tresh =cv2.threshold(blur, 20,255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(tresh, None, iterations=3)
    contors, _ =cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
   # cv2.drawContours(Frame1,contors, -1,(0,255,0), 2)
    for c in contors:
        if cv2.contourArea(c) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        #cv2.ractangle(Frame1, (x, y),(x+w, y+h), (0,255,0), 2)
        cv2.rectangle(Frame1,(x,y), (x+w, y+h), (0, 255, 0), 2)
        #winsound.PlaySound('alarm.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Camra OF SS', Frame1)
