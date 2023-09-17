import cv2
cap=cv2.VideoCapture(0)
cv2.namedWindow("camera",1)

while True:
    ret,frame=cap.read()
    cv2.imshow('camera',frame)
    if  cv2.waitKey(60) :      
        cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame)  # 保存路径
             
    