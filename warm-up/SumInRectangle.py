def find_sum_in_rectangle():
    matrix, coordinates = read_input()
    prefix_sums_matrix = get_prefix_sums_matrix(matrix)
    rectangle_sums = compute_rectangle_sums(prefix_sums_matrix, coordinates)
    write_output(rectangle_sums)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    parameters = lines[0].strip().split(" ")
    n, m, k = int(parameters[0]), int(parameters[1]), int(parameters[2])
    matrix = []
    for i in range(1, n + 1):
        row = lines[i].strip().split(" ")
        matrix.append([int(row[j]) for j in range(0, len(row))])
    coordinates = []
    for i in range(n + 1, n + 1 + k):
        coords = [int(num) for num in lines[i].strip().split(" ")]
        coordinates.append(coords)
    return matrix, coordinates


def get_prefix_sums_matrix(matrix):
    prefix_sums_matrix = []
    for i in range(len(matrix)):
        row = matrix[i]
        prefix_sums = [0] * (len(row) + 1)
        for j in range(1, len(row) + 1):
            prefix_sums[j] = prefix_sums[j - 1] + row[j - 1]
        prefix_sums_matrix.append(prefix_sums)
    return prefix_sums_matrix


def compute_rectangle_sums(prefix_sums_matrix, coordinates):
    rectangle_sums = []
    for coords_i in coordinates:
        curr_sum = 0
        x_1, y_1, x_2, y_2 = coords_i
        for i in range(x_1 - 1, x_2):
            row = prefix_sums_matrix[i]
            curr_sum += row[y_2] - row[y_1 - 1]
        rectangle_sums.append(curr_sum)
    return rectangle_sums


def write_output(sums):
    with open('output.txt', 'w') as output:
        for sum_i in sums:
            output.write(str(sum_i) + '\n')


# O(N * M) time | O(N * M) space
find_sum_in_rectangle()