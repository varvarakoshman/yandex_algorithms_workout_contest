def apply_dfs():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    visited = []
    dfs(adj_list, visited, 1)
    visited.sort()
    write_output(visited)


def dfs(adj_list, visited, vertex):
    visited.append(vertex)
    if vertex not in adj_list:
        return
    for child in adj_list[vertex]:
        if child not in visited:
            dfs(adj_list, visited, child)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def construct_adjacency_list(input_graph):
    adj_list = {}
    for i in range(1, len(input_graph)):
        edge = input_graph[i].split()
        if len(edge) == 0:
            break
        vertex_from = int(edge[0])
        vertex_to = int(edge[1])
        if vertex_from not in adj_list:
            adj_list[vertex_from] = [vertex_to]
        else:
            adj_list[vertex_from].append(vertex_to)
        if vertex_to not in adj_list:
            adj_list[vertex_to] = [vertex_from]
        elif vertex_from != vertex_to:
            adj_list[vertex_to].append(vertex_from)
    return adj_list


def write_output(vertex_seq):
    str_sequence = [str(vertex) for vertex in vertex_seq]
    with open('output.txt', 'w') as output:
        output.write(str(len(vertex_seq)) + "\n" + " ".join(str_sequence))


apply_dfs()
