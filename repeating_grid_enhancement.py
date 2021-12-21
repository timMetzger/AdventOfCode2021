# Timothy Metzger
# Advent of Code 2021
# Day 20

def main():
    with open('inputs/day20.txt') as f:
        alg = list(f.readline().strip())
        f.readline()
        image = [list(line.strip()) for line in f]

    # Part 1:
    # Image expands out infinitely filled with dark pixels
    # . -> 0
    # # -> 1

    for _ in range(2):
        image = enhance(image,alg)

    lit_pixels = 0
    for row in image:
        for col in row:
            if col == '#':
                lit_pixels += 1

    print("Part 1:",lit_pixels)



def enhance(image,alg):

    rows = len(image)
    cols = len(image[0])

    enhancements = []
    for i in range(rows):

        enhance_row = []
        for j in range(cols):
            enhance_row.append(decode(image, alg, i, j, rows, cols))
        enhancements.append(enhance_row)

    output_image = []
    for i in range(rows):
        output_image_row = []
        for j in range(cols):
            output_image_row.append(enhancements[i][j])
        output_image.append(output_image_row)

    return output_image

def decode(image, alg, i, j, rows, cols,state):
    # Get neighbors
    # Top row
    # ************
    block = []

    # Top left
    if i - 1 >= 0 and j - 1 >= 0:
        block.append(image[i - 1][j-1])
    else:
        if i - 1 < 0:
            if j - 1 < 0:
                block.append(image[rows-1][cols-1])
            else:
                block.append(image[rows-1][j-1])
        else:
            block.append(image[i-1][cols-1])

    # Top
    if i - 1 >= 0:
        block.append(image[i - 1][j])
    else:
        block.append(image[rows-1][j])

    # Top right
    if i - 1 >= 0 and j + 1 <= cols - 1:
        block.append(image[i - 1][j + 1])
    else:
        if i - 1 < 0:
            if j + 1 > cols - 1:
                block.append(image[rows-1][0])
            else:
                block.append(image[rows-1][j+1])
        else:
            block.append(image[i-1][0])


    # Middle row
    # **********

    # Left
    if j - 1 >= 0:
        block.append(image[i][j - 1])
    else:
        block.append(image[i][cols-1])

    # Middle
    block.append(image[i][j])

    # Right
    if j + 1 <= cols - 1:
        block.append(image[i][j + 1])
    else:
        block.append(image[i][0])

    # Bottom
    # ***********

    # Bottom left
    if i + 1 <= rows - 1 and j - 1 >= 0:
        block.append(image[i + 1][j - 1])
    else:
        if i + 1 > rows - 1:
            if j - 1 < 0:
                block.append(image[0][cols-1])
            else:
                block.append(image[0][j-1])
        else:
            block.append(image[i+1][cols-1])

    # Bottom
    if i + 1 <= rows - 1:
        block.append(image[i + 1][j])
    else:
        block.append(image[0][j])

    # Bottom right
    if i + 1 <= rows - 1 and j + 1 <= cols - 1:
        block.append(image[i + 1][j + 1])
    else:
        if i + 1 > rows - 1:
            if j + 1 > cols - 1:
                block.append(image[0][0])
            else:
                block.append(image[0][j+1])
        else:
            block.append(image[i+1][0])

    code = ''

    for char in block:
        if char == '.':
            code += '0'
        else:
            code += '1'


    return alg[int(code,2)]


if __name__ == "__main__":
    main()
