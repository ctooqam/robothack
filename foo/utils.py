def mean(measurements):
    return sum(measurements) / float(len(measurements))


def passed_white_black_white(measurements):
    """ First and last 25% should be bright. Middle 30% should be dark."""
    n = len(measurements)
    end_first = int(n * 0.25)
    start_last = int(n * 0.75)
    start_dark = int(n * 0.35)
    end_dark = int(n * 0.65)
    bright_1 = mean(measurements[:end_first])
    bright_2 = mean(measurements[start_last:])
    dark = mean(measurements[start_dark:end_dark])
    return bright_1 > 2 * dark and bright_2 > 2 * dark


def detect_black_line_callback(measurements)
    # Vi sparar de K senaste mätvärdena för att detektera när vi passerat ett vitt-svart-vitt område.
    # Beroede på robotens hastighet så kommer vi ha X mätvärden som tas över det mörka området. 
    # x ska motsvara ca 30-40% av K för att passed_white_black_white ska bli nöjd.
    dark_line_width = 25  # mm
    nbr_dark_samples = 100 * dark_line_width / DRIVE_SPEED
    K = int(nbr_dark_samples / 0.35)

    return len(measurements) > K and passed_white_black_white(measurements[len(measurements)-K:]):


def follow_line_until(line_sensor, other_sensor, callback, *, DRIVE_SPEED = 100, PROPORTIONAL_GAIN = 1.2):
    """
    Callback takes measurements from the second sensor. Returns True when we are finnished.
    
      DRIVE_SPEED       - Set the drive speed at 100 millimeters per second.
      PROPORTIONAL_GAIN - For example, if the light value deviates from the threshold by 10, the robot
                          steers at 10*1.2 = 12 degrees per second.
    """
    
    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2

    measurements = []

    while True:
        measurements.append(other_sensor.reflection())
        if len(measurements) > 10000:
            measurements = measurements[5000:]

        if callback(measurements):
            break

        deviation = line_sensor.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation

        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)

        # You can wait for a short time or do other things in this loop.
        wait(10)

