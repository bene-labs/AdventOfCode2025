class FreshRange:
    def __init__(self, values: list[str]):
        self.min = int(values[0])
        self.max = int(values[1])
        self.valid = True

    def adjust_for_overlaps(self, other_ranges: list):
        for other in other_ranges:
            if other.min <= self.min <= other.max:
                self.min = other.max + 1
                if self.min > self.max:
                    self.valid = False
                    break
            if other.min <= self.max <= other.max:
                self.max = other.min - 1
                if self.max < self.min:
                    self.valid = False
                    break

    def is_in_range(self, nb: int):
        return self.min <= nb <= self.max

    def get_length(self):
        return (self.max - self.min + 1) if self.valid else 0


def day5_part1(input_path: str)->int:
    fresh_ingredient_count: int = 0
    fresh_ranges: list[FreshRange] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        range_input, id_input = input_file.read().split("\n\n")
    for range_str in range_input.splitlines():
        fresh_ranges.append(FreshRange(range_str.split('-')))
    ingredient_ids = [int(ingredient_id) for ingredient_id in id_input.splitlines()]

    for ingredient_id in ingredient_ids:
        for fresh_range in fresh_ranges:
            if fresh_range.is_in_range(ingredient_id):
                fresh_ingredient_count += 1
                break
    return fresh_ingredient_count


def day5_part2(input_path: str)->int:
    total_fresh_ingredients : int = 0
    fresh_ranges: list[FreshRange] = []

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        range_input, id_input = input_file.read().split("\n\n")
    for range_str in range_input.splitlines():
        fresh_ranges.append(FreshRange(range_str.split('-')))
    for i in range(len(fresh_ranges)):
        fresh_ranges[i].adjust_for_overlaps(fresh_ranges[:i] + fresh_ranges[i+1:])



    for fresh_range in fresh_ranges:
        total_fresh_ingredients += fresh_range.get_length()

    return total_fresh_ingredients



if __name__ == '__main__':
    print("-----DAY 05----")
    print("Examples:")
    print(f'Part1: {day5_part1("inputs/day05_test")}')
    print(f'Part2: {day5_part2("inputs/day05_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day5_part1("inputs/day05")}')
    print(f'Part2: {day5_part2("inputs/day05")}')
