
def process_beam_rec(diagram: list[str], row:int, col: int)->int:
    if col < 0 or col > len(diagram[0]):
        return 0
    while row < len(diagram):
        if diagram[row][col] == '^':
            diagram[row] = diagram[row][:col] + 'X' + diagram[row][col + 1:]
            splits = 1
            splits += process_beam_rec(diagram, row, col-1)
            return splits + process_beam_rec(diagram, row, col+1)
        elif diagram[row][col] != '.':
            return 0
        else:
            diagram[row] = diagram[row][:col] + '|' + diagram[row][col + 1:]
        row += 1
    return 0
            
    
def day7_part1(input_path: str)->int:
    diagram: list[str] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        diagram = input_file.read().splitlines()
    
    start_col = diagram[0].index('S')    
    return process_beam_rec(diagram, 1, start_col)


def day7_part2(input_path: str)->int:
    diagram: list[str] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        diagram = input_file.read().splitlines()

    beam_counts = [0] * len(diagram[0])
    start_col = diagram[0].index('S')
    beam_cols: set = {start_col}
    beam_counts[start_col] = 1
    for row in diagram:
        for col in beam_cols.copy():
            if row[col] == '^':
                beam_cols.remove(col)
                beam_cols.add(col-1)
                beam_cols.add(col+1)
                beam_counts[col-1] += beam_counts[col]
                beam_counts[col+1] += beam_counts[col]
                beam_counts[col] = 0
        
    return sum(beam_counts)


if __name__ == '__main__':
    print("-----DAY 07----")
    print("Examples:")
    print(f'Part1: {day7_part1("inputs/day07_test")}')
    print(f'Part2: {day7_part2("inputs/day07_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day7_part1("inputs/day07")}')
    print(f'Part2: {day7_part2("inputs/day07")}')
