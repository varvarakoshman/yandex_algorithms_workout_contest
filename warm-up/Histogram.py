def historgam():
    input_seq = read_input()
    char_frequencies = get_char_frequencies(input_seq)
    frequency_chars, max_freq = get_frequency_chars(char_frequencies)
    sorted_chars = sorted(char_frequencies.keys())  # O(n*logn) time | O(n) space
    draw_histogram(sorted_chars, frequency_chars, max_freq)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return ''.join(lines)


# O(n) time | O(n) space
def get_char_frequencies(input_seq):
    char_frequencies = {}
    exclusions = ['\n', ' ']
    for char in input_seq:
        if char not in exclusions:
            char_frequencies[char] = char_frequencies.get(char, 0) + 1
    return char_frequencies


# O(n) time | O(n) space
def get_frequency_chars(char_frequencies):
    frequency_chars = {}
    max_freq = 0
    for char, frequency in char_frequencies.items():
        max_freq = max(max_freq, frequency)
        if frequency not in frequency_chars:
            frequency_chars[frequency] = [char]
        else:
            frequency_chars[frequency].append(char)
    return frequency_chars, max_freq


# O(n^2) time | O(n) space
def draw_histogram(sorted_chars, frequency_chars, max_freq):
    with open('output.txt', 'w') as f:
        new_line = [' ' for _ in sorted_chars]
        for counter in range(max_freq, 1, -1):
            if counter in frequency_chars:
                for char in frequency_chars[counter]:
                    new_line[sorted_chars.index(char)] = '#'
            f.write(''.join(new_line) + '\n')
        f.write('#' * len(sorted_chars) + '\n')
        f.write(''.join(sorted_chars) + '\n')


historgam()
