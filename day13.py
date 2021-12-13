# Timothy Metzger
# Advent of Code 2021
# Day 13
from itertools import zip_longest

def main():
    with open('inputs/day13.txt') as f:
        dots = []
        folds = []
        for line in f:
            if line.startswith('fold'):
                folds.append(line.strip().split(' ')[-1].split("="))
            else:
                if line != '\n':
                    dots.append(list(map(int,line.strip().split(','))))

    # Create grid
    max_x = 0
    max_y = 0
    for dot in dots:
        if dot[0] > max_x:
            max_x = dot[0]

        if dot[1] > max_y:
            max_y = dot[1]

    grid = []
    for _ in range(max_y + 1):
        row = []
        for _ in range(max_x + 1):
            row.append(0)
        grid.append(row)

    for dot in dots:
        grid[dot[1]][dot[0]] = 1

    # Folding
    # Horizontal folds = bottom comes up -- x value stays the same, y changes
    # Vertical folds = right comes left -- y value stays the same, x changes
    # Fold deletes the row at that position
    n = 0
    for direction, position in folds:
        position = int(position)
        new_grid = []



        # Horizontal fold
        if direction == 'y':
            top = grid[:position]
            bottom = grid[position+1:]



            for top_row, bottom_row in zip_longest(top,reversed(bottom)):
                row = []
                if top_row is None:
                    top_row = [0] * len(bottom_row)
                elif bottom_row is None:
                    bottom_row = [0] * len(top_row)


                for val1,val2 in zip(top_row,bottom_row):
                    if val1 or val2 == 1:
                        row.append(1)
                    else:
                        row.append(0)

                new_grid.append(row)
            grid = new_grid

        # Vertical fold
        else:
            left = []
            right = []
            for row in grid:
                left.append(row[:position])
                right.append(reversed(row[position+1:]))

            for left_row, right_row in zip_longest(left, right):
                row = []
                if left_row is None:
                    left_row = [0] * len(right_row)
                elif right_row is None:
                    right_row = [0] * len(left_row)

                for val1, val2 in zip(left_row, right_row):
                    if val1 or val2 == 1:
                        row.append(1)
                    else:
                        row.append(0)
                new_grid.append(row)

            grid = new_grid


        if n == 0:
            print('Part 1: ',count_dots(grid))

        n += 1


    for row in grid:
        for val in row:
            if val == 1:
                print('#',end=" ")
            else:
                print(' ',end=" ")
        print()


def count_dots(grid):
    count = 0
    for row in grid:
        for val in row:
            if val:
                count += 1

    return count







if __name__ == "__main__":
    main()