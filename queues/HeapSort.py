# O(n*logn) time | O(1) space
def heap_sort(array):
    heapify(array)
    heap_end_idx = len(array) - 1
    while heap_end_idx > 0:
        array[0], array[heap_end_idx] = array[heap_end_idx], array[0]
        heap_end_idx -= 1
        sift_down(array, 0, heap_end_idx)
    return array


# O(logn) time | O(1) space
def sift_down(array, parent_idx, heap_end_idx):
    left_child = parent_idx * 2 + 1
    while left_child <= heap_end_idx:
        max_child_idx = left_child
        right_child = parent_idx * 2 + 2
        if right_child <= heap_end_idx and array[right_child] > array[left_child]:
            max_child_idx = right_child
        if array[parent_idx] < array[max_child_idx]:
            array[parent_idx], array[max_child_idx] = array[max_child_idx], array[parent_idx]
        else:
            break
        parent_idx = max_child_idx
        left_child = parent_idx * 2 + 1


# O(n) time | O(1) space
def heapify(array):
    last_idx = len(array) - 1
    parent_idx = (last_idx - 1) // 2
    while parent_idx >= 0:
        sift_down(array, parent_idx, last_idx)
        parent_idx -= 1


def apply_heap_sort():
    n, elements = read_input()
    array = [int(elem) for elem in elements.strip().split()]
    heap_sort(array)
    write_output(array)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines[0], lines[1]


def write_output(array):
    with open('output.txt', 'w') as output:
        for elem in array:
            output.write(str(elem) + " ")


apply_heap_sort()
