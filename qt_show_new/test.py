import Adafruit_PCA9685
# from  moto import set_servo_pulse
# from  moto import set_servo_angle
from moto import *
import time
# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(50)
set_servo_angle(4,75)
# set_servo_angle(15,60)#机械手臂开

# time.sleep(1)
# set_servo_angle(15,110)#机械手臂关
# time.sleep(1)
# set_servo_angle(15,60)
# time.sleep(1)
# set_servo_angle(15,110)
# a=time.time()
# set_servo_angle(12,120)#
# time.sleep(0.2)
# set_servo_angle(4,110)
# time.sleep(0.4)
# while True:
#     set_servo_angle(12,120)#
#     time.sleep(0.2)
#     set_servo_angle(4,40)
#     time.sleep(0.4)
#     set_servo_angle(4,75)
#     time.sleep(0.4)
#     set_servo_angle(4,110)
#     time.sleep(0.2)
#     set_servo_angle(12,40)#
#     time.sleep(0.2)
#     set_servo_angle(4,40)
#     time.sleep(0.4)
#     set_servo_angle(4,75)
#     time.sleep(0.4)
#     set_servo_angle(4,110)
#     time.sleep(0.2)
# set_servo_angle(4,75)
# b=time.time()
# print(b-a)

#set_servo_angle(4,40)
# time.sleep(0.5)
# set_servo_angle(4,75)
# time.sleep(0.5)
# set_servo_angle(4,110)
# time.sleep(0.5)
# set_servo_angle(12,50)#
# set_servo_angle(4,40)
# time.sleep(0.5)
# set_servo_angle(4,75)
# time.sleep(0.5)
# set_servo_angle(4,110)

# time.sleep(1)
# set_servo_angle(15,60)#机械手臂开
# time.sleep(1)
# set_servo_angle(15,110)#机械手臂关
# time.sleep(1)
# set_servo_angle(4,90)#
# set_servo_angle(15,110)#机械手臂关
# time.sleep(1)
# set_servo_angle(15,60)
# time.sleep(1)
# set_servo_angle(15,110)
# import DBDynamics
# from DBDynamics import *
# m=Ant('/dev/ttyUSB0')
# m.setPowerOn(1)
# a=m.getActualPosition(1)
# print(a)
# m.setTargetVelocity(1,300)
# m.setPositionMode(1)
# m.setTargetPosition(1,30*50000)
# m.setAccTime(1,50)
# m.setAccTime(1, 5000)
# # b=m.getHomingDirection(1)
# print(b)
# m.setHomingMode(1)
# c=m.getActualPosition(1)
# print(c)
# m.setTargetVelocity(1,180)
# m.setTargetPosition(1,-60*50000)
# m.waitTargetPositionReached(1)
# set_servo_angle(7,58)
# time.sleep(2)
# set_servo_angle(11,128)
# time.sleep(2)
# set_servo_angle(11,160)
# time.sleep(2)
# # set_servo_angle(11,128)