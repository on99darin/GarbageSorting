import time
import DBDynamics
from DBDynamics import Ant
import RPi.GPIO as GPIO
# from moto import *
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
        if(a==b):  
            if (a == "kuangquanshui" or a == "yilaguan"):
                precict.cout1=precict.cout1+1
                precict.num=precict.num+1
                s = ("第" + str(precict.num) + "次识别 " + "数量为:" + str(precict.cout1) + " 类别为"+str(a)+"OK!")
            if (a == "xiangyan" or a == "wapian" or a=="taoci"):
                precict.cout2 = precict.cout2 + 1
                precict.num=precict.num+1
                s = ("第" + str(precict.num) + "次识别 " + "数量为:" + str(precict.cout2) + " 类别为"+str(a)+"OK!")
            if (a == "dianchi"):
                precict.cout3 = precict.cout3 + 1
                precict.num=precict.num+1
                s = ("第" + str(precict.num) + "次识别 " + "数量为:" + str(precict.cout3) + " 类别为"+str(a)+"OK!")
            if (a == "shucai"or a=="fruilt" or a=="egg"):
                precict.cout4 = precict.cout4 + 1
                precict.num=precict.num+1
                s = ("第" + str(precict.num) + "次识别 " + "数量为:" + str(precict.cout4) + " 类别为"+str(a)+"OK!")
            #time.sleep(1)
        return s

