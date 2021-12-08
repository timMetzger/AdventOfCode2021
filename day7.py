# Timothy Metzger
# Advent of Code 2021
# Day 7
from statistics import median, mean


def main():
    with open('inputs/day7.txt') as f:
        crabs = list(map(int, f.readline().strip().split(",")))

    alignment_location_1 = int(median(crabs))
    alignment_location_2 = int(mean(crabs))

    fuel_cost_1 = 0
    for crab in crabs:
        if crab != alignment_location_1:
            fuel_cost_1 += abs(crab - alignment_location_1)

    print("Part 1: ", fuel_cost_1)

    fuel_cost_2 = 0
    for crab in crabs:
        if crab != alignment_location_2:
            #This was my solution
            fuel = 0
            n = 1
            if crab < alignment_location_2:
                while crab < alignment_location_2:
                    crab += 1
                    fuel += n
                    n += 1
            else:
                while crab > alignment_location_2:
                    crab -= 1
                    fuel += n
                    n += 1

            fuel_cost_2 += fuel

            # This is the much simpler solution than using while loops
            # distance = abs(crab-alignment_location_2)
            # fuel_cost_2 += sum(range(0,distance+1))


    print("Part 2: ", fuel_cost_2)


if __name__ == "__main__":
    main()
