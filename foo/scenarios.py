from utils import *


def scenarioA1(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
    follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
    follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
    robot.straight(-100)
    front_motor.run_target(100, -80)
    robot.straight(150)
    front_motor.run_target(100, 0)
    follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
    robot.straight(100)
    front_motor.run_target(100, -80)
    robot.straight(-200)
    front_motor.run_target(100, 0)
    robot.straight(200)
    # Helicopter
    follow_line_until(line_sensor, other_sensor, robot, lambda x: stop_at_obstacle(x, obstacle_sensor))
    robot.straight(100)


def scenarioA2(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
    # Move to train
    robot.straight(-150)
    robot.turn(90)
    robot.straight(80)
    move_straight_until(other_sensor, robot, sharp_white_black_edge)
    robot.turn(20)
    # rotate_ccw_until(other_sensor, robot, lambda measurements: sharp_white_black_edge(measurements, reversed=True), speed=20)


def scenarioA3(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
    follow_line_until(other_sensor, line_sensor, robot, lambda x: stop_at_obstacle(x, obstacle_sensor, 155), side_factor=-1, PROPORTIONAL_GAIN=0.9)
    robot.turn(-15)
    front_motor.run_target(100, 80)
    robot.turn(45)
    front_motor.run_target(100, 0)
    robot.turn(-65)
    robot.straight(-150)
    robot.turn(195)
    move_straight_until(other_sensor, robot, sharp_white_black_edge)


def scenarioA4(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
    print("Scenario A4")
    rotate_ccw_until(line_sensor, robot, lambda measurements: sharp_white_black_edge(measurements, reversed=True), speed=20)
