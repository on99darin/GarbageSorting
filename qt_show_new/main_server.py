import sys, time
import time
import cv2
from camera import *
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QMainWindow,QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal,QDateTime,QTime
from ui_distancetest import *
from ui_distancetest import Ui_Dialog_lx
from testhr import *
from predict2 import *
from lobe import ImageModel
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import uic
from PyQt5.Qt import QUrl
import threading
from PyQt5.Qt import (QApplication, QWidget, QPushButton,
                      QThread,QMutex,pyqtSignal)
sensor0=20
sensor1=21
sensor2=16
red_led=26
green_led=19
# sensor1=22
# sensor2=23
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(sensor0,GPIO.IN)
GPIO.setup(sensor1,GPIO.IN)
GPIO.setup(sensor2,GPIO.IN)
GPIO.setup(green_led,GPIO.OUT)
GPIO.setup(red_led,GPIO.OUT)

cap=cv2.VideoCapture(0)
cv2.namedWindow("camera",1)
model = ImageModel.load('/home/pi/CLBDEMO/TFLite_gs')
class Dialog_lx(QtWidgets.QMainWindow, Ui_Dialog_lx):
    def __init__(self, parent=None):
        super(Dialog_lx, self).__init__(parent=parent)
#         self.setupUi(self)
        # 初始化一个定时器_lx, self).__init__(parent=parent)
        self.setupUi(self)
        #self.ui = uic.loadUi('ui_distancetest.ui')
        self.timer = QTimer(self)
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_player)
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(r'/home/pi/CLBDEMO/2.avi')))
        # 定义时间超时连接start_app
#         self.timer.timeout.connect(self.getdatastart)
        # 定义时间任务是一次性任务
        # self.timer.setSingleShot(True)
        # 实例化一个线程
#         self.work = WorkThread()
        self.work1=WorkThread1()
        self.work=WorkThread()
#         
        self.work2=WorkThread2()
        self.work3=WorkThread3()
        #self.work2=WorkThread2()
        # 多线程的信号触发连接到distance
#         self.work1.trigger.connect(self.predict
        self.work.trigger.connect(self.predict)
#         self.work2.trigger.connect(self.distance)
        self.work1.trigger.connect(self.openVideoFile)
        self.work2.trigger.connect(self.distance)
        
        
#         self.work3.start()
#         self.work.start()
#         self.work1.start()
#         self.work1.start()
#         self.work.start()
#         self.work2.start()
#     def getdatastart(self):
#         #启动定时器
#         self.timer.start(500)#500ms采集一次距离
# #         self.work2.trigger.connect(self.distance)
#         self.work2.start()
# #         self.work.trigger.connect(self.predict)
#     def timerstop(self):
#         #print('stop')
#         self.distanceEdit.setText('stop')
#         #关闭定时器
#         self.timer.stop()

    def distance(self, str):
        
#         if(((GPIO.input(sensor2))&(GPIO.input(sensor0))&(GPIO.input(sensor1)))==True):
# #     if(GPIO.input(sensor2)==True):
#             GPIO.output(green_led,GPIO.LOW)
#             GPIO.output(red_led,GPIO.HIGH)
#             self.distanceEdit.setText("满载")
#         else:
#             GPIO.output(red_led,GPIO.LOW)
#             GPIO.output(green_led,GPIO.HIGH)
#             self.distanceEdit.setText("未满载")
#         time.sleep(1)
            self.distanceEdit.setText(str)
# # #         hr2 = hrsr04()
# # #         a=hr2.checkdist()
# # # #         time = QTime.currentTime()
# # # #         t=time.toString()#时间
# # #         time.sleep(1)
# # #         b=hr2.checkdist()
# # #         if(a==b):
# # #             self.distanceEdit.setText('%s'% b)#显示文字
# # #         else:
# # #             self.distanceEdit.setText('%s'% "检测中..")
# #         self.distanceEdit.setText(str)   
# #         #print(t+':    %0.2f cm' % a)
# #         #self.show_result.setText('%0.2f cm' % a)#显示距离
#        self.distanceEdit.setText(str)#显示文字
#             self.show_result.setText(str)
    def predict(self, str):
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         aa=result.prediction
#         time.sleep(1)
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         bb=result.prediction
#         jud=precict()
#         s=jud.judge(aa,bb)
#         self.distanceEdit.setText("未满载")#显示文字
        self.listWidget.addItem(str)
#         if(s!="等待识别中..." or s!="空闲 可以识别"):
#             time.sleep(4)
    def openVideoFile(self):
#         qmut_1.lock()
#         #self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
#         self.player.setMedia(QMediaContent(QUrl.fromLocalFile(r'/home/pi/CLBDEMO/2.avi')))
        self.player.play()

#         qmut_1.unlock()   
class WorkThread2(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        #触发信号
          while True:
                if(((GPIO.input(sensor2))&(GPIO.input(sensor0))&(GPIO.input(sensor1)))==True):
#     if(GPIO.input(sensor2)==True):
                    GPIO.output(green_led,GPIO.LOW)
                    GPIO.output(red_led,GPIO.HIGH)
                    self.trigger.emit(str("满载"))
                else:
                    GPIO.output(red_led,GPIO.LOW)
                    GPIO.output(green_led,GPIO.HIGH)
                    self.trigger.emit(str("未满载"))
                time.sleep(1)
class WorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)
  
    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()
    def run(self):
        jud=precict()
        while True:
            try:
                result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
                aa=result.prediction
                time.sleep(0.1)
                result1 = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
                bb=result1.prediction
                tt=jud.judge(bb,aa)
                if(aa!="no trash"):
                    self.trigger.emit(str(tt))
            except:
                pass
            
class WorkThread1(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()
    def run(self):
       
#         #触发信号
#         self. player.setMedia(QMediaContent(QUrl.fromLocalFile(r'/home/pi/CLBDEMO/2.avi')))
#         self.player.play()
#         for i in range(10):
#             time.sleep(1)
#             self.trigger.emit(str(i))
#         hr2 = hrsr04()
#         a=hr2.checkdist()
#         time.sleep(1)
#         b=hr2.checkdist() 
#         if(a==b):
#              s=b
#         else:
#             s="检测中"
#         qmut_1.lock()
#          #self.player.setMedia(QMediaContent(QFileDialog.getOpenFileUrl()[0]))
#         self. player.setMedia(QMediaContent(QUrl.fromLocalFile(r'/home/pi/CLBDEMO/2.avi')))
#         self.player.play()
#         qmut_1.unlock()
        self.trigger.emit('')
#          time.sleep(1)
# def predict_play():
#     try:
#             result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#             global a
#             a=result.prediction
#             
# #             print(a)
#     except :
#                 print('')
#     time.sleep(0.1)
class WorkThread3(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()
    def run(self):
        while True:
            ret,frame=cap.read()
            cv2.imshow('camera',frame)
            if  cv2.waitKey(50) :      
                cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame) 
# def camera_play():
#         while True:
#             ret,frame=cap.read()
#             cv2.imshow('camera',frame)
#             if  cv2.waitKey(50) :      
#                 cv2.imwrite("/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg", frame)  #
# thread1=threading.Thread(target = camera_play, args = ())
# thread1.start()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    

    w = Dialog_lx()
#     w.showFullScreen()
    w.show()
#     hr=hrsr04()
#     hr.inithr()
#     thread1=threading.Thread(target = camera_play, args = ())
#     thread1.start()
    sys.exit(app.exec_())

