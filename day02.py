
def day2_part1(input_path: str)->int:
    invalid_ids_sum = 0

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        for id_range in input_file.read().split(','):
            start, stop = id_range.split('-')
            for gift_id in range(int(start), int(stop)+1, 1):
                gift_id_str = str(gift_id)
                id_len = len(gift_id_str)
                if id_len % 2 != 0:
                    continue
                if gift_id_str[0:id_len//2] == gift_id_str[id_len//2:]:
                    invalid_ids_sum += gift_id
    return invalid_ids_sum


def day2_part2(input_path: str)->int:
    invalid_ids_sum = 0

    with open(input_path, 'r', encoding='utf-8-sig') as input_file:
        for id_range in input_file.read().split(','):
            start, stop = id_range.split('-')
            for gift_id in range(int(start), int(stop)+1, 1):
                gift_id_str = str(gift_id)
                id_len = len(gift_id_str)
                for sequence_len in range(1, id_len//2 + 1, 1):
                    if id_len % sequence_len != 0:
                        continue
                    sequences = [gift_id_str[i:i+sequence_len] for i in range(0, id_len, sequence_len)]
                    sequence_iterator = iter(sequences)
                    first_sequence = next(sequence_iterator)
                    if all(seq == first_sequence for seq in sequence_iterator):
                        invalid_ids_sum += gift_id
                        break
    return invalid_ids_sum


if __name__ == '__main__':
    print("-----DAY 02----")
    print("Examples:")
    print(f'Part1: {day2_part1("inputs/day02_test")}')
    print(f'Part2: {day2_part2("inputs/day02_test")}')
    print('----')
    print("Solutions:")
    print(f'Part1: {day2_part1("inputs/day02")}')
    print(f'Part2: {day2_part2("inputs/day02")}')
