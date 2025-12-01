def day1(path: str, count_all_zeros: bool)->int:
    zero_count = 0

    with open(path, 'r', encoding='utf-8-sig') as input_file:
        dial = 50
        for instruction in input_file.read().splitlines():
            direction = instruction[0]
            amount = int(instruction[1:])
            if direction == 'L':
                dial -= amount
                while dial < 0:
                    dial = 100 - abs(dial)
                    if count_all_zeros:
                        zero_count += 1
            else:
                dial += amount
                while dial >= 100:
                    dial = dial - 100
                    if count_all_zeros:
                        zero_count += 1
            if not count_all_zeros and dial == 0:
                zero_count += 1
    return zero_count

if __name__ == '__main__':
    print("Examples:")
    print(f'Part1: {day1("inputs/day01_test", False)}')
    print(f'Part2: {day1("inputs/day01_test", True)}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day1("inputs/day01", False)}')
    print(f'Part2: {day1("inputs/day01", True)}')
