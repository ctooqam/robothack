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

