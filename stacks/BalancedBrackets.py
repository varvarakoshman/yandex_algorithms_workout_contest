def check_if_input_brackets_balanced():
    sequence = read_input()
    is_balanced = check_if_balanced(sequence)
    write_output(is_balanced)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines[0].strip()


def check_if_balanced(sequence):
    closing_by_opening = {
        "(": ")",
        "[": "]",
        "{": "}"
    }
    opened = []
    for bracket in sequence:
        if bracket in closing_by_opening:
            opened.append(bracket)
        elif len(opened) == 0 or closing_by_opening[opened.pop()] != bracket:
            return False
    return len(opened) == 0


def write_output(is_balanced):
    with open('output.txt', 'w') as output:
        output.write("yes" if is_balanced else "no")


# O(N) time | O(n) space
check_if_input_brackets_balanced()
