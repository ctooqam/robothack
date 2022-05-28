#!/usr/bin/env pybricks-micropython
"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Color Sensor Down Program
----------------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase
from scenarios import scenarioA
from utils import detect_black_line_callback, follow_line_until, stop_at_obstacle

ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
front_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S4)
other_sensor = ColorSensor(Port.S1)
obstacle_sensor = UltrasonicSensor(Port.S3)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

scenarioA1(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor)
scenarioA2(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor)
print("Done!")
