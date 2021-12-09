# Timothy Metzger
# Advent of Code 2021
# Day 9


from functools import reduce
def main():
    with open('inputs/day9.txt') as f:
        # I hate 1liners
        # breaking line into individual nums then mapping to int
        heights = [list(map(int, list(line.strip()))) for line in f]

    # Part 1:
    # risk_level = 1 + height

    rows = len(heights)
    cols = len(heights[0])
    low_points = []
    risk_level = 0
    for i in range(rows):
        for j in range(cols):
            dne = 0
            check = 0
            # Top
            if i - 1 >= 0:
                if heights[i - 1][j] > heights[i][j]:
                    check += 1
                else:
                    continue
            else:
                dne += 1

            # Right
            if j + 1 <= cols - 1:
                if heights[i][j + 1] > heights[i][j]:
                    check += 1
                else:
                    continue
            else:
                dne += 1

            # Bottom
            if i + 1 <= rows - 1:
                if heights[i + 1][j] > heights[i][j]:
                    check += 1
                else:
                    continue
            else:
                dne += 1

            # Left
            if j - 1 >= 0:
                if heights[i][j - 1] > heights[i][j]:
                    check += 1
                else:
                    continue
            else:
                dne += 1

            if 4 - dne == check:
                risk_level += 1 + heights[i][j]
                low_points.append((i, j))

    print('Part 1: ', risk_level)

    basin_size = []
    for low_point in low_points:
        basin_size.append(bfs(heights, low_point))

    big3 = sorted(basin_size,reverse=True)[:3]
    print("Part 2: ",reduce((lambda x,y : x*y),big3)) # Unnecessary big brain

def bfs(graph, start):
    start_i, start_j = start
    rows = len(graph)
    cols = len(graph[0])
    queue = []
    visited = []
    for i in range(rows):
        visited.append([False] * cols)

    visited[start_i][start_j] = True
    queue.append((start_i, start_j))
    basin = 1
    while queue:
        current_i, current_j = queue.pop(0)
        for neighbor_i, neighbor_j in get_neighbors(graph, (current_i, current_j)):
            print(neighbor_i,neighbor_j)
            if visited[neighbor_i][neighbor_j] is False:
                visited[neighbor_i][neighbor_j] = True
                queue.append((neighbor_i, neighbor_j))
                basin += 1
    return basin


def get_neighbors(graph, node):
    # Returns only the neighbors that exist and are not 9

    rows = len(graph)
    cols = len(graph[0])

    i, j = node

    neighbors = []
    # Top
    if i - 1 >= 0:
        if graph[i - 1][j] != 9:
            neighbors.append((i - 1, j))

    # Right
    if j + 1 <= cols - 1:
        if graph[i][j + 1] != 9:
            neighbors.append((i, j + 1))

    # Bottom
    if i + 1 <= rows - 1:
        if graph[i + 1][j] != 9:
            neighbors.append((i + 1, j))

    # Left
    if j - 1 >= 0:
        if graph[i][j - 1] != 9:
            neighbors.append((i, j - 1))

    return neighbors


if __name__ == "__main__":
    main()
