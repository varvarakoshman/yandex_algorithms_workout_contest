class Queue:
    def __init__(self, cards):
        self.max_elem = 10
        self.queue = [None] * self.max_elem
        for i in range(len(cards)):
            self.queue[i] = cards[i]
        self.head = 0
        self.tail = len(cards) - 1

    # O(1) time | O(1) space
    def push(self, n):
        idx = (self.tail + 1) % self.max_elem
        self.queue[idx] = n
        self.tail = idx
        if self.head == -1:
            self.head = 0

    # O(1) time | O(1) space
    def pop(self):
        curr_head = self.queue[self.head]
        if self.head == self.tail:
            self.tail = -1
            self.head = -1
        else:
            self.head = (self.head + 1) % self.max_elem
        return curr_head

    # O(1) time | O(1) space
    def size(self):
        if self.head == -1:
            return 0
        elif self.head <= self.tail:
            return self.tail - self.head + 1
        else:
            return self.max_elem - self.head + self.tail + 1


def emulate_drunk_card_game():
    player_1_cards, player_2_cards = read_input()
    winner, num_moves = find_winner(player_1_cards, player_2_cards)
    write_output(winner, num_moves)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    player_1_cards = [int(card) for card in lines[0].strip().split()]
    player_2_cards = [int(card) for card in lines[1].strip().split()]
    return player_1_cards, player_2_cards


def find_winner(player_1_cards, player_2_cards):
    queue_player_1 = Queue(player_1_cards)
    queue_player_2 = Queue(player_2_cards)
    count_moves = 0
    upper_bound = 10 ** 6
    while queue_player_1.size() != 0 and queue_player_2.size() != 0 and count_moves < upper_bound:
        card_player_1 = queue_player_1.pop()
        card_player_2 = queue_player_2.pop()
        diff = card_player_2 - card_player_1
        if diff > 0 and diff != 9 or diff == -9:
            queue_player_2.push(card_player_1)
            queue_player_2.push(card_player_2)
        else:
            queue_player_1.push(card_player_1)
            queue_player_1.push(card_player_2)
        count_moves += 1
    if count_moves == upper_bound:
        return "nobody", -1
    winner = "second" if queue_player_1.size() == 0 else "first"
    return winner, count_moves


def write_output(winner, num_moves):
    with open('output.txt', 'w') as output:
        if winner == "nobody":
            output.write("botva")
        else:
            output.write(winner + " " + str(num_moves))


emulate_drunk_card_game()