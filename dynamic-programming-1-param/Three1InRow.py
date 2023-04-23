def compute_sequences():
    sequence_len = read_input()
    sequence_number = get_sequence_number(sequence_len)
    write_output(sequence_number)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return int(lines[0])


# My initial solution
# O(n) time | O(1) space
def get_sequence_number_1(n):
    if n <= 2:
        return n * 2
    if n == 3:
        return 2 ** 3 - 1
    counts = [2, 4, 7, 0]
    for i in range(3, n):
        invalid_num = 1 if i < 4 else counts[i % 4]
        counts[i % 4] = counts[(i - 1) % 4] * 2 - invalid_num
    return counts[n % 4 - 1]


# Solution suggested by lecturer
# O(n) time | O(n) space
# есть 3 варианта:
# 1) на конце 0
# 2) на конце 1 единица
# 3) на конце 2 единицы
# dp[i] - число валидных последовательностей из i цифр
# _ _ _ 0 - dp[i - 1]
# _ _ 0 1 - dp[i - 2]
# _ 0 1 1 - dp[i - 3]
# найти число вариантов на i шаге - сложить число вариантов для каждого шаблона
def get_sequence_number(n):
    if n <= 2:
        return n * 2
    if n == 3:
        return 2 ** 3 - 1
    dp = [0] * n
    dp[0] = 2
    dp[1] = 4
    dp[2] = 7
    for i in range(3, n):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    return dp[-1]


def write_output(result):
    with open('output.txt', 'w') as output:
        output.write(str(result))


compute_sequences()
