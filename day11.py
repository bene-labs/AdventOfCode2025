from functools import cache


class Node:
    def __init__(self, connected_nodes: list, name: str):
        self.connected_nodes = connected_nodes
        self.id : str = name


def count_paths_to(nodes, start: str, end: str) -> int:

    @cache
    def _count_paths_to_rec(current: str, goal: str)-> int:
        if current == goal:
            return 1
        return sum([_count_paths_to_rec(next_node.id, goal) for next_node in nodes[current].connected_nodes])

    return _count_paths_to_rec(start, end)


def count_paths_along(nodes, start: str, end: str, to_visit: frozenset[str]) -> int:

    @cache
    def _count_paths_along_rec(current: str, goal: str, must_visit: frozenset[str])-> int:
        if current in must_visit:
            must_visit = must_visit - {current}
        elif current == goal:
            return 1 if len(must_visit) == 0 else 0
        return sum([_count_paths_along_rec(next_node.id, goal, must_visit) for next_node in nodes[current].connected_nodes])

    return _count_paths_along_rec(start, end, to_visit)


def get_nodes(input_path: str)->dict[str, Node]:
    unique_nodes: dict[str, Node] = {}
    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        for line in input_file.read().splitlines():
            name, connected_to = line.split(':')
            connected_nodes = []
            for node in connected_to.strip().split(' '):
                if not node in unique_nodes:
                    unique_nodes[node] = Node([], node)
                connected_nodes.append(unique_nodes[node])
            if name in unique_nodes:
                unique_nodes[name].connected_nodes += connected_nodes
            else:
                unique_nodes[name] = Node(connected_nodes, name)
    return unique_nodes


def day11_part1(input_path: str)->int:
    return count_paths_to(get_nodes(input_path), "you", "out")


def day11_part2(input_path: str)->int:
    return count_paths_along(get_nodes(input_path), "svr", "out", frozenset({"dac", "fft"}))


if __name__ == '__main__':
    print("-----DAY 11----")
    print("Examples:")
    print(f'Part1: {day11_part1("inputs/day11_part1_test")}')
    print(f'Part2: {day11_part2("inputs/day11_part2_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day11_part1("inputs/day11")}')
    print(f'Part2: {day11_part2("inputs/day11")}')
