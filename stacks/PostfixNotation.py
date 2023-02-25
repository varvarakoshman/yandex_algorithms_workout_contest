ALLOWED_OPERATIONS = ["+", "-", "*"]


def compute_with_postfix_notation():
    expression = read_input()
    result = compute_expression(expression)
    write_output(result)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    expression = lines[0].strip().split(" ")
    return expression


def compute_expression(expression):
    stack_nums = []
    for symbol in expression:
        if symbol in ALLOWED_OPERATIONS:
            second, first = stack_nums.pop(), stack_nums.pop()
            temp_result = apply_operation(first, second, symbol)
            stack_nums.append(temp_result)
        else:
            stack_nums.append(int(symbol))
    return stack_nums[0]


def apply_operation(first, second, operation):
    if operation == "+":
        return first + second
    elif operation == "-":
        return first - second
    else:
        return first * second


def write_output(result):
    with open('output.txt', 'w') as output:
        output.write(str(result))


# O(N) time | O(N) space
compute_with_postfix_notation()