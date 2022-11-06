#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import math
from vector import Vector

brick = EV3Brick()

drive = 1/3
pan = 1/56
tilt = 1/56
driveMotor = Motor(Port.B)
#panMotor = Motor(Port.B)
#tiltMotor = Motor(Port.C)

positionA = Vector(0, 0, 0)
positionB = Vector(12.4, 1.4, 3.3)

steps = 1000

a = 10
b = 1000

flip = True

def lerp(t, a, b):
    return a + (b - a) * t

def run():
    global flip
    for i in range(0, 10_000_000):
        if i % 10_000 is 0:
            flip = not flip

        if flip:
            driveMotor.run(1000)
            print("yes")

run()