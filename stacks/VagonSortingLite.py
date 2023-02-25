def sort_vagons():
    vagons_1_track = read_input()
    is_sortable = check_if_sortable(vagons_1_track)
    write_output(is_sortable)


def read_input():
    with open("input.txt") as input:
        lines = input.readlines()
    vagons_1_track = [int(vagon) for vagon in lines[1].strip().split()]
    return vagons_1_track


def check_if_sortable(vagons_1_track):
    last_target_vagon = 1
    stack = []
    for vagon in vagons_1_track:
        if vagon == last_target_vagon:
            last_target_vagon += 1
            while len(stack) > 0 and stack[-1] == last_target_vagon:
                stack.pop()
                last_target_vagon += 1
        else:
            stack.append(vagon)
    return len(stack) == 0


def write_output(is_sortable):
    with open('output.txt', 'w') as output:
        output.write("YES" if is_sortable else "NO")


sort_vagons()
