# Timothy Metzger
# Advent of Code 2021
# Day 3


def main():
    with open("inputs/day4.txt") as f:
        numbers = f.readline().strip().split(",")
        f.readline()

        boards = []
        board = []
        for line in f:

            if line == '\n':
                boards.append(board)
                board = []
            else:
                row = [int(x) for x in line.strip().split(" ") if x != ""]
                board.append(row)

        boards.append(board)

    marked_numbers = []
    for board in boards:
        marked_board = []
        for row in board:
            marked_row = [0] * len(row)
            marked_board.append(marked_row)

        marked_numbers.append(marked_board)

    winners = []
    while numbers:
        drawn_number = numbers.pop(0)
        for marker, board in zip(marked_numbers, boards):
            for i in range(len(board)):
                for j in range(len(board[0])):

                    if board[i][j] == int(drawn_number):
                        marker[i][j] = 1


        winners = check_winner(boards, marked_numbers,winners,int(drawn_number))


    print(winners)
    print("Part 1: ", winners[0])
    print("Part 2: ", winners[-1])





def check_winner(boards, marked_numbers,current_winners,drawn_number):
    for marker, board in zip(marked_numbers, boards):

        flag = False
        # Check for a row win
        for row in marker:
            if len(set(row)) == 1 and set(row) == {1}:
                flag = True

        # Check for a column win
        for j in range(len(marker[0])):
            column = []
            for i in range(len(marker)):
                column.append(marker[i][j])


            if len(set(column)) == 1 and set(column) == {1}:
                flag = True

        if flag:
            if current_winners == []:
                current_winners.append((board,sum_winner(board,marker,drawn_number)))
            already_won = False
            for winner in current_winners:
                if sorted(winner[0]) == sorted(board):
                    already_won = True
            if not already_won:
                current_winners.append((board,sum_winner(board,marker,drawn_number)))

    return current_winners





def sum_winner(board, marks,multiplier):
    sum = 0
    for marker_row, board_row in zip(marks, board):
        for mark, num in zip(marker_row, board_row):
            if mark == 0:
                sum += int(num)

    return sum * multiplier


if __name__ == "__main__":
    main()
