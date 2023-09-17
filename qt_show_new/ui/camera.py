import cv2
import time
#from lobe import ImageModel
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
# import RPi.GPIO as GPIO
# import DBDynamics
# from DBDynamics import Ant
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
# m.setTargetPosition(1,30*50000)
cap=cv2.VideoCapture(0)
#model = ImageModel.load('/home/pi/CLBDEMO/xiangyan TFLite 2')
cv2.namedWindow("camera",1)
# cv2.namedWindow("1.mp4",1)
while(True):
    ret,frame=cap.read()
    cv2.imshow('camera',frame)
    if  cv2.waitKey(30):
        cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame)  # 保存路径
        time.sleep(1)
#     result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#     a=result.prediction
#     print(a)
#      if a=="dianchi":
        
#     else: 
#         print("nothing")
    