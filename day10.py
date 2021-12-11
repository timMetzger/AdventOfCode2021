# Timothy Metzger
# Advent of Code 2021
# Day 10


from statistics import median


def main():
    with open('inputs/day10.txt') as f:
        lines = [line.strip() for line in f]

    # Part 1:
    # A corrupt line is when the brackets don't match
    # A incomplete match is when there are not enough closing brackets

    valid_open = ['(', '[', '{', '<']
    close_count = {')': 0, ']': 0, '}': 0, '>': 0}

    syntax_values = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    incomplete_line_stack = []
    corrupt_lines = []

    for line in lines:
        stack = []
        corrupt = False
        for char in line:
            # Push opening brackets to stack
            if char in valid_open:
                stack.append(char)
                continue
            else:
                # Check if closing bracket matches opening
                if char == ')' and stack[-1] == '(':
                    stack.pop()
                    continue
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                    continue
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                    continue
                elif char == '>' and stack[-1] == '<':
                    stack.pop()
                    continue
                else:
                    # Corrupt line
                    close_count[char] += 1
                    corrupt = True
            break
        if corrupt:
            corrupt_lines.append(line)

        if stack != [] and not corrupt:
            # Incomplete line
            incomplete_line_stack.append(stack)

    part1_answer = 0
    for key, val in close_count.items():
        if val > 0:
            part1_answer += syntax_values[key] * val

    print('Part 1: ', part1_answer)

    # Part 2

    line_values = []
    for stack in incomplete_line_stack:
        to_add = ''
        stack = reversed(stack)
        for char in stack:
            if char == '(':
                to_add += ')'
            elif char == '[':
                to_add += ']'
            elif char == '{':
                to_add += '}'
            elif char == '<':
                to_add += '>'

        line_values.append(get_line_value(to_add))

    print('Part 2: ', median(sorted(line_values)))


def get_line_value(chars):
    point_table = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    score = 0
    for char in chars:
        score = score * 5 + point_table[char]

    return score


if __name__ == "__main__":
    main()
