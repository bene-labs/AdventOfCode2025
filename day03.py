
def day3(input_path: str, size: int)->int:
    total_voltage = 0

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        for voltages in input_file.read().splitlines():
            volt_sequence: str = ""
            for offset in range(size-1, -1, -1):
                available_voltage = voltages[:-offset] if offset > 0 else voltages
                index_biggest = max(range(len(available_voltage)), key=available_voltage.__getitem__)
                volt_sequence += voltages[index_biggest]
                voltages = voltages[index_biggest+1:]
            total_voltage += int(volt_sequence)

    return total_voltage


if __name__ == '__main__':
    print("-----DAY 03----")
    print("Examples:")
    print(f'Part1: {day3("inputs/day03_test", 2)}')
    print(f'Part2: {day3("inputs/day03_test", 12)}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day3("inputs/day03", 2)}')
    print(f'Part2: {day3("inputs/day03", 12)}')
