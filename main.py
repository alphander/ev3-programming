#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
import math
from vector import Vector

drive = 1/3
pan = 1/56
tilt = 1/56
driveMotor = Motor(Port.D)
panMotor = Motor(Port.B)
tiltMotor = Motor(Port.C)

positionA = Vector(0, 0, 0)
positionB = Vector(12.4, 1.4, 3.3)

steps = 1000

for i in range(100, steps+1):
    t = i * 10
    driveMotor.run_time(t, 1, then=Stop.COAST, wait=True)


#for i in range(0, steps+1):
#    t = (i / steps)
#    position = positionA.lerp(t, positionB)