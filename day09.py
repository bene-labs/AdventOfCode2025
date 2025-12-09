from math import dist


def day9_part1(input_path: str)->int:
    corner_coordinates : list[tuple[int]] = []
    with open(input_path, 'r', encoding='utf-8') as input_file:
        for coordinate in input_file.read().splitlines():
            corner_coordinates.append(tuple[int](int(pos) for pos in coordinate.split(',')))
    
    orig_point = (0, 0)
    corner_coordinates.sort(key=lambda cord: dist(orig_point, cord))
    biggest_rect_dimension = tuple(point2 - point1 + 1 for point1, point2 in zip(corner_coordinates[0], corner_coordinates[-1]))
    return biggest_rect_dimension[0] * biggest_rect_dimension[1]


if __name__ == '__main__':
    print("-----DAY 09----")
    print("Examples:")
    print(f'Part1: {day9_part1("inputs/day09_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day9_part1("inputs/day09")}')
