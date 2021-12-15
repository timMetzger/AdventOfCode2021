# Timothy Metzger
# Advent of Code 2021
# Day 15

def main():
    with open('inputs/day15.txt') as f:
        cavern = [list(map(int, list(line.strip()))) for line in f]

    start = (0, 0)
    end = (len(cavern) - 1, len(cavern[0]) - 1)

    # Part 1
    # print('Part 1: ',a_star(cavern, start, end)[0] - cavern[0][0])

    # Part 2:
    # Cavern is actually 5 times as large
    # Going to try the naive approach first but its probably a bad idea

    expanded_rows = []
    for row in cavern:
        expanded_rows.append([item + 1 if item != 9 else 1 for item in row])

    row_length = len(cavern)

    # Duplicate bottom cell to the right four times adding 1 to each element
    current = 0
    for _ in range(4):
        for row in expanded_rows:
            row.extend([item + 1 if item != 9 else 1 for item in row[current:]])
        current += row_length

    current = 0
    for _ in range(3):
        for row in expanded_rows[current:current + row_length]:
            new_row = [item + 1 if item != 9 else 1 for item in row]
            expanded_rows.append(new_row)
        current += row_length

    # Add to right of first block
    for starting_row, extension in zip(cavern, expanded_rows):
        starting_row.extend(extension[:row_length * 4])

    # Add blocks below
    for row in expanded_rows:
        cavern.append(row)

    end = (len(cavern) - 1, len(cavern[0]) - 1)

    print('Part 2: ', a_star(cavern, start, end)[0] - cavern[0][0])


def a_star(graph, start, end):
    open_set = {start}

    path = {}
    g_scores = {}
    f_scores = {}
    for i in range(len(graph)):
        for j in range(len(graph)):
            g_scores[(i, j)] = float('inf')
            f_scores[(i, j)] = float('inf')

    g_scores[start] = 0
    f_scores[start] = manhattan_distance(start, end)
    while open_set:
        # (i,j) with lowest f_score
        current_value = float('inf')
        for key in open_set:
            if f_scores[key] < current_value:
                current = key
                current_value = f_scores[current]

        if current == end:
            return build_path(graph, path, current)

        open_set.remove(current)

        for neighbor in get_neighbors(graph, current):
            temp_g_score = g_scores[current] + graph[current[0]][current[1]]
            if temp_g_score < g_scores[neighbor]:
                path[neighbor] = current
                g_scores[neighbor] = temp_g_score
                f_scores[neighbor] = temp_g_score + manhattan_distance(neighbor, end)

                if neighbor not in open_set:
                    open_set.add(neighbor)

    return "Failure"


def build_path(graph, path, current):
    retraced_path = [current]
    while current in path.keys():
        current = path[current]
        retraced_path.append(current)

    risk_level = 0
    for pos in retraced_path:
        risk_level += graph[pos[0]][pos[1]]

    return (risk_level, retraced_path)


def get_neighbors(graph, node):
    rows = len(graph)
    cols = len(graph[0])

    i, j = node

    neighbors = []
    # Top
    if i - 1 >= 0:
        neighbors.append((i - 1, j))

    # Right
    if j + 1 <= cols - 1:
        neighbors.append((i, j + 1))

    # Bottom
    if i + 1 <= rows - 1:
        neighbors.append((i + 1, j))

    # Left
    if j - 1 >= 0:
        neighbors.append((i, j - 1))

    return neighbors


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


if __name__ == "__main__":
    main()
