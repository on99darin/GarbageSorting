import cv2
from time import sleep
from lobe import ImageModel
from PIL import ImageFile
import threading
from PIL import Image
from main_server import *
ImageFile.LOAD_TRUNCATED_IMAGES=True
# import RPi.GPIO as GPIO
# import DBDynamics
# from DBDynamics import Ant
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
# m.setTargetPosition(1,30*50000)
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
cap=cv2.VideoCapture(0)
# model = ImageModel.load('/home/pi/CLBDEMO/TFLite5.2')
cv2.namedWindow("camera",1)
# cv2.namedWindow("1).mp4",1)
a=""

        
def predict():
    while True:
        try:
            result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
            global a
            a=result.prediction
            print(a)
        except :
                print('')
        sleep(0.1)

thread1=threading.Thread(target = predict, args = ())
# thread1.start()


while True:
    ret,frame=cap.read()
    cv2.imshow('camera',frame)
    if  cv2.waitKey(30) :      
        cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame)  # 保存路径
#         time.sleep(1)
#     result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#     a=result.prediction
#     print(a)
#      if a=="dianchi":
        
#     else: 
#         print("nothing")
