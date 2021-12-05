# Timothy Metzger
# Advent of Code 2021
# Day 5

def main():
    with open('inputs/day5.txt') as f:
        lines = [line.strip().split(" -> ") for line in f]

    vents = []
    for line in lines:
        vent = []
        for item in line:
            x, y = item.split(',')
            vent.append(int(x))
            vent.append(int(y))

        vents.append(vent)

    max_x = 0
    max_y = 0
    for vent in vents:
        if vent[0] > max_x:
            max_x = vent[0]
        if vent[2] > max_x:
            max_x = vent[2]

        if vent[1] > max_y:
            max_y = vent[1]
        if vent[3] > max_y:
            max_y = vent[3]

    ocean_floor = []
    for _ in range(max_y + 1):
        row = []
        for _ in range(max_x + 1):
            row.append(0)

        ocean_floor.append(row)

    for vent in vents:
        draw_lines(vent, ocean_floor, ignore_diagonals=False)

    # print("Part 1: ", points_of_danger(ocean_floor)) #5169
    print("Part 2: ", points_of_danger(ocean_floor))


def draw_lines(vent, ocean_floor, ignore_diagonals=True):
    x1, y1, x2, y2 = vent
    # Vertical case
    if x1 == x2:
        starting_point = min(y1, y2)
        end_point = max(y1, y2) + 1
        while starting_point < end_point:
            ocean_floor[starting_point][x1] += 1
            starting_point += 1
    # Horizontal case
    elif y1 == y2:
        starting_point = min(x1, x2)
        end_point = max(x1, x2) + 1
        while starting_point < end_point:
            ocean_floor[y1][starting_point] += 1
            starting_point += 1

    else:
        if not ignore_diagonals:

            # Always choosing the left most x
            current_x = min(x1, x2)
            end_x = max(x1, x2) + 1
            if current_x == x1:
                current_y = y1
                end_y = y2 + 1
            else:
                current_y = y2
                end_y = y1 + 1

            # Determine if moving up or down
            if end_y < current_y:
                add_y = -1
            else:
                add_y = 1

            while current_x < end_x:
                ocean_floor[current_y][current_x] += 1

                current_x += 1
                current_y += add_y


def points_of_danger(ocean_floor):
    dangerous_points = 0
    for row in ocean_floor:
        for point in row:
            if point >= 2:
                dangerous_points += 1

    return dangerous_points


if __name__ == "__main__":
    main()
