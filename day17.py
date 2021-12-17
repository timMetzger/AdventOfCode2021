# Timothy Metzger
# Advent of Code 2021
# Day 17

from copy import copy


def main():
    with open('inputs/day17.txt') as f:
        line = f.readline().split(": ")[1:]

    line = line[0].split(", ")
    x_bounds = list(map(int, line[0].replace("x=", "").split("..")))
    y_bounds = list(map(int, line[1].replace("y=", "").split("..")))

    x0, y0 = 0, 0

    # x will be column
    # y will be row

    valid_launch = []
    count = 0
    for x in range(0,500):
        for y in range(-200,1000):
            xdot0, ydot0 = x, y
            xdot,ydot = copy(x), copy(y)
            current_x, current_y = 0, 0
            max_height = 0
            while current_x < 155 and current_y > -102:
                current_x += xdot
                current_y += ydot

                if xdot > 0:
                    xdot -= 1

                ydot -= 1

                if ydot == 0:
                    max_height = copy(current_y)


                if 135 <= current_x <= 155 and -102 <= current_y <= -78:
                    valid_launch.append((xdot0, ydot0, max_height))

    print(len(set(valid_launch)))

if __name__ == "__main__":
    main()
