# O(n*logn) time | O(n) space
def nails():
    coordinates = read_input()
    optimal_distance = get_optimal_distance(coordinates)
    write_output(optimal_distance)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return [int(coord) for coord in lines[1].split()]


def get_optimal_distance(coordinates):
    coordinates.sort()
    dp = [0] * (len(coordinates) + 1)
    dp[1] = float('inf')
    for i in range(1, len(coordinates)):
        dp_idx = i + 1
        dp[dp_idx] = min(dp[dp_idx - 2], dp[dp_idx - 1]) + (coordinates[i] - coordinates[i - 1])
    return dp[-1]


def write_output(optimal_distance):
    with open('output.txt', 'w') as output:
        output.write(str(optimal_distance))


nails()
