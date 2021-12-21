# Timothy Metzger
# Advent of Code 2021
# Day 21

from functools import cache
from itertools import product

possible_rolls = list(product([1, 2, 3], repeat=3))
def main():
    player1_pos = 7
    player2_pos = 4
    score1 = 0
    score2 = 0

    # die_start = 1
    # die_end = 100
    current = 1
    player1 = True
    rolls = 0

    while True:
        move = 0

        if current + 3 <= 100:
            move = sum(range(current, current + 3))
            current += 3
        else:
            n = 0
            while current <= 100:
                move += current
                current += 1
                n += 1
            current = 1
            while n < 3:
                move += current
                current += 1
                n += 1

        if move > 10:
            move %= 10

        if player1:
            if player1_pos + move > 10:
                player1_pos = (player1_pos + move) % 10
            else:
                player1_pos += move

            score1 += player1_pos
            player1 = False
        else:
            if player2_pos + move > 10:
                player2_pos = (player2_pos + move) % 10
            else:
                player2_pos += move

            score2 += player2_pos
            player1 = True

        rolls += 3
        if score1 >= 1000 or score2 >= 1000:
            break


    print("Part 1: ",min(score1,score2) * rolls)

    player1_wins = 0
    player2_wins = 0
    player1_pos = 4
    player2_pos = 8
    score1 = 0
    score2 = 0

    # print("Part 2: ",count_universes(player1_pos,player2_pos,player1_wins,player2_wins,score1,score2,True))


# From reddit
    print(max(dirac_dice(player1_pos, player2_pos, 0, 0)))
@cache
def dirac_dice(p1, p2, s1, s2):
    if (s1 >= 21):
        return (1, 0)
    if (s2 >= 21):
        return (0, 1)

    total_p1_wins = total_p2_wins = 0

    for r1, r2, r3 in possible_rolls:
        new_position = (p1 + r1 + r2 + r3) % 10
        new_score = s1 + new_position + 1

        p2_wins, p1_wins = dirac_dice(p2, new_position, s2, new_score)

        total_p1_wins += p1_wins
        total_p2_wins += p2_wins

    return (total_p1_wins, total_p2_wins)

# My attempt
# @cache
# def count_universes(pos1,pos2,wins1,wins2,score1,score2,player):
#
#     # Terminal state
#     if score1 >= 21 or score2 >= 21:
#         return (1,0) if player else (0,1)
#
#     if player:
#         for roll in possible_rolls:
#             move = sum(roll)
#             if pos1 + move > 10:
#                 pos1 = (pos1 + move) % 10
#             else:
#                 pos1 += move
#             score1 += pos1
#
#             wins = count_universes(pos1,pos2,wins1,wins2,score1,score2,False)
#             wins1 += wins[0]
#             wins2 += wins[1]
#     else:
#         for roll in possible_rolls:
#             move = sum(roll)
#             if pos2 + move > 10:
#                 pos2 = (pos2 + move) % 10
#             else:
#                 pos2 += move
#             score2 += pos2
#
#             wins = count_universes(pos1,pos2,wins1,wins2,score1,score2, True)
#             wins1 += wins[0]
#             wins2 += wins[1]
#
#     return wins1,wins2

if __name__ == "__main__":
    main()
