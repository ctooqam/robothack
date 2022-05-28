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
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.robotics import DriveBase

from utils import passed_white_black_white

ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Calculate the light threshold. Choose values based on your measurements.
BLACK = 9
WHITE = 85
threshold = (BLACK + WHITE) / 2

# Set the drive speed at 100 millimeters per second.
DRIVE_SPEED = 100

# Set the gain of the proportional line controller. This means that for every
# percentage point of light deviating from the threshold, we set the turn
# rate of the drivebase to 1.2 degrees per second.

# For example, if the light value deviates from the threshold by 10, the robot
# steers at 10*1.2 = 12 degrees per second.
PROPORTIONAL_GAIN = 1.2

# Start following the line endlessly.

# Vi sparar de K senaste mätvärdena för att detektera när vi passerat ett vitt-svart-vitt område.
# Beroede på robotens hastighet så kommer vi ha X mätvärden som tas över det mörka området. 
# x ska motsvara ca 30-40% av K för att passed_white_black_white ska bli nöjd.
dark_line_width = 25  # mm
nbr_dark_samples = 100 * dark_line_width / DRIVE_SPEED
K = int(nbr_dark_samples / 0.35)

measurements = []

while True:

    measurements.append(line_sensor.reflection())

    if len(measurements) > K and passed_white_black_white(measurements[len(measurements)-K:])
        ev3.speaker.beep()
        print("Detected white-black-white")

    # Calculate the deviation from the threshold.
    #deviation = line_sensor.reflection() - threshold
    # print(line_sensor.reflection())
    # ev3.screen.print(line_sensor.reflection())
    # Calculate the turn rate.
    turn_rate = PROPORTIONAL_GAIN * deviation

    # Set the drive base speed and turn rate.
    robot.drive(DRIVE_SPEED, turn_rate)

    # You can wait for a short time or do other things in this loop.
    wait(10)

    if len(measurments) > 10000:
        meaurements = measurements[5000:]
