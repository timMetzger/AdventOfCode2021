# Timothy Metzger
# Advent of Code 2021
# Day 12

def main():
    with open('inputs/day12.txt') as f:
        connections = [line.strip().split("-") for line in f]

    adj_list = {}
    small_caves = {}

    for connection in connections:
        point1 = connection[0]
        point2 = connection[1]



        if point1.islower():
            small_caves[point1] = False
        if point2.islower():
            small_caves[point2] = False

        if point1 in adj_list.keys():
            if point2 not in adj_list[point1]:
                adj_list[point1].append(point2)
        else:
            if point2 != 'start':
                adj_list[point1] = [point2]

        if point2 in adj_list.keys():
            if point1 not in adj_list[point2]:
                adj_list[point2].append(point1)
        else:
            if point1 != 'start':
                adj_list[point2] = [point1]

    # Part 1:
    # Find all paths that get from start to end
    # May only visit a small cave once (small caves are lowercase)
    # Basically this is the british museum algorithm with the above constraint

    paths = get_paths(adj_list, small_caves, 'start', 'end')
    # print("Part 1: ",len(paths))

    # Part 2:
    # Now one small cave may be visited twice
    part2_answer = []
    for path in paths:
        if path not in part2_answer and path is not None:
            part2_answer.append(path)
            print(path)

    print(len(part2_answer))



def dfs(adj_list, small_caves, node, destination, path,paths,special_cave):
    if node in small_caves.keys():
        if node == special_cave:
            small_caves[node] += 1
        else:
            small_caves[node] = True

    path.append(node)

    if node == destination:
        paths.append(path[:])
    else:
        for neighbor in adj_list[node]:
            if neighbor in small_caves.keys():
                if neighbor == special_cave and small_caves[neighbor] < 2:
                    dfs(adj_list, small_caves, neighbor, destination, path, paths,special_cave)
                elif small_caves[neighbor] is False:
                    dfs(adj_list,small_caves,neighbor,destination,path,paths,special_cave)
            else:
                dfs(adj_list,small_caves,neighbor,destination,path,paths,special_cave)

    path.pop()
    if node in small_caves.keys():
        if node == special_cave:
            if small_caves[node] > 0:
                small_caves[node] -= 1
            else:
                small_caves[node] = False
        else:
            small_caves[node] = False



def get_paths(adj_list, small_caves, start, end):
    for key in small_caves.keys():
        small_caves[key] = False
    path = []
    paths = []
    special_caves = [cave for cave in small_caves if (cave != 'start' and cave != 'end')]

    for key in special_caves:
        paths.append(dfs(adj_list, small_caves, start, end, path,paths,key))


    return paths





if __name__ == "__main__":
    main()
