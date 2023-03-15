def graph_min_path():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    start, end = [int(v) for v in input_graph[-1].split()]
    min_path, min_path_len = get_shortest_path(adj_list, start, end)
    write_output(min_path, min_path_len)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def get_shortest_path(adj_list, start, end):
    if start == end:
        return [], 0
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
    if predecessors[end] != -1:
        path = unroll_path(predecessors, start, end)
        return path, len(path) - 1
    else:
        return [], -1


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


def write_output(min_path, min_path_len):
    with open('output.txt', 'w') as output:
        output.write(str(min_path_len) + '\n')
        if min_path_len > 0:
            path_joined = " ".join([str(vertex) for vertex in min_path])
            output.write(path_joined)


graph_min_path()
