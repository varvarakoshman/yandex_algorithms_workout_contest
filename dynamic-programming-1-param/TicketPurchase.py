# O(n) time | O(n) space
def ticket_purchase():
    n, time_table = read_input()
    optimal_time = get_min_purchase_time(n, time_table)
    write_output(optimal_time)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    n = int(lines[0])
    time_table = [[], [], []]
    # create 3 virtual people, so that dp-formula works for the 1st in line
    for i in range(3):
        time_table[0].append(float('inf'))
        time_table[1].append(float('inf'))
        time_table[2].append(float('inf'))
    for i in range(1, len(lines)):
        values = lines[i].split()
        time_table[0].append(int(values[0]))
        time_table[1].append(int(values[1]))
        time_table[2].append(int(values[2]))
    return n, time_table


def get_min_purchase_time(n, time_table):
    a, b, c = time_table
    dp = [0, 0, 0]
    for i in range(3, n + 3):
        optimal_time = min(dp[i - 1] + a[i], dp[i - 2] + b[i - 1], dp[i - 3] + c[i - 2])
        dp.append(optimal_time)
    return dp[-1]


def write_output(optimal_time):
    with open('output.txt', 'w') as output:
        output.write(str(optimal_time))


ticket_purchase()
