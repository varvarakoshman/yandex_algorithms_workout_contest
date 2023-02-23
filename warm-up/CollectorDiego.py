def find_distinct_stickers():
    diego_stickers, collectors_stickers = read_input()
    result = get_distinct_Diego_stickers(diego_stickers, collectors_stickers)
    write_output(result)
    return


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    diego_stickers = [int(sticker) for sticker in lines[1].split(" ")]
    collectors_stickers = [int(sticker) for sticker in lines[3].split(" ")]
    return diego_stickers, collectors_stickers


def get_distinct_Diego_stickers(diego_stickers, collectors_stickers):
    diego_stickers.sort()
    unique_stickers = get_diego_unique_map(diego_stickers)
    sticker_counts = []
    for collector_sticker in collectors_stickers:
        count_distinct_stickers = get_distinct_for_collector(collector_sticker, diego_stickers, unique_stickers)
        sticker_counts.append(count_distinct_stickers)
    return sticker_counts


def get_diego_unique_map(diego_stickers):
    unique_stickers = {0: 1}
    for i in range(1, len(diego_stickers)):
        if diego_stickers[i] != diego_stickers[i - 1]:
            unique_stickers[i] = unique_stickers[i - 1] + 1
        else:
            unique_stickers[i] = unique_stickers[i - 1]
    return unique_stickers


def get_distinct_for_collector(collector_sticker, diego_stickers, unique_stickers):
    left = 0
    right = len(diego_stickers) - 1
    count_distinct = 0
    while left <= right:
        if left == right:
            if diego_stickers[right] < collector_sticker:
                count_distinct = unique_stickers[right]
            break
        middle = (right + left) // 2
        if collector_sticker > diego_stickers[middle + 1]:
            left = middle + 1
        elif collector_sticker <= diego_stickers[middle]:
            right = middle - 1
        else:
            count_distinct = unique_stickers[middle]
            break
    return count_distinct


def write_output(result):
    with open('output.txt', 'w') as output:
        for sticker in result:
            output.write(str(sticker) + '\n')


# O(n*logn) time | O(n) space
find_distinct_stickers()