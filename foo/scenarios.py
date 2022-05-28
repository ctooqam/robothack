from utils import detect_black_line_callback, follow_line_until, stop_at_obstacle, sharp_white_black_edge


def scenarioA1(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
  follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
  follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
  robot.straight(-100)
  front_motor.run_target(100,-80)
  robot.straight(150)
  front_motor.run_target(100,0)
  follow_line_until(line_sensor, other_sensor, robot, detect_black_line_callback)
  robot.straight(100)
  front_motor.run_target(100,-80)
  robot.straight(-200)
  front_motor.run_target(100,0)
  robot.straight(200)
  # Helicopter
  follow_line_until(line_sensor, other_sensor, robot, lambda x: stop_at_obstacle(x, obstacle_sensor))
  robot.straight(100)


def scenarioA2(ev3, left_motor, right_motor, front_motor, line_sensor, other_sensor, robot, obstacle_sensor):
  # Move to train
  robot.straight(-200)
  robot.turn(90)
  follow_line_until(line_sensor, other_sensor, robot, sharp_white_black_edge)
