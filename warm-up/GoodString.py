def good_string():
    frequencies = read_input()
    result = get_good_string_len(frequencies)
    write_output(result)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    n = int(lines[0])
    frequencies = []
    for i in range(1, n + 1):
        frequencies.append(int(lines[i]))
    return frequencies


def get_good_string_len(frequencies):
    count = 0
    if len(frequencies) < 2:
        return count
    for i in range(1, len(frequencies)):
        if frequencies[i - 1] <= frequencies[i]:
            count += frequencies[i - 1]
        else:
            count += frequencies[i]
    return count


def write_output(max_count):
    with open('output.txt', 'w') as output:
        output.write(str(max_count))


good_string()
