import sys, time
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton,QWidget,QHBoxLayout,QMainWindow,QLabel
from PyQt5.QtCore import QTimer, QThread, pyqtSignal,QDateTime,QTime
from ui_distancetest import *
from ui_distancetest import Ui_Dialog_lx
#from testhr import *
#from predict import *
#from lobe import ImageModel
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import uic
#model = ImageModel.load('/home/pi/CLBDEMO/xiangyan TFLite 2')
class Dialog_lx(QtWidgets.QMainWindow, Ui_Dialog_lx):
    def __init__(self, parent=None):
        super(Dialog_lx, self).__init__(parent=parent)
#         self.setupUi(self)
        # 初始化一个定时器_lx, self).__init__(parent=parent)
        self.setupUi(self)
        #self.ui = uic.loadUi('ui_distancetest.ui')
        self.player = QMediaPlayer()
        self.timer = QTimer(self)
        # 定义时间超时连接start_app
        self.timer.timeout.connect(self.getdatastart)
        # 定义时间任务是一次性任务
        # self.timer.setSingleShot(True)
        # 实例化一个线程
        #self.work = WorkThread()
        self.work1=WorkThread1()
        self.work=imageThread()
        #self.work2=WorkThread2()
        # 多线程的信号触发连接到distance
        self.work1.trigger.connect(self.distance)
        #self.work.trigger.connect(self.predict)
        #self.work.trigger.connect(self.openVideoFile)
    def getdatastart(self):
        #启动定时器
        self.timer.start(500)#500ms采集一次距离
        self.work.start()
        self.work1.start()
#         self.work1.trigger.connect(self.distance)
#         self.work.trigger.connect(self.predict)
    def timerstop(self):
        #print('stop')
        self.distanceEdit.setText('stop')
        #关闭定时器
        self.timer.stop()

    def distance(self, str):
#         hr2 = hrsr04()
#         a=hr2.checkdist()
#         time = QTime.currentTime()
#         t=time.toString()#时间
#          print(str)
#          time.sleep(1)
#         b=hr2.checkdist()
        
#         if(a==b):
#             self.distanceEdit.setText('%s'% b)#显示文字
#         else:
#             self.distanceEdit.setText('%s'% "检测中..")
        self.distanceEdit.setText(str)
        
        #print(t+':    %0.2f cm' % a)
        #self.show_result.setText('%0.2f cm' % a)#显示距离
        #self.distanceEdit.setText('%s'% a)#显示文字
        #self.show_result.setText("1")
    def predict(self, str):
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         aa=result.prediction
#         time.sleep(1)
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         bb=result.prediction
#         jud=precict()
#         s=jud.judge(aa,bb)
        self.listWidget.addItem(str)
#         if(s!="等待识别中..." or s!="空闲 可以识别"):
#             time.sleep(4)
class WorkThread(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        #触发信号
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         aa=result.prediction
#         time.sleep(1)
#         result = model.predict_from_file('/home/pi/bin/xiangyan TFLite/example/pic/pic.jpg')
#         bb=result.prediction
#         jud=precict()
#         s=jud.judge(aa,bb)
#         self.trigger.emit(str(s))
#         if(s!="等待识别中..." or s!="空闲 可以识别"):
#              time.sleep(4)
        for i in range(20):
            time.sleep(3)
            i=str("sdasdsad"+str(i))
            self.trigger.emit(str(i))
class WorkThread1(QThread):
    # 定义一个信号
    trigger = pyqtSignal(str)

    def __int__(self):
        # 初始化函数，默认
        super(WorkThread, self).__init__()

    def run(self):
        #触发信号
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
#         self.trigger.emit(str(s))
#         time.sleep(1)
        self.trigger.emit('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Dialog_lx()
    w.show()
    
    sys.exit(app.exec_())