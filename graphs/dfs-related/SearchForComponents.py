# O(|V| + |E|) time | O(|V|) space
# (space time correct?)
def find_graph_components():
    input_graph = read_input()
    adj_list = construct_adjacency_list(input_graph)
    components = get_components(adj_list)
    write_output(components)


def get_components(adj_list):
    components = []
    visited = set()
    for vertex, neighbours in adj_list.items():
        if vertex in visited:
            continue
        component = [vertex]
        visited.add(vertex)
        for neighbour in neighbours:
            if neighbour not in visited:
                dfs(adj_list, visited, neighbour, component)
        components.append(component)
    return components


def dfs(adj_list, visited, vertex, component):
    visited.add(vertex)
    component.append(vertex)
    if vertex not in adj_list:
        return
    for neighbour in adj_list[vertex]:
        if neighbour not in visited:
            dfs(adj_list, visited, neighbour, component)


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


def write_output(components):
    with open('output.txt', 'w') as output:
        output.write(str(len(components)) + "\n")
        for component in components:
            vertex_sequence = [str(vertex) for vertex in component]
            output.write(str(len(vertex_sequence)) + "\n")
            output.write(" ".join(vertex_sequence) + "\n")


find_graph_components()
