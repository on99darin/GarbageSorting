#显示变量

#!/usr/bin/python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
import sys
from PyQt5.QtCore import *#QCoreApplication
from PyQt5.QtGui import *#QIcon,Qpalette,Qbrush,QPixmap,QColor
from PyQt5.QtWidgets import *#QWidget,QLabel,QPushButton,QGridLayout,QApplication

class UI(QWidget):
    #初始化
    def __init__(self):
        super().__init__()
        self.distances=0  
        self.setMinimumSize(40, 30)
        self.initUI()
              
    def initUI(self):
        #新建一个QTimer对象        
        self.timer = QTimer()      
        self.timer.setInterval(1000)       
        self.timer.start()
         
        # 信号连接到槽    超时刷新     
        self.timer.timeout.connect(self.onTimerOut)

        self.init_hcsr()
        self.distances=self.read_distance()
        
        self.distances_show = QLabel(self)
        self.distances_show.setText(str(self.distances))
        self.distances_show.move(60, 100)

        self.setGeometry(0, 30, 600, 300)
        self.setWindowTitle('show')
        self.show()
        self.setWindowIcon(QIcon('logo.png'))
		
	#定义槽  超时刷新UI
    def onTimerOut(self):        
        self.distances=self.read_distance()
        self.distances_show.setText(str(self.distances))
     
    def init_hcsr(self):
        GPIO.setmode(GPIO.BCM)		#以BCM编码格式
        GPIO.setup(6, GPIO.IN)	
        GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)   #初始化低电平
        
    def read_distance(self):
        GPIO.output(5, GPIO.LOW)
        time.sleep(0.00001)#10微妙
        GPIO.output(5, GPIO.HIGH)
        
        # start
        while not (GPIO.input(6) == 1):
            pass                       #pass主要作用就是占据位置，让代码整体完整，相当于C的;或者{}，当你还没想清楚函数内部内容，就可以用pass来进行填坑
        start = time.time()

        # end
        while not (GPIO.input(6) == 0): 
            pass
        end = time.time()

        # 计算distance 时间差单位为S
        self.distance = round((end - start) * 343 / 2 * 100, 2)
        print("distance:{:.2f}cm".format(self.distance))
        return self.distance
    	
     
    #确认是否退出UI
    def closeEvent(self, event):
        box = QMessageBox(QMessageBox.Question, self.tr("提示"), self.tr("您确定要退出吗？"), QMessageBox.NoButton, self)
        yr_btn = box.addButton(self.tr("是"), QMessageBox.YesRole)
        box.addButton(self.tr("否"), QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yr_btn:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = UI()
	sys.exit(app.exec_())   #消息循环结束之后返回0，接着调用sys.exit(0)退出程序

