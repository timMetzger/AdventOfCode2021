# Timothy Metzger
# Advent of Code 2021
# Day 1

def main():
    with open("inputs/day1.txt") as f:
        depths = [int(x) for x in f]

    # Part 1
    count = 0
    prev = depths[0]

    for depth in depths[1:]:
        if depth > prev:
            count += 1

        prev = depth

    print("Part 1: ", count)


    # Part 2

    count = 0

    for i in range(len(depths)):
        try:
            prev_window = sum(depths[i:i+3])
            next_window = sum(depths[i+1:i+4])
            if next_window > prev_window:
                count += 1
        except IndexError:
            break

    print("Part 2: ", count)


if __name__ == "__main__":
    main()