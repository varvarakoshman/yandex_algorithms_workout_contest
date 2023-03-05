class Heap:
    def __init__(self):
        self.elements = []

    # O(logn) time | O(1) space
    def insert(self, k):
        self.elements.append(k)
        curr_idx = len(self.elements) - 1
        while self.elements[max(0, (curr_idx - 1)) // 2] < self.elements[curr_idx]:
            parent_idx = (curr_idx - 1) // 2
            self.elements[parent_idx], self.elements[curr_idx] = self.elements[curr_idx], self.elements[parent_idx]
            curr_idx = parent_idx

    # O(logn) time | O(1) space
    def extract(self):
        extracted_elem = self.elements[0]
        self.elements[0] = self.elements[-1]
        parent_idx, left_idx, right_idx = 0, 1, 2
        while right_idx < len(self.elements):
            max_child_idx = right_idx if self.elements[right_idx] > self.elements[left_idx] else left_idx
            if self.elements[parent_idx] < self.elements[max_child_idx]:
                self.elements[parent_idx], self.elements[max_child_idx] = \
                    self.elements[max_child_idx], self.elements[parent_idx]
            else:
                break
            parent_idx = max_child_idx
            left_idx = 2 * parent_idx + 1
            right_idx = 2 * parent_idx + 2
        self.elements.pop()
        return extracted_elem


def process_heap():
    commands = read_input()
    command_results = execute_input_commands(commands)
    write_output(command_results)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def execute_input_commands(commands):
    heap = Heap()
    results = []
    for i in range(1, len(commands)):
        command_name = commands[i]
        command = command_name.strip().split()
        if len(command) > 1:
            heap.insert(int(command[1]))
        else:
            results.append(heap.extract())
    return results


def write_output(command_results):
    with open('output.txt', 'w') as output:
        for result in command_results:
            output.write(str(result) + "\n")


process_heap()
