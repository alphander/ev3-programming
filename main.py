#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from math import *
from vector import Vector

brick = EV3Brick()

drive = 1/3
pan = 1/56
tilt = 1/56
driveMotor = Motor(Port.D)
#panMotor = Motor(Port.B)
#tiltMotor = Motor(Port.C)

positionA = Vector(0, 0, 0)
positionB = Vector(12.4, 1.4, 3.3)

steps = 1000

a = 10
b = 1000
#800 max speed

def main():
    for i in range(10000000000):
        driveMotor.run(10000)
        speed = driveMotor.speed()
        speedStr = str(speed)
        brick.screen.print(speedStr)

if __name__=="__main__":
    main()