class Stack:
    def __init__(self):
        self.stack = []

    # O(1) time | O(1) space
    def push(self, n):
        self.stack.append(n)
        return "ok"

    # O(1) time | O(1) space
    def pop(self):
        if self.size() == 0:
            return "error"
        last_elem = self.stack[-1]
        del self.stack[-1]
        return last_elem

    # O(1) time | O(1) space
    def back(self):
        return self.stack[-1] if self.size() > 0 else "error"

    # O(1) time | O(1) space
    def size(self):
        return len(self.stack)

    # O(1) time | O(1) space
    def clear(self):
        self.stack = []
        return "ok"

    # O(1) time | O(1) space
    def exit(self):
        return "bye"


def process_stack():
    commands = read_input()
    command_results = execute_input_commands(commands)
    write_output(command_results)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def execute_input_commands(commands):
    stack = Stack()
    results = []
    for command in commands:
        if command.strip() == "exit":
            results.append(stack.exit())
            break
        results.append(execute_command(stack, command))
    return results


def execute_command(stack, command):
    command_name = command.split(" ")[0].strip()
    if command_name == "push":
        return stack.push(int(command.split(" ")[1]))
    elif command_name == "pop":
        return stack.pop()
    elif command_name == "back":
        return stack.back()
    elif command_name == "size":
        return stack.size()
    else:
        return stack.clear()


def write_output(command_results):
    with open('output.txt', 'w') as output:
        for result in command_results:
            output.write(str(result) + "\n")


process_stack()
