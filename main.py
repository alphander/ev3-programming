#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from math import *
from vector import Vector
import time

brick = EV3Brick()

drive = 1/3
pan = 1/56
tilt = 1/56
driveMotor = Motor(Port.A)
panMotor = Motor(Port.B)
tiltMotor = Motor(Port.C)

positionA = Vector(0, 0, 0)
positionB = Vector(12.4, 1.4, 3.3)



#Note for ezra: This is stuff that you don't need to worry about!
startTime = time.time()

oldTime = 0 
currentTime = time.time()

oldAngle = 0
currentAngle = 0
#800 max speed

def sample_angle(timeSinceStart):
    pass


def run_motor(motor):
    global timeSinceStart, oldTime, currentTime
    global oldAngle, currentAngle

    oldTime = currentTime
    currentTime = time.time()
    dt = currentTime - oldTime

    timeSinceStart = currentTime - startTime
    oldAngle = currentAngle
    currentAngle = sample_angle(timeSinceStart)

    realSpeed = motor.speed()
    realAngle = motor.angle()

    angleError = realAngle - currentAngle

    #angleError is the difference between the expected angle and the true angle in real life

    

def main():
    while True:
        run_motor(driveMotor)

if __name__=="__main__":
    main()