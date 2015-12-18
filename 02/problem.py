def do():
    problem()
    problem2()

def get_input_list():
    input_value = open('input', 'r')
    lines = []
    for x in input_value:
        value = x[:-1].split("x")
        lines.append(value)
    return lines

def problem():
    values = get_input_list()
    sum_value = 0
    for value in values:
        a = int(value[0])
        b = int(value[1])
        c = int(value[2])
        ab = a*b
        bc = b*c
        ca = c*a
        val = (2*(ab)) + (2*(bc)) + (2*(ca))
        slack = min(ab,bc,ca)
        sum_value += val + slack
    print(sum_value)

def problem2():
    values = get_input_list()
    sum_value = 0
    for value in values:
        a = int(value[0])
        b = int(value[1])
        c = int(value[2])
        ribbon = (2 * min(a+b, b+c, c+a)) + (a*b*c)
        print(ribbon)
        sum_value += ribbon
    print(sum_value)
