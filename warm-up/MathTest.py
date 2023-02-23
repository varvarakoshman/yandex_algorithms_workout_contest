def math_test():
    n, k, petya_row, petya_position = read_input()
    result = get_vasya_target_place(n, k, petya_row, petya_position)
    write_output(result)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return int(lines[0]), int(lines[1]), int(lines[2]), int(lines[3])


def get_vasya_target_place(n, k, petya_row, petya_position):
    total_number_rows = n // 2 + n % 2
    petya_place_number = petya_row * 2
    if petya_position == 1:
        petya_place_number -= 1

    free_place_before = petya_place_number - k
    position_before, row_before = get_new_position(free_place_before)
    distance_before = petya_row - row_before - 1

    free_place_after = petya_place_number + k
    position_after, row_after = get_new_position(free_place_after)
    distance_after = row_after - petya_row - 1

    is_valid_before = row_before > 0
    is_valid_after = row_after <= total_number_rows and free_place_after <= n

    if is_valid_after and distance_after <= distance_before:
        return [int(row_after), 2 if position_after == 0 else 1]
    elif is_valid_before:
        return [int(row_before), 2 if position_before == 0 else 1]
    else:
        return [-1]


def get_new_position(free_place):
    position = free_place % 2
    row_after = free_place // 2 + position
    return position, row_after


def write_output(result):
    with open('output.txt', 'w') as output:
        if result[0] == -1:
            output.write(str(-1))
        else:
            output.write(str(result[0]) + " " + str(result[1]))


math_test()
