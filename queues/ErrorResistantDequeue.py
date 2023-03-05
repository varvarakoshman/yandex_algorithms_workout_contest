class Dequeue:
    def __init__(self):
        self.front_ = self.rear = -1
        self.threshold = 100
        self.elements = [None] * self.threshold

    # O(1) time | O(1) space
    def push_front(self, n):
        self.front_ -= 1
        if self.front_ < 0:
            self.front_ = self.threshold - 1
        self.elements[self.front_] = n
        self.rear = self.front_ if self.rear == -1 else self.rear
        return 'ok'

    # O(1) time | O(1) space amortized
    def push_back(self, n):
        self.rear += 1
        self.elements[self.rear % self.threshold] = n
        self.front_ = self.rear if self.front_ == -1 else self.front_
        return 'ok'

    # O(1) time | O(1) space
    def pop_front(self):
        popped_elem = self.front()
        if popped_elem != 'error':
            if self.rear == self.front_:
                self.front_ = self.rear = -1
            elif self.front_ == self.threshold - 1:
                self.front_ = 0
            else:
                self.front_ += 1
        return popped_elem

    # O(1) time | O(1) space
    def pop_back(self):
        popped_elem = self.back()
        if popped_elem != 'error':
            if self.rear == self.front_:
                self.front_ = self.rear = -1
            elif self.rear == 0:
                self.rear = self.threshold - 1
            else:
                self.rear -= 1
        return popped_elem

    # O(1) time | O(1) space
    def front(self):
        return self.elements[self.front_ % self.threshold] if self.size() > 0 else 'error'

    # O(1) time | O(1) space
    def back(self):
        return self.elements[self.rear % self.threshold] if self.size() > 0 else 'error'

    # O(1) time | O(1) space
    def size(self):
        if self.front_ == -1 and self.rear == -1:
            return 0
        elif self.front_ <= self.rear:
            return self.rear - self.front_ + 1
        else:
            right_part = self.threshold - self.front_
            left_part = self.rear + 1
            return left_part + right_part

    # O(1) time | O(1) space
    def clear(self):
        self.elements = [None] * self.threshold
        self.front_ = self.rear = -1
        return "ok"

    # O(1) time | O(1) space
    def exit(self):
        return "bye"


def process_deque():
    commands = read_input()
    command_results = execute_input_commands(commands)
    write_output(command_results)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def execute_input_commands(commands):
    dequeue = Dequeue()
    results = []
    for command in commands:
        if command.strip() == "exit":
            results.append(dequeue.exit())
            break
        results.append(execute_command(dequeue, command))
    return results


def execute_command(dequeue, command):
    command_name = command.split(" ")[0].strip()
    if command_name == "push_back":
        return dequeue.push_back(int(command.split(" ")[1]))
    elif command_name == "push_front":
        return dequeue.push_front(int(command.split(" ")[1]))
    elif command_name == "pop_back":
        return dequeue.pop_back()
    elif command_name == "pop_front":
        return dequeue.pop_front()
    elif command_name == "front":
        return dequeue.front()
    elif command_name == "back":
        return dequeue.back()
    elif command_name == "size":
        return dequeue.size()
    else:
        return dequeue.clear()


def write_output(command_results):
    with open('output.txt', 'w') as output:
        for result in command_results:
            output.write(str(result) + "\n")

process_deque()
