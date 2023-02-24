SEC_IN_DAY = 24 * 60 * 60


def find_accurate_time():
    a, b, c = read_input()
    accurate_time = get_accurate_time(a, b, c)
    write_output(accurate_time)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines[0].strip(), lines[1].strip(), lines[2].strip()


def get_accurate_time(a, b, c):
    delay_one_way_sec = get_one_way_delay(a, c)
    new_time_sec = get_delayed_server_time_sec(b, delay_one_way_sec)
    return get_formatted_time(new_time_sec)


def get_one_way_delay(a, c):
    a_time = [int(ai) for ai in a.split(":")]
    c_time = [int(ci) for ci in c.split(":")]
    a_time_sec = get_time_sec(a_time)
    c_time_sec = get_time_sec(c_time)
    delta = c_time_sec - a_time_sec if c_time_sec >= a_time_sec else (SEC_IN_DAY - a_time_sec) + c_time_sec
    delta_one_way = arithmetic_round(delta / 2)
    return delta_one_way


def get_time_sec(time):
    return time[0] * 60 * 60 + time[1] * 60 + time[2]


def arithmetic_round(number):
    fractional_part = number % 1
    number = number - fractional_part
    if fractional_part >= 0.5:
        number += 1
    return int(number)


def get_delayed_server_time_sec(b, delay_one_way_sec):
    b_time = [int(bi) for bi in b.split(":")]
    b_time_sec = get_time_sec(b_time)
    delayed_time = b_time_sec + delay_one_way_sec
    if delayed_time > SEC_IN_DAY:
        delayed_time = delayed_time - SEC_IN_DAY
    return delayed_time


def get_formatted_time(time_sec):
    hh = time_sec // 3600
    mm_ss = time_sec - hh * 3600
    mm = mm_ss // 60
    ss = mm_ss - mm * 60
    return [str(hh) if hh > 9 else "0" + str(hh),
            str(mm) if mm > 9 else "0" + str(mm),
            str(ss) if ss > 9 else "0" + str(ss)]


def write_output(accurate_time):
    with open('output.txt', 'w') as output:
        output.write(":".join(accurate_time))


# O(1) time | O(1) space
find_accurate_time()
