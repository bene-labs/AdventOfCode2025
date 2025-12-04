adjacent_offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0),  (1, 0),
        (-1, 1), (0, 1), (1, 1),
]


def day4_part1(input_path: str)->int:
    accessible_roll_count = 0
    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        roll_map = input_file.read().splitlines()
    for y in range(len(roll_map)):
        for x in range(len(roll_map[y])):
            if not roll_map[y][x] == "@":
                continue
            filled_spaces = 0
            for x_offset, y_offset in adjacent_offsets:
                adjacent_x = x + x_offset
                adjacent_y = y + y_offset
                if adjacent_x < 0 or adjacent_x >= len(roll_map[y]) or adjacent_y < 0 or adjacent_y >= len(roll_map):
                    continue
                if roll_map[adjacent_y][adjacent_x] == "@":
                    filled_spaces += 1
                    if filled_spaces >= 4:
                        break
            else:
                accessible_roll_count += 1
    return accessible_roll_count

def day4_part2(input_path: str)->int:
    total_removals = 0
    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        roll_map = input_file.read().splitlines()

    while True:
        removals = 0
        new_map = roll_map.copy()
        for y in range(len(roll_map)):
            for x in range(len(roll_map[y])):
                if not roll_map[y][x] == "@":
                    continue
                filled_spaces = 0
                for x_offset, y_offset in adjacent_offsets:
                    adjacent_x = x + x_offset
                    adjacent_y = y + y_offset
                    if adjacent_x < 0 or adjacent_x >= len(roll_map[y]) or adjacent_y < 0 or adjacent_y >= len(roll_map):
                        continue
                    if roll_map[adjacent_y][adjacent_x] == "@":
                        filled_spaces += 1
                        if filled_spaces >= 4:
                            break
                else:
                    new_map[y] = new_map[y][:x] + "." + roll_map[y][x+1:]
                    removals += 1
        if removals == 0:
            break
        total_removals += removals
        roll_map = new_map
    return total_removals



if __name__ == '__main__':
    print("-----DAY 04----")
    print("Examples:")
    print(f'Part1: {day4_part1("inputs/day04_test")}')
    print(f'Part2: {day4_part2("inputs/day04_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day4_part1("inputs/day04")}')
    print(f'Part2: {day4_part2("inputs/day04")}')
