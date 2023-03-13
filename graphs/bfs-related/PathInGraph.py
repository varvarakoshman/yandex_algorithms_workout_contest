def graph_min_path():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    start, end = [int(v) for v in input_graph[-1].split()]
    min_path = get_shortest_path(adj_list, start, end)
    write_output(min_path)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def get_shortest_path(adj_list, start, end):
    visited = {start}
    predecessors = [-1] * (len(adj_list) + 1)
    queue_vertices = [start]
    while len(queue_vertices) > 0:
        vertex = queue_vertices.pop(0)
        if vertex == end:
            break
        if vertex not in adj_list:
            continue
        for neighbour in adj_list[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                predecessors[neighbour] = vertex
                queue_vertices.append(neighbour)
    return unroll_path(predecessors, start, end)


def unroll_path(predecessors, start, end):
    first_in_path = predecessors[end]
    path = [end, first_in_path]
    while first_in_path != start:
        first_in_path = predecessors[first_in_path]
        path.append(first_in_path)
    path.reverse()
    return path


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


def write_output(shortest_path):
    with open('output.txt', 'w') as output:
        path_len = len(shortest_path) - 1
        output.write(str(path_len) + '\n')
        if path_len > 0:
            path_joined = " ".join([str(vertex) for vertex in shortest_path])
            output.write(path_joined)


graph_min_path()
