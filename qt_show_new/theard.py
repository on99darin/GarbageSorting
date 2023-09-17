import threading
import time
import cv2
cap=cv2.VideoCapture(0)
cv2.namedWindow("camera",1)
def thread1():

    while True:
        
        ret,frame=cap.read()
        cv2.imshow('camera',frame)
        if  cv2.waitKey(60) :      
             cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame)
        
#         print("\nThis is thread1!")


def thread2():

    while True:

        print("\nThis is thread2!")

        time.sleep(2)

thread3=threading.Thread(target = thread1, args = ())
# thread4=threading.Thread(target=  thread2,args = () )
thread3.start()
# thread4.start()
    