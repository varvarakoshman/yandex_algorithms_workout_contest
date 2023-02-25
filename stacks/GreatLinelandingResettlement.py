def resettle_cities():
    cities_costs = read_input()
    new_settlement = move_cities(cities_costs)
    write_output(new_settlement)


def read_input():
    with open('input.txt') as input:
        lines = input.readlines()
    cities_costs = [int(cost) for cost in lines[1].strip().split()]
    return cities_costs


def move_cities(cities_costs):
    new_settlement = ['-1'] * len(cities_costs)
    stack = [[0, cities_costs[0]]]
    for city_idx in range(1, len(cities_costs)):
        city_cost = cities_costs[city_idx]
        while len(stack) > 0 and city_cost < stack[-1][1]:
            new_settlement[stack.pop()[0]] = str(city_idx)
        else:
            stack.append([city_idx, city_cost])
    return new_settlement


def write_output(new_settlement):
    with open('output.txt', 'w') as output:
        output.write(' '.join(new_settlement))


# O(n) time | O(n) space
resettle_cities()
