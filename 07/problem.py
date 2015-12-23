import re


calculated_instructions = {}
instructions = {}


def do():
    problem1() # for problem 2, just override value in input to be whatever a gives first.


def problem1():
    the_input = get_input("input")
    for instruction in the_input:
        wire_instructions = instruction.split("->")
        wire_instruction = wire_instructions[0].strip()
        wired_value = wire_instructions[1].strip()
        match = re.match(r'^\d+$', wire_instruction)
        if match is not None:
            calculated_instructions[wired_value] = int(match.group())
        instructions[wired_value] = wire_instruction
    print(do_instruction("a"))


def do_instruction(signal):
    if signal in calculated_instructions:
        # import pdb; pdb.set_trace()
        return calculated_instructions[signal]
    if type(str_to_int_optional(signal)) == int:
        return str_to_int_optional(signal)
    instruction = instructions[signal]
    match = re.match(
        r'^(|.+)(OR|AND|NOT|RSHIFT|LSHIFT)\s(\w+)|^\d+|\w+', instruction)
    value1 = str_to_int_optional(match.group(1))
    operation = match.group(2)
    value2 = str_to_int_optional(match.group(3))
    if operation is None:
        value = do_instruction(match.group().strip())
    elif operation == "NOT":
        if type(value2) == int:
            value = ~value2
        else:
            value = ~do_instruction(value2)
    else:
        num1, num2 = get_values(value1, value2)
        if operation == "OR":
            value = num1 | num2
        elif operation == "AND":
            value = num1 & num2
        elif operation == "RSHIFT":
            value = num1 >> num2
        elif operation == "LSHIFT":
            value = num1 << num2
    calculated_instructions[signal] = value
    return value


def get_values(a, b):
    result = []
    if type(a) == int:
        result.append(a)
    else:
        result.append(do_instruction(a))
    if type(b) == int:
        result.append(b)
    else:
        result.append(do_instruction(b))
    return result


def str_to_int_optional(value):
    if value is None:
        return None
    match = re.match(r'^\d+$', value)
    if match is not None:
        return int(match.group())
    return value.strip()


def get_input(filename):
    return open(filename, "r")

if __name__ == "__main__":
    do()
