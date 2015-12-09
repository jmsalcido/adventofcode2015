def do():
    input_value = get_input().read()
    # both santas start at the same point 0,0
    santa_pos_x, santa_pos_y = 0, 0
    robo_pos_x, robo_pos_y = 0, 0
    santa_turn = True
    houses = {}
    for char in input_value:
        # Im thinking to do:
        # have a hashtable that will contain the houses
        # Santa starts at 0,0.
        # The grid is infinite, so, the initial position is not interesting for us, 0,0 is a good starting point.
        # The Hashtable length will count the number of houses that received at least 1 present. -- first problem
        # 2 houses per visit?
        if santa_turn:
            pos_x, pos_y = santa_pos_x, santa_pos_y
        else:
            pos_x, pos_y = robo_pos_x, robo_pos_y
        add_to_pos(houses, pos_x, pos_y)
        if char == "^":
            pos_y += 1
        if char == ">":
            pos_x += 1
        if char == "v":
            pos_y -= 1
        if char == "<":
            pos_x -= 1
        add_to_pos(houses, pos_x, pos_y)
        if santa_turn:
            santa_pos_x, santa_pos_y = pos_x, pos_y
        else:
            robo_pos_x, robo_pos_y = pos_x, pos_y
        santa_turn = not santa_turn
    print("x:", pos_x, " y:", pos_y)
    print(len(houses.keys()))

def get_input():
    return open("input", "r")

def add_to_pos(d, pos_x, pos_y):
    key = (pos_x, pos_y)
    if key in d:
        d[key] += 1
    else:
        d[key] = 1
