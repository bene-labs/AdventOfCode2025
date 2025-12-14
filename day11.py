
class Node:
    def __init__(self, connected: list, name: str):
        self.connected = connected
        self.id = name
    
    def count_path_to_rec(self, to: str, visited = [])->int:
        if self.id == to:
            return 1
        if self.id in visited:
            return 0
        path_count = 0
        for node in self.connected:
            path_count += node.count_path_to_rec(to, visited + [self.id])
        return path_count


def day11_part1(input_path: str)->int:
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
                unique_nodes[name].connected += connected_nodes
            else:
                unique_nodes[name] = Node(connected_nodes, name)
    return unique_nodes["you"].count_path_to_rec("out")

def day11_part2(input_path: str)->int:
    return 0


if __name__ == '__main__':
    print("-----DAY 11----")
    print("Examples:")
    print(f'Part1: {day11_part1("inputs/day11_test")}')
    # print(f'Part2: {day10_part2("inputs/day10_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day11_part1("inputs/day11")}')
    # print(f'Part2: {day10_part2("inputs/day10")}')
