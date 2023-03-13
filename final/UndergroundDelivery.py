class DeliveryStack:
    def __init__(self):
        self.stack = []
        self.product_index = {}

    def add(self, product, count):
        self.stack.append([product, count])
        self.product_index[product] = self.product_index.get(product, 0) + count

    def delete(self, count):
        while count > 0 and len(self.stack) > 0:
            last_vagon = self.stack[-1]
            if last_vagon[1] > count:
                self.stack[-1][1] = last_vagon[1] - count
                self.product_index[last_vagon[0]] -= count
                break
            self.stack.pop()
            count -= last_vagon[1]
            self.product_index[last_vagon[0]] -= last_vagon[1]

    def get(self, product):
        return self.product_index[product] if product in self.product_index else 0


def underground_delivery():
    commands = read_input()
    delivery_stack = DeliveryStack()
    result = execute_commands(delivery_stack, commands)
    write_output(result)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def execute_commands(delivery_stack, commands):
    result = []
    for i in range(1, len(commands)):
        command = commands[i].split()
        if len(command) == 3:
            delivery_stack.add(command[2], int(command[1]))
        elif command[0] == 'get':
            result.append(delivery_stack.get(command[1]))
        else:
            delivery_stack.delete(int(command[1]))
    return result


def write_output(commands_results):
    with open('output.txt', 'w') as output:
        for command_result in commands_results:
            output.write(str(command_result) + '\n')


underground_delivery()
