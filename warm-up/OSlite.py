def find_num_working_os():
    coordinates = read_input()
    os_number = get_os_number(coordinates)
    write_output(os_number)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    n = int(lines[1])
    coordinates = []
    for i in range(2, n + 2):
        coords = [int(num) for num in lines[i].split(" ")]
        coordinates.append(coords)
    return coordinates


def get_os_number(coordinates):
    valid_intervals = {}
    for idx, coordinate in enumerate(coordinates):
        valid_intervals[idx] = True
        for prev_idx in range(idx - 1, -1, -1):
            if valid_intervals[prev_idx]:
                is_intersected = check_if_intersect(coordinate, coordinates[prev_idx])
                if is_intersected:
                    valid_intervals[prev_idx] = False
    count = 0
    for idx in range(len(coordinates)):
        if valid_intervals[idx]:
            count += 1
    return count


def check_if_intersect(new_interval, prev_interval):
    return True if prev_interval[0] <= new_interval[1] and new_interval[0] <= prev_interval[1] else False


def write_output(os_number):
    with open('output.txt', 'w') as output:
        output.write(str(os_number))


# O(n^2) time | O(n) space
find_num_working_os()