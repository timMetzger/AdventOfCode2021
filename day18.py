# Timothy Metzger
# Advent of Code 2021
# Day 18

from math import floor, ceil


def main():
    with open("inputs/day18.txt") as f:
        snailfish_pairs = [line.strip() for line in f]

    total = []
    for snailfish in snailfish_pairs:
        total.append(snailfish)

    total = ",".join(total)
    total = "[" + total + "]"
    reduced_fish = reduce_fish(total)
    for char in reduced_fish:
        print(char, end="")


def explode(fish, i):
    left_num = None
    right_num = None
    pair = []
    stack = [fish[i - 1]]

    while stack:
        if fish[i] == '[':
            stack.append(fish[i])
        elif fish[i] == ']':
            stack.pop()

        if len(stack) >= 2 and fish[i + 1].isnumeric() and fish[i + 3].isnumeric():
            pair.extend([int(fish[i + 1]), int(fish[i + 3]), i])

            # Grab closest left number
            for j in range(len(fish[:i]), -1, -1):
                if fish[j].isnumeric():
                    left_num = [int(fish[j]), j]
                    break

            # Grab closest right number
            for j in range(i + 4, len(fish)):
                if fish[j].isnumeric() and is_regular_num(fish, j):
                    right_num = [int(fish[j]), j]
                    break

            break

        i += 1

    to_remove = []

    new_left = None
    new_right = None
    new_pair = [None, None]

    fish = list(fish)

    #
    if left_num is None:
        left_num = [0, None]
        new_right = pair[1] + right_num[0]

    elif right_num is None:
        right_num = [0, None]
        new_left = pair[0] + left_num[0]

    else:
        new_right = pair[1] + right_num[0]
        new_left = pair[0] + left_num[0]

    to_remove.extend([pair[2], pair[2] + 1, pair[2] + 2, pair[2] + 3, pair[2] + 4])

    new_fish = []
    for i, char in enumerate(fish):
        if i == pair[2]:
            new_fish.append(str(0))
        elif left_num[1] is not None and i == left_num[1]:
            new_fish.append(str(new_left))
        elif right_num[1] is not None and i == right_num[1]:
            new_fish.append(str(new_right))
        elif i not in to_remove:
            new_fish.append(str(char))

    return new_fish


def split_fish(fish, i):
    left_num = floor(int(fish[i]) / 2)
    right_num = ceil(int(fish[i]) / 2)
    new_pair = list(f'[{left_num},{right_num}]')
    fish = list(fish)

    new_fish = []
    for j in range(len(fish)):
        if j == i:
            for char in new_pair:
                new_fish.append(char)
        else:
            new_fish.append(fish[j])

    new_fish = [str(char) for char in new_fish]

    return new_fish


def is_regular_num(fish, i):
    stack = []
    current = 0
    stack.append(fish[current])
    in_pos = False

    while stack:
        if fish[i] == '[':
            stack.append(fish[i])
        elif fish[i] == ']':
            stack.pop()

        if current == i and len(stack) < 4:
            return True

        current += 1


def reduce_fish(fish):
    # TODO terminal state?
    for char in fish:
        print(char, end='')
    print()
    # Check exploding
    bracket_stack = []
    for i, char in enumerate(fish):
        if char == '[':
            bracket_stack.append(char)
        elif char == ']':
            bracket_stack.pop()
        elif len(bracket_stack) > 4 and char.isnumeric() and fish[i - 1] == '[':
            fish = explode(fish, i - 1)
            return reduce_fish(fish)


    # Check splitting
    for i, char in enumerate(fish):
        if char.isnumeric():
            if int(char) > 9:
                fish = split_fish(fish, i)
                return reduce_fish(fish)

    return fish



if __name__ == "__main__":
    main()
