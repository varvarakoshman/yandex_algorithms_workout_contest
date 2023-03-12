# O(|V| + |E|) time | O(|V|) space
# (space time correct?)
def detect_cycle():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    cycle = get_cycle(adj_list)
    if len(cycle) != 0:
        cycle.append(cycle[0])
        del cycle[0]
    write_output(cycle)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    return lines


def construct_adjacency_list(input_graph):
    vertex_n = int(input_graph[0])
    adj_list = {}
    for i in range(vertex_n):
        adj_list[i + 1] = []
    for i in range(1, len(input_graph)):
        for idx, vertex in enumerate(input_graph[i].split()):
            value = int(vertex)
            if value == 1:
                adj_list[i].append(idx + 1)
    return adj_list


def get_cycle(adj_list):
    for vertex, other_vertices in adj_list.items():
        visited = {}
        if vertex in visited and visited[vertex] == 2:
            continue
        has_cycle, path, _ = dfs(adj_list, visited, vertex, -1, [], False)
        if has_cycle:
            return path
    return []


def dfs(adj_list, visited, vertex, prev_vertex, path, has_cycle):
    visited[vertex] = 1
    is_path_finished = False
    for neighbour in adj_list[vertex]:
        if has_cycle:
            break
        if neighbour in visited and visited[neighbour] == 2 or neighbour == prev_vertex:
            continue
        if neighbour not in visited:
            has_sub_cycle, path, is_path_finished = dfs(adj_list, visited, neighbour, vertex, path, has_cycle)
            if len(path) != 0 and neighbour == path[0]:
                is_path_finished = True
            if has_sub_cycle and not is_path_finished:
                path.append(neighbour)
            has_cycle = has_cycle or has_sub_cycle
        elif visited[neighbour] == 1:
            path.append(neighbour)
            has_cycle = True
    visited[vertex] = 2
    return has_cycle, path, is_path_finished


def write_output(cycle):
    with open('output.txt', 'w') as output:
        if len(cycle) == 0:
            output.write('NO')
        else:
            vertexes_str = [str(vertex) for vertex in cycle]
            output.write('YES' + '\n' + str(len(cycle)) + '\n' + " ".join(vertexes_str))


detect_cycle()
