import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDesktopWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer
import serial

class UI(QWidget):
    harmful = 0
    recycle = 0
    kitchen = 0
    other = 0

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('垃圾分类')
        self.resize(800, 480)
        self.center()
        self.setupLabels()

        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.updateLabels)
        self.timer.start()

        self.setupSerial()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def setupLabels(self):
        label_positions = {
            '有害垃圾': (670, 100),
            '可回收垃圾': (670, 200),
            '厨余垃圾': (670, 300),
            '其他垃圾': (670, 400)
        }

        self.labels = {}
        for label_name, (x, y) in label_positions.items():
            self.labels[label_name] = self.createLabel(label_name, x, y)

    def createLabel(self, text, x, y):
        label = QLabel(text, self)
        label.move(x, y)
        label.setFont(QFont("Arial", 16))
        return label

    def updateLabels(self):
        for label_name, label in self.labels.items():
            label.setText(f'{label_name}: {getattr(self, label_name.lower())}')

    def setupSerial(self):
        self.serial_port = serial.Serial('/dev/ttyS0', 9600)
        self.serial_port.flushInput()

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
    ex.show()
    sys.exit(app.exec_())
