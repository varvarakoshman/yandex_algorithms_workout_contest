import string


def process_favorite_word():
    favorite_word = read_input().strip()
    letter_frequencies = compute_letter_frequencies(favorite_word)
    write_output(letter_frequencies)


def read_input():
    with open("input.txt") as input:
        return input.readlines()[0]


def compute_letter_frequencies(favorite_word):
    letter_frequencies = {}
    for idx, letter in enumerate(favorite_word):
        frequency = (idx + 1) * (len(favorite_word) - idx)
        letter_frequencies[letter] = letter_frequencies.get(letter, 0) + frequency
    return letter_frequencies


def write_output(letter_frequencies):
    alphabet = string.ascii_lowercase
    with open('output.txt', 'w') as output:
        for letter in alphabet:
            if letter in letter_frequencies:
                output.write(letter + ": " + str(letter_frequencies[letter]) + '\n')


# O(n) time | O(n) space, n - number of letters in favourite word
process_favorite_word()
