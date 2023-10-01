import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,QWidget,QApplication,QLabel,QDesktopWidget
from PyQt5.QtGui import QStandardItemModel,QFont
from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt
import RPi.GPIO as GPIO

class UI(QWidget):
    harmful=0
    recycle=0
    kitchen=0
    other=0
    #初始化
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setupSerial()

    def initUI(self):
        #创建一个GUI
        self.resize(800, 480)
        self.setWindowTitle('垃圾分类')
        self.center()

        #QTimer刷新        
        self.serial_timer = QTimer(self)      
        self.serial_timer.timeout.connect(self.processSerialData)       
        self.serial_timer.start(100)

        #QLable布局管理
        #有害垃圾标签
        harmful = QLabel('有害垃圾',self)
        harmful.move(670,100)
        #有害垃圾数量
        harmfullab = QLabel('', self)
        harmfullab.setText(str(self.harmful))
        harmfullab.move(750, 100)

        #可回收垃圾标签
        recycle = QLabel('可回收垃圾',self)
        recycle.move(670,200)
        #可回收垃圾数量
        recyclelab = QLabel('', self)
        recyclelab.setText(str(self.recycle))
        recyclelab.move(750, 200)

        #厨余垃圾标签
        kitchen = QLabel('厨余垃圾',self)
        kitchen.move(670,300)
        #有害垃圾数量
        kitchenlab = QLabel('', self)
        kitchenlab.setText(str(self.kitchen))
        kitchenlab.move(750, 300)

        #其他垃圾标签
        other = QLabel('其他垃圾',self)
        other.move(670,400)
        
        #其他垃圾数量
        otherlab = QLabel('', self)
        otherlab.setText(str(self.other))
        otherlab.move(750, 400)


        self.show()
    
    def setupSerial(self):
        self.serial_port = serial.Serial('/dev/ttyS0', 115200)  # 根据实际串口设备和波特率进行设置
        self.serial_port.flushInput()


    def center(self):
        #窗口居中函数
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def processSerialData(self):
        if self.serial_port.in_waiting > 0:
            received_data = self.serial_port.read(1).decode()
            if received_data == '1':
                self.harmful += 1
            elif received_data == '2':
                self.recycle += 1
            elif received_data == '3':
                self.kitchen += 1
            elif received_data == '4':
                self.other += 1


if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = UI()
	sys.exit(app.exec_())   

