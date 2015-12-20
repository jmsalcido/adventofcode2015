# My idea:
# import pdb; pdb.set_trace()
# need to parse each instruction:
# possible values:
# - turn on x,y thru a,b
# - turn off x,y thru a,b
# - toggle x,y thru a,b
# where: x,y = first position
# and: a,b = second position
#
# example:
# [
#  [x,x,x,x],
#  [x,x,x,x],
#  [x,x,x,x],
#  [x,x,x,x]
# ]
#
# turn on 0,0 thru 1,1
# [
#  [o,o,x,x],
#  [o,o,x,x],
#  [x,x,x,x],
#  [x,x,x,x]
# ]
#
import re


def do():
    # problem1()
    problem2()


def problem1():
    width = 1000
    height = 1000
    universe = initUniverse(width, height)
    the_input = get_input('input')
    parsed_instruction = {}
    lights = 0
    for instruction in the_input:
        # parse each instruction
        # first group is the instruction
        # second group is x,y
        # third group is xb,yb
        parts = re.match(
            # (^.+)\s(\d+,\d+)\s\w+\s(\d+,\d+)\n # try with this too.
            r'(^.+)\s(\d+,\d+)\s\w+\s(\d+,\d+)\n', instruction)
        command = parts.group(1)
        x, y = parts.group(2).split(",")
        xb, yb = parts.group(3).split(",")
        rectangle = calculateRectangle(int(x), int(y), int(xb), int(yb))
        toggle = command == "toggle"
        # import pdb; pdb.set_trace()
        if toggle:
            toggleUniverse(universe, rectangle)
        else:
            turnOnOff(universe, command == "turn on", rectangle)
    for px in range(width):
        for py in range(height):
            if universe[px][py]:
                lights += 1
    print(lights)


def problem2():
    width = 1000
    height = 1000
    universe = initUniverse(width, height)
    the_input = get_input('input')
    parsed_instruction = {}
    lights = 0
    for instruction in the_input:
        # parse each instruction
        # first group is the instruction
        # second group is x,y
        # third group is xb,yb
        parts = re.match(
            # (^.+)\s(\d+,\d+)\s\w+\s(\d+,\d+)\n # try with this too.
            r'(^.+)\s(\d+,\d+)\s\w+\s(\d+,\d+)\n', instruction)
        command = parts.group(1)
        x, y = parts.group(2).split(",")
        xb, yb = parts.group(3).split(",")
        rectangle = calculateRectangle(int(x), int(y), int(xb), int(yb))
        # import pdb; pdb.set_trace()
        if command == "toggle":
            toggleUniverse2(universe, rectangle)
        if command == "turn on":
            turnOnOff2(universe, 1, rectangle)
        if command == "turn off":
            turnOnOff2(universe, -1, rectangle)
    print(sum([sum(x) for x in universe]))


def calculateRectangle(x, y, xb, yb):
    rectangle = []
    rigth = xb > x
    up = yb > y
    # area = (abs(x - xb) + 1) * (abs(y - yb) + 1)
    if (xb > x):
        range_x = range(x, xb + 1)
    else:
        range_x = range(xb, x + 1)
    if (yb > y):
        range_y = range(y, yb + 1)
    else:
        range_y = range(yb, y + 1)

    for px in range_x:
        for py in range_y:
            rectangle.append((px, py))
    return rectangle


def turnOnOff(universe, value, rectangle):
    for coordinate in rectangle:
        universe[coordinate[0]][coordinate[1]] = value
    return universe

def turnOnOff2(universe, value, rectangle):
    for coordinate in rectangle:
        # stupid 0 case
        if universe[coordinate[0]][coordinate[1]] == 0 and value == -1:
            universe[coordinate[0]][coordinate[1]] = 0
        else:
            universe[coordinate[0]][coordinate[1]] += value
    return universe


def toggleUniverse(universe, rectangle):
    for coordinate in rectangle:
        value = universe[coordinate[0]][coordinate[1]]
        universe[coordinate[0]][coordinate[1]] = not value
    return universe

def toggleUniverse2(universe, rectangle):
    for coordinate in rectangle:
        universe[coordinate[0]][coordinate[1]] += 2
    return universe


def initUniverse(width, height):
    # could be a simple dict with values for ON and no value for OFF.
    # I will use the list of lists.. fuck it.
    # this returns a False (turned off lights) array of [width]x[height]
    return [
        [False for x in range(width)]
        for x in range(height)
    ]

def initUniverse2(width, height):
    # could be a simple dict with values for ON and no value for OFF.
    # I will use the list of lists.. fuck it.
    # this returns a False (turned off lights) array of [width]x[height]
    return [
        [0 for x in range(width)]
        for x in range(height)
    ]


def get_input(filename):
    return open(filename, 'r')

if __name__ == "__main__":
    do()
