import time
import DBDynamics
from DBDynamics import Ant
import RPi.GPIO as GPIO
from moto import *
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
# m.setTargetVelocity(1,180)
classes1=["kuangquanshui","yilaguan"]
classes2=["xiangyan","wapian","taoci"]
classes3=["shucai","fruilt","egg"]
class precict:
    cout4=0
    cout1=0
    cout2=0
    cout3=0
    num=0
    def judge(self,b,a):
        if(a in classes1)&(b in classes1):
            precict.cout1=precict.cout1+1
            precict.num=precict.num+1
            set_servo_angle(12,40)#
            time.sleep(0.2)
            set_servo_angle(4,40)
            time.sleep(0.4)
            set_servo_angle(4,75)
            s = (str(precict.num) + "      "+ str(precict.cout1) + "可回收垃圾  "+"OK!")
        if(a in classes2)&(b in classes2):
            precict.cout2 = precict.cout2 + 1
            precict.num=precict.num+1
            set_servo_angle(12,120)#
            time.sleep(0.2)
            set_servo_angle(4,40)
            time.sleep(0.4)
            set_servo_angle(4,75)
            s = (str(precict.num) + "      "+ str(precict.cout2) + "其他垃圾  "+"OK!")
               
        if (a == "dianchi")&(b == "dianchi"):
                precict.cout3 = precict.cout3 + 1
                precict.num=precict.num+1
                set_servo_angle(12,40)#
                time.sleep(0.2)
                set_servo_angle(4,110)
                time.sleep(0.4)
                set_servo_angle(4,75)
                s = (str(precict.num) + "      "+ str(precict.cout3) + "电池  "+"OK!")

        if(a in classes3)&(b in classes3):
                precict.cout4 = precict.cout4 + 1
                precict.num=precict.num+1
                set_servo_angle(12,120)#
                time.sleep(0.2)
                set_servo_angle(4,110)
                time.sleep(0.4)
                set_servo_angle(4,75)
                
                s = (str(precict.num) + "      "+ str(precict.cout4) + "厨余垃圾  "+"OK!")
            #time.sleep(1)
        return s

