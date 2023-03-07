class Queue:
    def __init__(self):
        self.max_elem = 100
        self.queue = [None] * self.max_elem
        self.head = self.tail = -1

    # O(1) time | O(1) space (amortized)
    def push(self, n):
        if self.get_next_idx() == self.head:
            self.extend_queue()
        idx = self.get_next_idx()
        self.queue[idx] = n
        self.tail = idx
        if self.head == -1:
            self.head = 0
        return "ok"

    def get_next_idx(self):
        return (self.tail + 1) % self.max_elem

    # O(n) time | O(n) space
    def extend_queue(self):
        self.max_elem = int(self.max_elem * 1.5)
        new_queue = [None] * self.max_elem
        if self.head < self.tail:
            for i in range(len(self.queue)):
                new_queue[i] = self.queue[i]
        else:
            idx = 0
            for i in range(self.head, len(self.queue)):
                new_queue[idx] = self.queue[i]
                idx += 1
            for i in range(self.tail + 1):
                new_queue[idx] = self.queue[i]
                idx += 1
            self.head = 0
            self.tail = idx - 1
        self.queue = new_queue

    # O(1) time | O(1) space
    def pop(self):
        if self.size() == 0:
            return "error"
        curr_head = self.queue[self.head]
        if self.head == self.tail:
            self.tail = -1
            self.head = -1
        else:
            self.head = (self.head + 1) % self.max_elem
        return curr_head

    # O(1) time | O(1) space
    def front(self):
        return self.queue[self.head] if self.size() > 0 else "error"

    # O(1) time | O(1) space
    def size(self):
        if self.head == -1:
            return 0
        elif self.head <= self.tail:
            return self.tail - self.head + 1
        else:
            return self.max_elem - self.head + self.tail + 1

    # O(1) time | O(1) space
    def clear(self):
        self.queue = [None] * self.max_elem
        self.tail = -1
        self.head = -1
        return "ok"

    # O(1) time | O(1) space
    def exit(self):
        return "bye"


def process_queue():
    commands = read_input()
    command_results = execute_input_commands(commands)
    write_output(command_results)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def execute_input_commands(commands):
    queue = Queue()
    results = []
    for command in commands:
        if command.strip() == "exit":
            results.append(queue.exit())
            break
        results.append(execute_command(queue, command))
    return results


def execute_command(queue, command):
    command_name = command.split(" ")[0].strip()
    if command_name == "push":
        return queue.push(int(command.split(" ")[1]))
    elif command_name == "pop":
        return queue.pop()
    elif command_name == "front":
        return queue.front()
    elif command_name == "size":
        return queue.size()
    else:
        return queue.clear()


def write_output(command_results):
    with open('output.txt', 'w') as output:
        for result in command_results:
            output.write(str(result) + "\n")


process_queue()
