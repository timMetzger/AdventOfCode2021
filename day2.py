# Timothy Metzger
# Advent of Code 2021
# Day 2

def main():
    with open('inputs/day2.txt') as f:
        movements = [line for line in f]

    # Part 1

    # up decrease depth and vice versa
    x = 0
    y = 0
    for line in movements:
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == 'forward':
            x += distance
        elif direction == 'up':
            y -= distance
        elif direction == 'down':
            y += distance

        else:
            print("wtf")

    print("Part 1: ", x * y)

    # Part 2

    x = 0
    y = 0
    aim = 0

    for line in movements:
        direction, distance = line.split(" ")
        distance = int(distance)
        if direction == "up":
            aim -= distance

        elif direction == 'down':
            aim += distance

        elif direction == "forward":
            x += distance
            y += distance * aim

    print("Part 2: ", x * y)


if __name__ == "__main__":
    main()
