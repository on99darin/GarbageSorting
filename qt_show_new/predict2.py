import time
import DBDynamics
from DBDynamics import Ant
import RPi.GPIO as GPIO
from moto import *
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
# m.setTargetVelocity(1,180)
class precict:
    cout4=0
    cout1=0
    cout2=0
    cout3=0
    num=0
    def judge(self,b,a):
        if(a=="xiangyan")&(b=="xiangyan"):
            precict.cout2 = precict.cout2 + 1
            precict.num=precict.num+1
            set_servo_angle(12,120)#
            time.sleep(0.2)
            set_servo_angle(4,35)
            time.sleep(0.5)
            set_servo_angle(4,75)
            s = (str(precict.num) + "  其他垃圾  "+ str(precict.cout2) + "  "+"OK!")
               
        if (a == "dianchi")&(b == "dianchi"):
                precict.cout3 = precict.cout3 + 1
                precict.num=precict.num+1
                set_servo_angle(12,40)#
                time.sleep(0.2)
                set_servo_angle(4,110)
                time.sleep(0.5)
                set_servo_angle(4,75)
                s = (str(precict.num) + "  有害垃圾  "+ str(precict.cout3) + "  "+"OK!")
        if(a=="kehuishou")&(b=="kehuishou"):
            precict.cout1=precict.cout1+1
            precict.num=precict.num+1
            set_servo_angle(12,40)#
            time.sleep(0.2)
            set_servo_angle(4,40)
            time.sleep(0.5)
            set_servo_angle(4,75)
            s = (str(precict.num) + "  可回收垃圾  "+ str(precict.cout1) + "  "+"OK!")

        if(a=="chuyu")&(b=="chuyu"):
                precict.cout4 = precict.cout4 + 1
                precict.num=precict.num+1
                set_servo_angle(12,120)#
                time.sleep(0.2)
                set_servo_angle(4,110)
                time.sleep(0.5)
                set_servo_angle(4,75)
                s = (str(precict.num) + "  厨余垃圾  "+ str(precict.cout4) + "  "+"OK!")
            #time.sleep(1)
        
        return s

 