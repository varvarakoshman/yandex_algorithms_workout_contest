def compute_number_jumps():
    n, k = read_input()
    jump_count = get_jump_count(n, k)
    write_output(jump_count)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    params = lines[0].strip().split()
    return int(params[0]), int(params[1])


# O(n) time | O(n) space
def get_jump_count(n, k):
    dp = [0] * n
    dp[0] = 1
    k_window_sum = dp[0]
    left_pointer = 0
    for i in range(1, n):
        dp[i] = k_window_sum
        k_window_sum += dp[i]
        if i > k - 1:
            k_window_sum -= dp[left_pointer]
            left_pointer += 1
    return dp[-1]


def write_output(result):
    with open('output.txt', 'w') as output:
        output.write(str(result))


compute_number_jumps()
