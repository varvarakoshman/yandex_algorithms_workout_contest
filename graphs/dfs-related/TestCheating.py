def test_cheating():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    is_bipartite = check_is_bipartite(adj_list)
    write_output(is_bipartite)


def check_is_bipartite(adj_list):
    vertexes_colored = {}
    is_bipartite = True
    for vertex, neighbours in adj_list.items():
        if vertex not in vertexes_colored:
            vertexes_colored[vertex] = 1
            is_bipartite = is_bipartite and dfs(adj_list, vertexes_colored, vertex, is_bipartite)
    return is_bipartite


def dfs(adj_list, vertexes_colored, vertex, is_bipartite):
    for neighbour in adj_list[vertex]:
        if not is_bipartite:
            break
        if neighbour not in vertexes_colored:
            vertexes_colored[neighbour] = 3 - vertexes_colored[vertex]
            is_bipartite = is_bipartite and dfs(adj_list, vertexes_colored, neighbour, is_bipartite)
        elif vertexes_colored[neighbour] == vertexes_colored[vertex]:
            is_bipartite = False
    return is_bipartite


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def construct_adjacency_list(input_graph):
    adj_list = {}
    params = input_graph[0].split()
    vertex_n, edges_n = int(params[0]), int(params[1])
    for i in range(vertex_n):
        adj_list[i + 1] = []
    for i in range(1, len(input_graph)):
        edge = input_graph[i].split()
        if len(edge) == 0:
            break
        vertex_from = int(edge[0])
        vertex_to = int(edge[1])
        adj_list[vertex_from].append(vertex_to)
        if vertex_from != vertex_to:
            adj_list[vertex_to].append(vertex_from)
    return adj_list


def write_output(can_cheat):
    with open('output.txt', 'w') as output:
        output.write("YES" if can_cheat else "NO")


test_cheating()
