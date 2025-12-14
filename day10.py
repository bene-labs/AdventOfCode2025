import pulp

MAX_DEPTH = 10


def find_shortest_button_path_rec( target_value: int, switches: list[int],  solutions: set[int], reached_values: list[int] = [],
                                   current_value: int = 0, current_switch: int | None = None, depth: int = 0, ):
    if depth >= MAX_DEPTH:
        return
    if solutions and depth >= min(solutions):
        return
    if current_switch:
        next_value = current_value ^ current_switch
        if next_value == target_value:
            #print(f"{depth}", end=", ")
            solutions.add(depth)
            return
        if next_value in reached_values:            
            return
    else:
        next_value = current_value
    
    for switch in switches:
        find_shortest_button_path_rec(target_value, switches, solutions, reached_values + [next_value], next_value, switch, depth + 1)
    return


def get_target_nummer(target_str: str)->int:
    target_nummer = 0
    for i in range(len(target_str)):
        if target_str[i] == '#':
            target_nummer += 2**i
    return target_nummer


def get_switches(switches_str: str)->list[int]:
    switches = []
    for switch_str in switches_str.strip().split(' '):
        switches.append(
            sum([2**int(switch) for switch in switch_str[1:-1].split(',')]))
    return switches

def get_target_joltage(joltages_str: str)->int:
    target_joltage = 0
    for i, joltage_str in enumerate(joltages_str[1:-1].split(',')):
        target_joltage += (2 ** i) * int(joltage_str)
    return target_joltage
    

def day10_part1(input_path: str)->int:
    required_button_presses = 0

    instructions = open(input_path, "r", encoding="utf-8").read().splitlines()
    for i, instruction in enumerate(instructions):
        target_end_idx = instruction.find(']')
        target_str = instruction[1:target_end_idx]
        switches_str = instruction[target_end_idx + 1:instruction.find('{')]

        solutions = set()
        find_shortest_button_path_rec(get_target_nummer(target_str), get_switches(switches_str), solutions)
        required_button_presses += min(solutions)
   
    return required_button_presses

def get_decimal_switches( switches_str: str)->list[int]:
    switches = []
    
    for switch_str in switches_str.strip().split(' '):
        switches.append([int(value) for value in switch_str[1:-1].split(',')])
    return switches

def get_problem(target_joltages : list[int],  switches: list):

    problem = pulp.LpProblem(sense=pulp.LpMinimize)

    x = [pulp.LpVariable(f"x{i}", lowBound=0, cat="Integer") for i in range(len(switches))]
    problem += pulp.lpSum(x)

    for i in range(len(target_joltages)):
        problem += pulp.lpSum(y for j, y in enumerate(x) if i in switches[j] ) == target_joltages[i]
    
    return problem


def day10_part2(input_path: str) -> int:
    required_button_presses = 0
    instructions = open(input_path, "r", encoding="utf-8").read().splitlines()
    for i, instruction in enumerate(instructions):
        joltage_start_idx = instruction.find('{')
        target_joltage_str = instruction[joltage_start_idx+1:-1]
        
        switches = get_decimal_switches(instruction[instruction.find(']') + 1:joltage_start_idx])
        target_joltages = [int(target) for target in target_joltage_str.split(',')]
        problem = get_problem(target_joltages, switches)
        
        problem.solve(pulp.PULP_CBC_CMD(msg=False))
        required_button_presses += int(pulp.value(problem.objective))

    return required_button_presses


if __name__ == '__main__':
    print("-----DAY 10-----")
    print("Examples:")
    print(f'Part1: {day10_part1("inputs/day10_test")}')
    print(f'Part2: {day10_part2("inputs/day10_test")}')
    print('----')
    print("Solutions:")
    # print(f'Part1: {day10_part1("inputs/day10")}')
    print(f'Part2: {day10_part2("inputs/day10")}')
