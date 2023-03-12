# O(|V| + |E|) time | O(|V|) space
# (space time correct?)
def apply_top_sort():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    has_cycle = check_has_cycle(adj_list)
    if has_cycle:
        write_output([])
    else:
        sorted_vertexes = topological_sort(adj_list)
        write_output(sorted_vertexes)


def check_has_cycle(adj_list):
    visited = {}
    has_cycle = False
    for vertex, neighbours in adj_list.items():
        if vertex not in visited:
            has_cycle = dfs_cycle(adj_list, visited, vertex)
            if has_cycle:
                break
    return has_cycle


def dfs_cycle(adj_list, visited, vertex):
    has_cycle = False
    visited[vertex] = 1
    for neighbour in adj_list[vertex]:
        if has_cycle:
            break
        if neighbour not in visited:
            has_cycle = has_cycle or dfs_cycle(adj_list, visited, neighbour)
        elif visited[neighbour] == 2:
            continue
        else:
            return True
    visited[vertex] = 2
    return has_cycle


def topological_sort(adj_list):
    visited = set()
    sorted_vertexes = []
    for vertex, neighbours in adj_list.items():
        if vertex not in visited:
            dfs(adj_list, visited, vertex, sorted_vertexes)
    sorted_vertexes.reverse()
    return sorted_vertexes


def dfs(adj_list, visited, vertex, path):
    visited.add(vertex)
    for neighbour in adj_list[vertex]:
        if neighbour not in visited:
            dfs(adj_list, visited, neighbour, path)
    path.append(vertex)


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
    return adj_list


def write_output(sorted_vertexes):
    with open('output.txt', 'w') as output:
        sorted_vertexes_str = [str(vertex) for vertex in sorted_vertexes]
        output.write(str(-1) if len(sorted_vertexes) == 0 else " ".join(sorted_vertexes_str))


apply_top_sort()
