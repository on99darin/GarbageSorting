import sys
import RPi.GPIO as GPIO
import serial
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QApplication, QLabel, QDesktopWidget
from PyQt5.QtGui import QStandardItemModel, QFont
from PyQt5 import uic
from PyQt5.QtCore import QTimer, Qt, QThread, pyqtSignal

class UltrasonicThread(QThread):
    distanceChanged = pyqtSignal(float)

    def __init__(self, trig_pin, echo_pin):
        super().__init__()
        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.distance = 0
        

    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

        while True:
            GPIO.output(self.trig_pin, False)
            time.sleep(0.1)

            GPIO.output(self.trig_pin, True)
            time.sleep(0.00001)
            GPIO.output(self.trig_pin, False)

            pulse_start = time.time()
            while GPIO.input(self.echo_pin) == 0:
                pulse_start = time.time()

            pulse_end = time.time()
            while GPIO.input(self.echo_pin) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            distance = pulse_duration * 17150
            distance = round(distance, 2)

            self.distanceChanged.emit(distance)
            time.sleep(1)

class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.harmful = 0
        self.recycle = 0
        self.kitchen = 0
        self.other = 0
        self.Label = ''
        self.total = 0
        self.types = []
        self.signal1 = "full"
        self.signal2 = "free"
        self.serlist=[]
        self.initUI()
        self.setupSerial()
        self.setupServo()
    def initUI(self):
        self.initUltrasonicThreads()

        self.resize(900, 480)
        self.setWindowTitle('垃圾分类')
        self.center()

        self.serial_timer1 = QTimer(self)
        self.serial_timer1.setInterval(1000)
        self.serial_timer1.timeout.connect(self.processSerialData1)
        self.serial_timer1.start()
        
        self.serial_timer = QTimer(self)
        self.serial_timer.setInterval(100)
        self.serial_timer.timeout.connect(self.processSerialData2)
        self.serial_timer.start()
        
        harmful = QLabel('有害垃圾', self)
        harmful.move(100, 150)
        self.harmful_label1 = QLabel('0', self)
        self.harmful_label1.move(180, 150)
        self.harmful_label2 = QLabel('free', self)
        self.harmful_label2.move(230, 150)

        recycle = QLabel('可回收垃圾', self)
        recycle.move(100, 220)
        self.recycle_label1 = QLabel('0', self)
        self.recycle_label1.move(180, 220)
        self.recycle_label2 = QLabel('free', self)
        self.recycle_label2.move(230, 220)

        kitchen = QLabel('厨余垃圾', self)
        kitchen.move(600, 150)
        self.kitchen_label1 = QLabel('0', self)
        self.kitchen_label1.move(680, 150)
        self.kitchen_label2 = QLabel('free', self)
        self.kitchen_label2.move(730, 150)

        other = QLabel('其他垃圾', self)
        other.move(600, 220)
        self.other_label1 = QLabel('0', self)
        self.other_label1.move(680, 220)
        self.other_label2 = QLabel('free', self)
        self.other_label2.move(730, 220)

        total = QLabel('total', self)
        total.move(670, 300)
        self.total_label1 = QLabel('0', self)
        self.total_label1.move(800, 300)
        
        types = QLabel('type',self)
        types.move(400,300)
        self.types_label1 = QLabel('', self)
        self.types_label1.move(480, 300)
        self.types_label1.resize(100,20)
        
        status = QLabel('status',self)
        status.move(100,300)
        self.status_label1 = QLabel('wait',self)
        self.status_label1.move(230, 300)
        self.status_label1.resize(100,20)
        
        title = QLabel('智能垃圾分类',self)
        title.move(400,60)
        
        
        self.show()

    def setupSerial(self):
        #self.serial_port = serial.Serial("/dev/ttyAMA0", 115200)
        #self.serial_port.flushInput()
        self.ser = serial.Serial("/dev/ttyAMA0", 115200)
        self.ser.flushInput()
    def center(self):
        # 窗口居中函数
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    
    def setupServo(self):
         
        GPIO.setmode(GPIO.BCM)
        
        self.servo1_pin = 18
        self.servo2_pin = 19
        self.frequency = 50
        
        GPIO.setup(self.servo1_pin, GPIO.OUT)
        GPIO.setup(self.servo2_pin, GPIO.OUT)
        
        self.pwm1 = GPIO.PWM(self.servo1_pin, self.frequency)
        self.pwm2 = GPIO.PWM(self.servo2_pin, self.frequency)
        self.pwm1.ChangeDutyCycle(0)
        self.pwm2.ChangeDutyCycle(0)
    
    def processSerialData2(self):
        
        
        self.pwm1 .start(angle_to_duty_cycle(15,180))
        self.pwm2 .start(angle_to_duty_cycle(180,270))
        time.sleep(1)
        data = myserial.ser(self)
        print("data: ", data)        
        if data == "b'1'":
            duty_cycle1 = angle_to_duty_cycle(80, 180)
            duty_cycle2 = angle_to_duty_cycle(90, 270)
            self.status_label1.setText(str('OK!'))
            self.servo2_go(duty_cycle2)
            self.servo1_go(duty_cycle1)
            time.sleep(1)
            self.status_label1.setText(str('OK!'))
            #self.setupServo()
            self.pwm1 .start(angle_to_duty_cycle(15,180))
            self.pwm2 .start(angle_to_duty_cycle(180,270))
        
        elif data == "b'2'":
            duty_cycle1 = angle_to_duty_cycle(80, 180)
            duty_cycle2 = angle_to_duty_cycle(0, 270)
            self.status_label1.setText(str('OK!'))
            self.servo2_go(duty_cycle2)
            self.servo1_go(duty_cycle1)
            time.sleep(1)
            #self.setupServo()
            self.pwm1 .start(angle_to_duty_cycle(15,180))
            self.pwm2 .start(angle_to_duty_cycle(180,270))
            
           
            
        elif data == "b'3'":
            duty_cycle1 = angle_to_duty_cycle(80, 180)
            duty_cycle2 = angle_to_duty_cycle(180, 270)
            
            self.servo2_go(duty_cycle2)
            self.servo1_go(duty_cycle1)
            time.sleep(1)
            #self.setupServo()
            self.status_label1.setText(str('OK!'))
            self.pwm1 .start(angle_to_duty_cycle(15,180))
            self.pwm2 .start(angle_to_duty_cycle(180,270))
        
        elif data == "b'4'":
            duty_cycle1 = angle_to_duty_cycle(80, 180)
            duty_cycle2 = angle_to_duty_cycle(270, 270)
            
            self.servo2_go(duty_cycle2)
            self.servo1_go(duty_cycle1)
            time.sleep(1)
            #self.setupServo()
            self.status_label1.setText(str('OK!'))
            self.pwm1 .start(angle_to_duty_cycle(15,180))
            self.pwm2 .start(angle_to_duty_cycle(180,270))
        else:
            self.status_label1.setText(str('FALSE!'))
    def processSerialData1(self):
        if self.ser.in_waiting > 0:
            received_data = self.ser.read(1).decode()
            #print("data=" + received_data)
            
            if received_data == '1':
                
                self.harmful += 1
                self.total += 1
                self.harmful_label1.setText(str(self.harmful))
                Type = "有害垃圾"
                self.types_label1.setText(str(Type))
            elif received_data == '2':
                
                self.recycle += 1
                self.total += 1
                self.recycle_label1.setText(str(self.recycle))
                Type = '可回收垃圾'
                self.types_label1.setText(str(Type))
            elif received_data == '3':
                
                self.kitchen += 1
                self.total += 1
                self.kitchen_label1.setText(str(self.kitchen))
                Type = '厨余垃圾'
                self.types_label1.setText(str(Type))
            elif received_data == '4':
              
                self.other += 1
                self.total += 1
                self.other_label1.setText(str(self.other))
                Type = '其他垃圾'
                self.types_label1.setText(str(Type))
            self.total_label1.setText(str(self.total))    
        
            
            

    def initUltrasonicThreads(self):
        trig_pin1 = 5
        echo_pin1 = 6
        trig_pin2 = 24
        echo_pin2 = 23
        trig_pin3 = 21
        echo_pin3 = 20
        trig_pin4 = 27
        echo_pin4 = 17
        
        self.ultrasonic_threads = []  # 新增
        
        ultrasonic_thread1 = UltrasonicThread(trig_pin1, echo_pin1)
        ultrasonic_thread2 = UltrasonicThread(trig_pin2, echo_pin2)
        ultrasonic_thread3 = UltrasonicThread(trig_pin3, echo_pin3)
        ultrasonic_thread4 = UltrasonicThread(trig_pin4, echo_pin4)
        
        

        self.ultrasonic_threads.append(ultrasonic_thread1)  # 新增
        self.ultrasonic_threads.append(ultrasonic_thread2)  # 新增
        self.ultrasonic_threads.append(ultrasonic_thread3)  # 新增
        self.ultrasonic_threads.append(ultrasonic_thread4)  # 新增

        
        ultrasonic_thread1.distanceChanged.connect(self.processDistance1)
        ultrasonic_thread2.distanceChanged.connect(self.processDistance2)
        ultrasonic_thread3.distanceChanged.connect(self.processDistance3)
        ultrasonic_thread4.distanceChanged.connect(self.processDistance4)

        ultrasonic_thread1.start()
        ultrasonic_thread2.start()
        ultrasonic_thread3.start()
        ultrasonic_thread4.start()

    def processDistance1(self, distance):
        if distance <= 50 and distance >= 5 :
         
            text = f"Distance1: {distance}"
            print(text)
            if distance < 24.5:                                       
                self.harmful_label2.setText(str(self.signal1))
            else :
                self.harmful_label2.setText(str(self.signal2))

    def processDistance2(self, distance):
        if distance <= 50 and distance >= 5 :
        
            text = f"Distance2: {distance}"
            print(text)
            if distance < 24.5:                        
                self.recycle_label2.setText(str(self.signal1))
            else:                       
                self.recycle_label2.setText(str(self.signal2))


    def processDistance3(self, distance):
         if distance <= 50 and distance >= 5 :
        
            text = f"Distance3: {distance}"
            print(text)
            if distance < 24.5:                        
                self.kitchen_label2.setText(str(self.signal1))
            else:                       
                self.kitchen_label2.setText(str(self.signal2))

    def processDistance4(self, distance):
         if distance <= 50 and distance >= 5 :
        
            text = f"Distance4: {distance}"
            print(text)
            if distance < 24.5:                        
                self.other_label2.setText(str(self.signal1))
            else:                       
                self.other_label2.setText(str(self.signal2))
    
    def servo1_go(self, duty_cycle):
        self.pwm1.start(duty_cycle)
        time.sleep(1)
        self.pwm1.ChangeDutyCycle(0) # Clear the current duty cycle to stop the servo from jittering
        time.sleep(0.01)
        self.pwm1.ChangeDutyCycle(duty_cycle)
    
    def servo2_go(self, duty_cycle):
        self.pwm2.start(duty_cycle)
        time.sleep(1)
        self.pwm2.ChangeDutyCycle(0) # Clear the current duty cycle to stop the servo from jittering
        time.sleep(1)
        self.pwm2.ChangeDutyCycle(duty_cycle)
    
    def closeEvent(self,event):
        for thread in self.ultrasonic_threads:
            thread.quit()
            #thread.wait()
        event.accept()

class myserial(UI):
    def __init__(self, parent=None):
        super(myserial, self).__init__(parent)
        self.serlist=[]
    def ser(self):
        try:
            
            count2 = 0
            self.serlist.clear()
            while True:
                self.ser.flushInput()
                time.sleep(0.1)
                count1 = self.ser.inWaiting()
                if count1 != 0:
                    a = str(self.ser.read(count1))
                    if count2 < 3:
                        self.serlist.append(a)
                        count2 += 1
                    
                
                    if count2 == 3:
                        if self.serlist[0] == self.serlist[1] == self.serlist[2]:
                            print(a)
                            return self.serlist[0]
                            break
                        else:
                            count2 = 0
                            self.serlist.clear()
                    time.sleep(0.2)
        except KeyboardInterrupt:
            pass

def angle_to_duty_cycle(angle, servo_range):
    duty_cycle = (angle / servo_range) * 10 + 2
    return duty_cycle

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())

