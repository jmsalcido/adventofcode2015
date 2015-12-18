def do():
    problem()
    problem2()

def problem():
    input_file = readFile()
    value = input_file.read()
    sum_value = 0
    for x in value:
        if x == '(':
            sum_value+=1
        if x == ')':
            sum_value-=1
    input_file.close()
    print(sum_value)

def problem2():
    input_file = readFile()
    value = input_file.read()
    input_file.close()
    sum_value = 0
    position = 0
    for x in value:
        if sum_value == -1:
            break
        if x == "(":
            sum_value+=1
        if x == ")":
            sum_value-=1
        position+=1
    print("floor: " + str(sum_value))
    print("position: " + str(position))

def readFile():
    return open('input', 'r')
