# Timothy Metzger
# Advent of Code 2021
# Day 11

def main():
    with open('inputs/day11.txt') as f:
        octopuses = []
        for line in f:
            octopuses.append(list(map(int,list(line.strip()))))

    # Part 1:
    # Octopuses increase in energy by 1 every step
    # When energy level is greater than 9 the octopus flashes
    # When the octopus flashes all adjacent octopuses have their energy increased by 1
    # If flashed during step the octopus resets to 0

    rows = len(octopuses)
    cols = len(octopuses[0])

    steps = 100
    n = 1
    flashes = 0

    while n:
        if all_flashed(octopuses):
            break

        step(octopuses)
        nines = get_nines(octopuses)

        flashed = []
        while nines:
            for nine in nines:
                flashed.append(nine)
                octopuses[nine[0]][nine[1]] = 0
                flashes += 1
                for neighbor_i,neighbor_j in get_neighbors(octopuses,nine):
                    if (neighbor_i,neighbor_j) not in flashed:
                        octopuses[neighbor_i][neighbor_j] += 1

            nines = get_nines(octopuses)



        n += 1

    print('Part 1: ', flashes)
    print('Part 2: ', n - 1)



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

    # Top Left
    if i - 1 >= 0 and j - 1 >= 0:
        neighbors.append((i-1,j-1))

    # Top Right
    if i - 1 >= 0 and j + 1 <= cols - 1:
        neighbors.append((i-1,j+1))

    # Bottom Left
    if i + 1  <= rows - 1 and j - 1 >= 0:
        neighbors.append((i+1,j-1))

    # Bottom Right
    if i + 1 <= rows - 1 and j + 1 <= cols - 1:
        neighbors.append((i+1,j+1))

    return neighbors

def get_nines(graph):
    nines = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] > 9:
                nines.append((i, j))
    return nines

def step(graph):
    nines = []
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            graph[i][j] += 1

def all_flashed(graph):
    for row in graph:
        for col in row:
            if col != 0:
                return False

    return True





if __name__ == "__main__":
    main()