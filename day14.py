# Timothy Metzger
# Advent of Code 2021
# Day 14

from collections import Counter

def main():
    with open('inputs/day14.txt') as f:
        template = f.readline().strip()
        f.readline()
        pair_insertions = {}
        for line in f:
            key,val = line.strip().split(" -> ")
            pair_insertions[key] = val


    # Part 1:
    # Naive solution is the easiest here
    # Each iterations adds len() - 1 characters to the length


    # steps = 10
    #
    # for i in range(steps):
    #     new_str = ""
    #     for i in range(len(template) - 1):
    #         new_str += template[i] + pair_insertions[template[i:i+2]]
    #     new_str += template[-1]
    #     template = new_str
    #
    # counts = Counter(template)
    # print(counts)
    # part1_ans = max(counts.values()) - min(counts.values())
    # print('Part 1: ', part1_ans)


    # Part 2:
    # Going to try keeping count of the number of pairs each iteration
    steps = 40


    pair_counts = {key: 0 for key in pair_insertions.keys()}

    letters = {}
    for key in pair_counts.keys():
        letters[key[0]] = 0
        letters[key[1]] = 0
    for char in template:
        letters[char] += 1

    for i in range(len(template) - 1):
        pair_counts[template[i:i+2]] = 1

    for i in range(steps):
        to_add = {}
        for key,val in pair_counts.items():
            if val == 0:
                continue
            else:
                pair_counts[key] = 0

                # Create left pair
                left_key = key[0] + pair_insertions[key]
                if left_key not in to_add:
                    to_add[left_key] = 0

                to_add[left_key] += val

                # Create right pair
                right_key = pair_insertions[key] + key[1]
                if right_key not in to_add:
                    to_add[right_key] = 0
                to_add[right_key] += val

                # Add letters to overall count
                letters[pair_insertions[key]] += val

                continue


        for key, val in to_add.items():
            pair_counts[key] += val

        print(f"Step {i+1}: {max(letters.values()) - min(letters.values())}")

    part2_answer = max(letters.values()) - min(letters.values())
    print("Part 2: ", part2_answer)



if __name__ == "__main__":
    main()