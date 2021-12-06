# Timothy Metzger
# Advent of Code 2021
# Day 5

# import pickle
from collections import Counter

# Got this solution from reddit from u/conkerandco
# Data holds the number of fish holding that life cycle value until reproducing
# Each iteration the fish at 0 position ie. the fish that is going to reproduce is moved to the back of fishs
# and then that value is added to what would have been the previously second to last accounting for the reproduction
# of the all of the children
def model_lf(days, data):
    for _ in range(days):
        data.append(data.pop(0))
        data[6] += data[-1]
    return sum(data)

def main():
    with open('inputs/day6.txt') as f:
        fishs = Counter(list(map(int, f.read().split(','))))
    print(fishs)
    data = [fishs[i] for i in range(9)]
    print(model_lf(256,data))


    # This is the naive solution and me trying to make it work for 256 days by pickling the arrays to get around memory
    # fish_groups = []
    # final_day = 256
    # for day in range(1,final_day + 1):
    #     print(day)
    #     if fish_groups == []:
    #         new_fish = spawn_fish(fishs)
    #         for fish in new_fish:
    #             fishs.append(fish)
    #
    #         if len(fishs) > 5000:
    #             fish_groups.append(pickle.dumps(fishs))
    #
    #     else:
    #         holding_tank = []
    #         for i, fish_group in enumerate(fish_groups):
    #             current = pickle.loads(fish_group)
    #             new_fish = spawn_fish(current)
    #             if len(current) > 5000:
    #                 for fish in new_fish:
    #                     holding_tank.append(fish)
    #                     if len(holding_tank) > 5000:
    #                         fish_groups.append(pickle.dumps(holding_tank))
    #                         holding_tank = []
    #             else:
    #                 for fish in new_fish:
    #                     current.append(fish)
    #
    #             fish_groups[i] = pickle.dumps(current)
    #
    #         if holding_tank != []:
    #
    #             fish_groups.append(pickle.dumps(holding_tank))
    #
    #
    # count = 0
    # for group in fish_groups:
    #     count += len(pickle.loads(group))
    #
    # print(count)
    # # print("Part 1: ",len(fishs))


def spawn_fish(fishs):
    fish_to_add = []

    for i in range(len(fishs)):
        if fishs[i] == 0:
            fish_to_add.append(8)
            fishs[i] = 6
        else:
            fishs[i] -= 1

    return fish_to_add


if __name__ == "__main__":
    main()