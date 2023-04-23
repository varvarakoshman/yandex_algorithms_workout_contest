def calculator():
    n = read_input()
    steps_count, steps = get_optimal_operations(n)
    write_output(steps_count, steps)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return int(lines[0])


# O(n) time | O(n) space
def get_optimal_operations(n):
    prev, dp = [0] * (n + 1), [0] * (n + 1)
    for i in range(2, n + 1):
        options = [i - 1]
        if i % 2 == 0:
            options.append(i // 2)
        if i % 3 == 0:
            options.append(i // 3)
        optimal_option_idx = min(options, key=lambda idx: dp[idx])
        prev[i] = optimal_option_idx
        dp[i] = dp[optimal_option_idx] + 1
    return dp[-1], get_step_sequence(prev, n)


def get_step_sequence(prev, n):
    step_sequence = []
    latest = -1
    while prev[latest] != 0:
        step_sequence.append(str(prev[latest]))
        latest = prev[latest]
    step_sequence.reverse()
    step_sequence.append(str(n))
    return step_sequence


def write_output(steps_count, steps):
    with open('output.txt', 'w') as output:
        output.write(str(steps_count) + "\n" + " ".join(steps))


calculator()
