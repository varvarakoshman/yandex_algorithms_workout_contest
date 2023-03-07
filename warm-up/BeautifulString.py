import string


def beautiful_string():
    k, input_str = read_input()
    max_count = get_max_beautiful_len(k, input_str)
    write_output(max_count)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return int(lines[0]), lines[1].replace('\n', '')


# O(n*m) time, where n - string length, m - size of alphabet | O(1) space
def get_max_beautiful_len(k, input_str):
    alphabet = list(string.ascii_lowercase)
    global_max = 0
    for letter in alphabet:
        changes_count = k
        right_pointer, left_pointer = 0, 0
        while left_pointer < len(input_str) and left_pointer <= right_pointer:
            while changes_count != -1 and right_pointer < len(input_str):
                if input_str[right_pointer] != letter:
                    changes_count -= 1
                if changes_count != -1:
                    global_max = max(global_max, right_pointer - left_pointer)
                right_pointer += 1
            if right_pointer == len(input_str) and input_str[right_pointer - 1] == letter:
                global_max = max(global_max, right_pointer - left_pointer)
            else:
                global_max = max(global_max, right_pointer - 1 - left_pointer)
            if input_str[left_pointer] != letter:
                changes_count += 1
            left_pointer += 1
    return global_max


def write_output(max_count):
    with open('output.txt', 'w') as output:
        output.write(str(max_count))


beautiful_string()


#
# def get_max_beautiful_len(k, input_str):
#     alphabet = list(string.ascii_lowercase)
#     global_max = 0
#     for letter in alphabet:
#         changes_count = k
#         left_pointer, right_pointer = 0, 1
#         if input_str[left_pointer] != letter:
#             changes_count -= 1
#         while left_pointer < right_pointer < len(input_str):
#             if input_str[right_pointer] != letter:
#                 changes_count -= 1
#             if changes_count >= 0:
#                 right_pointer += 1
#             else:
#                 global_max = max(global_max, right_pointer - left_pointer)
#                 if input_str[left_pointer] != letter:
#                     changes_count += 1
#                 left_pointer += 1
#         global_max = max(global_max, right_pointer - left_pointer)
#     return global_max
