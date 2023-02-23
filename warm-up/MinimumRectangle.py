def find_minimum_rectangle():
    points_coordinates = read_input()
    target_coords = get_rectangle_coords(points_coordinates)
    write_output(target_coords)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    n = int(lines[0].strip())
    coordinates = []
    for i in range(1, n + 1):
        coords = lines[i].strip().split(" ")
        coordinates.append([int(coords[0]), int(coords[1])])
    return coordinates


def get_rectangle_coords(points_coordinates):
    max_x = min_x = points_coordinates[0][0]
    max_y = min_y = points_coordinates[0][1]
    for i in range(1, len(points_coordinates)):
        curr_x, curr_y = points_coordinates[i]
        max_x = max(max_x, curr_x)
        min_x = min(min_x, curr_x)
        max_y = max(max_y, curr_y)
        min_y = min(min_y, curr_y)
    return [str(min_x), str(min_y), str(max_x), str(max_y)]


def write_output(target_coords):
    with open('output.txt', 'w') as output:
        output.write(" ".join(target_coords))


# O(n) time | O(1) space, n - number of coordinates
find_minimum_rectangle()