#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

from math import *
from statistics import *
# Create your objects here.
ev3 = EV3Brick()
MotorLeft = Motor(Port.A)
MotorRight = Motor(Port.B)
MotorWater= Motor(Port.C)
MotorBlocks = Motor(Port.D)
left_color = ColorSensor()
right_color = ColorSensor()
bottom_color = ColorSensor()
gyro_sensor = GyroSensor()
# Write your program here.

# PID General Controller
def PID_Gyro(threshold, target, actual):
    kp = 1
    ki = 1
    kd = 1
    integral = 0
    derivative   = 0
    output = 0
    error = target - actual
    previous = error
    while abs(error) > threshold:
        error = target - actual
        integral += error
        derivative = error - previous
        output = (kp * error) + (ki * integral) + (kd * derivative)
        MotorLeft.run(output)
        MotorRight.run(output * -1) 
        print(f"error is now {error}, output is now: {output}")
        
# def PID_Colour(threshold, left_rgb, right_rgb, actual_rgb): # look yuzhe you arent dead
#     kp = 1
#     ki = 1
#     kd = 1
#     integral = 0 
#     derivative = 0
#     output = 0
#     error = (target_rgb(1)-actual_rgb(1),target_rgb(2)-actual_rgb(2),target_rgb(0)-actual_rgb(0))
#     previous = error
#     while abs(mean(error)) > threshold:
#         error = (target_rgb(1)-actual_rgb(1),target_rgb(2)-actual_rgb(2),target_rgb(0)-actual_rgb(0))
#         integral += mean(error)
#         derivative = (error(1)-previous(1),error(2)-previous(2),error(0)-previous(0))
# actual prrogram
# Testing
PID_Gyro(2,0,gyro_sensor.angle())
# the picking stuff up FUNCTION


# the savepeopleandpickstuffup algorithm