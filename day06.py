
def day6_part1(input_path: str)->int:
    total_sum = 0
    problems = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        problems = [problem.split() for problem in input_file.read().splitlines()]

    for column in range(len(problems[0])):
        problem_res = 0
        is_mult = problems[-1][column] == '*'
        for row in range(len(problems) -1):
            if row == 0:
                problem_res = int(problems[row][column])
            elif is_mult:
                problem_res *= int(problems[row][column])
            else:
                problem_res += int(problems[row][column])
        total_sum += problem_res
    return total_sum


def day6_part2(input_path: str)->int:
    total_sum = 0
    problems = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        problem_input = input_file.read().splitlines()
        problems = []
        offset = 0
        for col in range(1, len(problem_input[0])-1, 1):
            if all([row[col] == " " for row in problem_input]):
                problems.append([row[offset:col] for row in problem_input])
                offset = col+1
                continue
        problems.append([row[offset:] for row in problem_input])
    
    for row in range(len(problems)):
        problem_res = 0
        is_mult = problems[row][-1][0] == '*'
        num_len = len(problems[row][0])
        for num_col in range(num_len - 1, -1, -1):
            num = ""
            for column in range(len(problems[row]) -1):
                num += problems[row][column][num_col]
            if num_col == num_len - 1:
                problem_res = int(num)
            elif is_mult:
                problem_res *= int(num)
            else:
                problem_res += int(num)
        total_sum += problem_res
    return total_sum


if __name__ == '__main__':
    print("-----DAY 06----")
    print("Examples:")
    print(f'Part1: {day6_part1("inputs/day06_test")}')
    print(f'Part2: {day6_part2("inputs/day06_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day6_part1("inputs/day06")}')
    print(f'Part2: {day6_part2("inputs/day06")}')
