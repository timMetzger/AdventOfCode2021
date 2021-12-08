# Timothy Metzger
# Advent of Code 2021
# Day 8


# Part 1:
# To render digits need unique segments
# Digit -> Number of Segments
# 1 -> 2
# 7 -> 3
# 4 -> 4
# 8 -> 7

# Part 2:
# The numbers identified in the out output also indicate which wires need to be on to produce that digit
# ie. dab -> 8 so wires d, a, and b need to be on
# sudoku ?



def main():
    signals = []
    outputs = []
    with open('inputs/day8.txt') as f:
        for line in f:
            line = line.strip().split(" | ")
            signals.append(line[0].split(" "))
            outputs.append(line[1].split(" "))

    codes = [2,3,4,7]



    part1_count = 0
    for output in outputs:
        for code in output:
            if len(code) in codes:
                part1_count += 1

    print("Part 1: ",part1_count)


    group_chart = {5:[2,3,5],6:[0,6,9]}
    code_chart = {2: 1, 3: 7, 4: 4, 7: 8}


    marked_positions = [False] * 7
    part2_count = 0
    for signal, output in zip(signals,outputs):
        part2_dict = {0: '', 1: '', 2: '', 3: '', 4: '', 5: '', 6: '', 7: '', 8: '', 9: ''}
        queue = []
        for signal_part in signal:
            if len(signal_part) in codes:
                part2_dict[code_chart[len(signal_part)]] = signal_part

            else:
                queue.append(signal_part)

        for code in queue:

            if len(code) == 5:
                # grouping = [2,3,5]
                if set(part2_dict[7]).issubset(set(code)):
                    part2_dict[3] = code
                else:
                    if len(set(code).intersection(set(part2_dict[4]))) == 3:
                        part2_dict[5] = code
                    else:
                        part2_dict[2] = code

            else:
                # grouping = [0,6,9]
                if set(part2_dict[4]).issubset(set(code)):
                    part2_dict[9] = code

                else:
                    if set(part2_dict[7]).issubset(set(code)):
                        part2_dict[0] = code

                    else:
                        part2_dict[6] = code

        output_value = ""

        for signal_output in output:
            signal_output = set(signal_output)
            for key,val in part2_dict.items():
                if set(val) == signal_output:
                    output_value += str(key)

        part2_count += int(output_value)


    print("Part 2: ", part2_count)


if __name__ == "__main__":
    main()