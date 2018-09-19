#!/usr/bin/python3

import sys

N = 15

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
  scores = {}
  for i in range(N):
    for j in range(N):
      if field[i][j] != '.':
        continue
      position = (i, j)
      scores[position] = GetScore(field, position)

  sorted_scores = sorted(scores.items(), key=lambda x: x[1])
  return sorted_scores[0][0]

def GetScore(field, position):
  o_stones = []
  o_stones.append(CountStonesInDirection(field, position, (1, 1), 'O'))
  o_stones.append(CountStonesInDirection(field, position, (1, 0), 'O'))
  o_stones.append(CountStonesInDirection(field, position, (1, -1), 'O'))
  o_stones.append(CountStonesInDirection(field, position, (0, 1), 'O'))
  o_stones = sorted(o_stones, reverse=True)
  x_stones = []
  x_stones.append(CountStonesInDirection(field, position, (1, 1), 'X'))
  x_stones.append(CountStonesInDirection(field, position, (1, 0), 'X'))
  x_stones.append(CountStonesInDirection(field, position, (1, -1), 'X'))
  x_stones.append(CountStonesInDirection(field, position, (0, 1), 'X'))
  x_stones = sorted(x_stones, reverse=True)

  if o_stones[0] == 5:
    return 0
  if x_stones[0] == 5:
    return 1
  if o_stones[0] == 4:
    return 2
  if x_stones[0] == 4:
    return 3
  if o_stones[0] == 3 and o_stones[1] == 3:
    return 4
  if x_stones[0] == 3 and x_stones[1] == 3:
    return 5
  if o_stones[0] == 3 and o_stones[1] == 2:
    return 6
  if x_stones[0] == 3 and x_stones[1] == 2:
    return 7
  if o_stones[0] == 3:
    return 8
  if x_stones[0] == 3:
    return 9
  if o_stones[0] == 2 and o_stones[1] == 2:
    return 10
  if o_stones[0] == 2:
    return 11
  return 20

def CountStonesInDirection(field, position, diff, stone):
  field[position[0]][position[1]] = stone
  max_count = 0
  for start in range(5):
    row = position[0] - start * diff[0]
    col = position[1] - start * diff[1]
    i = 0
    count = 0
    while i < 5:
      if row < 0 or col < 0 or row >= N or col >= N:
        break
      if field[row][col] != stone and field[row][col] != '.':
        break
      if field[row][col] == stone:
        count += 1
      elif field[row][col] == '.':
        count = 0
      row += diff[0]
      col += diff[1]
      i += 1
    if i == 5 and count > max_count:
      max_count = count
  field[position[0]][position[1]] = '.'
  return max_count

# Outputs |msg| to stderr; This is actually a thin wrapper of print().
def DebugPrint(msg):
    import sys
    print(msg, file=sys.stderr)

# =============================================================================
# DO NOT EDIT FOLLOWING FUNCTIONS
# =============================================================================

def main():
  field = Input()
  position = Think(field)
  Output(position)

def Input():
  field = [list(input()) for i in range(N)]
  return field

def Output(position):
  print(position[0], position[1])

if __name__  == '__main__':
  main()

