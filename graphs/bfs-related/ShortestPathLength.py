def shortest_path_len():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    start, end = [int(v) for v in input_graph[-1].split()]
    path_len = get_shortest_path_len(adj_list, start, end)
    write_output(path_len)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


# BFS
def get_shortest_path_len(adj_list, start, end):
    destinations = [-1] * (len(adj_list) + 1)
    destinations[start] = 0
    queue_vertices = [start]
    while len(queue_vertices) > 0:
        if destinations[end] != -1:
            break
        vertex = queue_vertices.pop(0)
        if vertex not in adj_list:
            continue
        for neighbour in adj_list[vertex]:
            if destinations[neighbour] == -1:
                destinations[neighbour] = destinations[vertex] + 1
                queue_vertices.append(neighbour)
    return destinations[end]


def construct_adjacency_list(input_graph):
    vertex_n = int(input_graph[0])
    adj_list = {}
    for i in range(vertex_n):
        adj_list[i + 1] = []
    for i in range(1, len(input_graph) - 1):
        for idx, vertex in enumerate(input_graph[i].split()):
            value = int(vertex)
            if value == 1:
                adj_list[i].append(idx + 1)
    return adj_list


def write_output(shortest_path_len):
    with open('output.txt', 'w') as output:
        output.write(str(shortest_path_len))


shortest_path_len()
