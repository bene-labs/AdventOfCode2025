from math import dist
from itertools import combinations


class Connection:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2
        self.distance = dist(p1, p2)


def day8_part1(input_path: str, max_connections: int = 1000)->int:
    box_coordinates : list[tuple[int] | str] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        box_coordinates = input_file.read().splitlines()
        for i in range(len(box_coordinates)):
            box_coordinates[i] = tuple(int(pos) for pos in box_coordinates[i].split(','))
    
    connections : list[Connection] = []
    for coord1, coord2 in combinations(box_coordinates, 2):
        if coord1 == coord2:
            continue
        connections.append(Connection(coord1, coord2))
    connections.sort(key=lambda c: c.distance)
    connections = connections[:max_connections]
    
    circuits: list[set]  = []
    for p1, p2 in [(connection.point1, connection.point2) for connection in connections]:
        connected_circuits_indices = set()
        for idx, circuit in enumerate(circuits):
            if p1 in circuit:
                circuit.add(p1)
                connected_circuits_indices.add(idx)
            if p2 in circuit:
                circuit.add(p2)
                connected_circuits_indices.add(idx)
        match len(connected_circuits_indices):
            case 0:
                circuits.append({p1, p2})
            case 1:
                idx = next(iter(connected_circuits_indices))
                circuits[idx].add(p1)
                circuits[idx].add(p2)
            case _:
                circuit_it = iter(connected_circuits_indices)
                merge_into_idx = next(circuit_it)
                for other_circuit_idx in circuit_it:
                    circuits[merge_into_idx] = circuits[merge_into_idx] | circuits[other_circuit_idx]
                    del circuits[other_circuit_idx]
    circuits.sort(key=lambda c:len(c), reverse=True)
    
    result = 1
    for i in range(3):
        result *= len(circuits[i])
    return result


def day8_part2(input_path: str) -> int:
    box_coordinates: list[tuple[int]] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        for coordinate in input_file.read().splitlines():
            box_coordinates.append(tuple[int](int(pos) for pos in coordinate.split(',')))

    connections: list[Connection] = []
    unique_box_coordinates = set(box_coordinates)
    for coord1, coord2 in combinations(box_coordinates, 2):
        if coord1 == coord2:
            continue
        connections.append(Connection(coord1, coord2))
    connections.sort(key=lambda c: c.distance)

    circuits: list[set] = []
    for p1, p2 in [(connection.point1, connection.point2) for connection in connections]:
        connected_circuits_indices = set()
        for idx, circuit in enumerate(circuits):
            if p1 in circuit:
                circuit.add(p1)
                connected_circuits_indices.add(idx)
            if p2 in circuit:
                circuit.add(p2)
                connected_circuits_indices.add(idx)
        match len(connected_circuits_indices):
            case 0:
                circuits.append({p1, p2})
                continue
            case 1:
                idx = next(iter(connected_circuits_indices))
                circuits[idx].add(p1)
                circuits[idx].add(p2)
            case _:
                circuit_it = iter(connected_circuits_indices)
                merge_into_idx = next(circuit_it)
                for other_circuit_idx in circuit_it:
                    circuits[merge_into_idx] = circuits[merge_into_idx] | circuits[other_circuit_idx]
                    del circuits[other_circuit_idx]
        if len(circuits) == 1 and circuits[0] == unique_box_coordinates:
            return p1[0] * p2[0]
    return -1


if __name__ == '__main__':
    print("-----DAY 08----")
    print("Examples:")
    print(f'Part1: {day8_part1("inputs/day08_test", 10)}')
    print(f'Part2: {day8_part2("inputs/day08_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day8_part1("inputs/day08")}')
    print(f'Part2: {day8_part2("inputs/day08")}')
