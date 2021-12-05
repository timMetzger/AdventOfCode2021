# Timothy Metzger
# Advent of Code 2021
# Day 3


def main():
    with open("inputs/day3.txt") as f:
        diagnostics = []
        for line in f:
            report = []
            for num in line.strip():
                report.append(int(num))

            diagnostics.append(report)

    rows = len(diagnostics)
    cols = len(diagnostics[0])

    gamma = ""
    epsilon = ""

    # Goes through column by column
    # If bit is a zero subtract and if positive add to count
    # Final count determines the bits of gamma and epsilon
    for col in range(cols):
        count = 0
        for row in range(rows):

            if diagnostics[row][col] == 1:
                count += 1
            else:
                count -= 1

        if count > 0:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    part1_answer = int(gamma, 2) * int(epsilon, 2)
    print("Part 1: ", part1_answer)

    oxygen = find_rating(diagnostics, 'oxygen', 0)
    co2 = find_rating(diagnostics, 'co2', 0)

    oxygen_rating = ""
    co2_rating = ""
    for num in oxygen:
        for bit in num:
            oxygen_rating += str(bit)

    for num in co2:
        for bit in num:
            co2_rating += str(bit)

    part2_answer = int(oxygen_rating, 2) * int(co2_rating, 2)

    print("Part 2: ", part2_answer)


def find_rating(ratings, rating_type, index):
    if len(ratings) == 1:
        return ratings

    count = 0
    if rating_type == 'oxygen':
        for row in ratings:
            if row[index] > 0:
                count += 1
            else:
                count -= 1

        if count >= 0:
            ratings = [row for row in ratings if row[index] == 1]
        else:
            ratings = [row for row in ratings if row[index] == 0]

        return find_rating(ratings, rating_type, index + 1)

    elif rating_type == 'co2':
        for row in ratings:
            if row[index] > 0:
                count += 1
            else:
                count -= 1

        if count >= 0:
            ratings = [row for row in ratings if row[index] == 0]
        else:
            ratings = [row for row in ratings if row[index] == 1]

        return find_rating(ratings, rating_type, index + 1)


if __name__ == "__main__":
    main()
