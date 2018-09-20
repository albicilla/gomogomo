#!/usr/bin/python3

import random

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))

    best_position = (0, 0)
    for i in range(N):
        for j in range(N):
            if field[i][j] != '.':
                continue

            position = (i, j)
            # Assume to put a stone on (i, j).
            field[i][j] = 'O'
            if CanHaveFiveStones(field, position):
                DebugPrint('I have a winning choice at (%d, %d)' % (i, j))
                return position
            # Revert the assumption.
            field[i][j] = '.'
            if GetDistance(best_position, CENTER) > GetDistance(position, CENTER):
                best_position = position
    return best_position


def OnBoard(row, col):
    return (0 <= row < N) and (0 <= col < N)


def MyThink(field):
    black_score = [0, 15, 150, 1500, 10000000]
    white_score = [0, 10, 100, 1000, 1000000]

    direction = ((0, 1), (1, 0), (1, 1), (1, -1))
    empty_score = 7

    scores = [[0] * N for _ in range(N)]

    for start_r in range(N):
        for start_c in range(N):
            for (dr, dc) in direction:
                if not OnBoard(start_r + dr * 4, start_c + dc * 4):
                    continue

                black_count = 0
                white_count = 0
                for i in range(5):
                    r = start_r + dr * i
                    c = start_c + dc * i
                    if field[r][c] == 'O':
                        black_count += 1
                    elif field[r][c] == 'X':
                        white_count += 1

                if black_count == 5 or white_count == 5:
                    score = 0
                    assert False
                elif black_count == 0 and white_count == 0:
                    score = empty_score
                elif black_count > 0 and white_count > 0:
                    score = 0
                else:
                    score = black_score[black_count] + white_score[white_count]

                for i in range(5):
                    r = start_r + dr * i
                    c = start_c + dc * i
                    scores[r][c] += score
    return FindBestHand(field, scores)


def FindBestHand(field, scores):
    best_score = -1
    best_hand = (0, 0)  # We should print something
    tie = 0

    for r in range(N):
        for c in range(N):
            if field[r][c] != '.':
                continue
            score = scores[r][c]
            if score > best_score:
                best_score = score
                best_hand = (r, c)
                tie = 0
            elif score == best_score:
                if random.randint(0, tie + 2) == 0:
                    best_score = score
                    best_hand = (r, c)
                    tie = 0
                else:
                    tie += 1
            else:
                pass
    return best_hand


# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1)) >= 5 or
            CountStonesOnLine(field, position, (1, 0)) >= 5 or
            CountStonesOnLine(field, position, (1, -1)) >= 5 or
            CountStonesOnLine(field, position, (0, 1)) >= 5)


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff):
    count = 0

    row = position[0]
    col = position[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        row += diff[0]
        col += diff[1]
        count += 1

    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != 'O':
            break
        row -= diff[0]
        col -= diff[1]
        count += 1

    return count


# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# =============================================================================
# DO NOT EDIT FOLLOWING FUNCTIONS
# =============================================================================

def main():
    field = Input()
    # position = Think(field)
    position = MyThink(field)
    Output(position)


def Input():
    field = [list(input()) for i in range(N)]
    return field


def Output(position):
    print(position[0], position[1])


# Outputs |msg| to stderr; This is actually a thin wrapper of print().
def DebugPrint(*msg):
    import sys
    print(*msg, file=sys.stderr)


if __name__    == '__main__':
    main()

