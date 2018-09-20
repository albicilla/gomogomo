#!/usr/bin/python3

import sys

N = 15


# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
  scores = {}
  is_first_turn=1
  fcnt=0
  for i in range(N):
      for j in range(N):
          if field[i][j]!='.':
              fcnt+=1
  if fcnt>1:
      is_first_turn=0
  if is_first_turn==1:
      for i in range(6,7):
          for j in range(6,7):
              if(field[i][j]=='.'):
                  return (i,j)

  temp_score=100
  ret_position=(0,0)


  for i in range(N):
    for j in range(N):
      if field[i][j] != '.':
        continue
      position = (i, j)
      v=GetScore(field, position)
      # DebugPrint('value = (%d)' % (v))

      if v<temp_score:
          # DebugPrint('value = (%d)' % (v))
          # DebugPrint('position = (%d,%d)' % (i,j))

          temp_score=v
          ret_position=(i,j)


  return ret_position

def GetScore(field, position):
    o_stones = []
    o_stones.append(CountStonesInDirection(field, position, (1, 1), 'O'))
    o_stones.append(CountStonesInDirection(field, position, (-1, -1), 'O'))

    o_stones.append(CountStonesInDirection(field, position, (1, 0), 'O'))
    o_stones.append(CountStonesInDirection(field, position, (-1, 0), 'O'))

    o_stones.append(CountStonesInDirection(field, position, (1, -1), 'O'))
    o_stones.append(CountStonesInDirection(field, position, (-1, 1), 'O'))

    o_stones.append(CountStonesInDirection(field, position, (0, 1), 'O'))
    o_stones.append(CountStonesInDirection(field, position, (0, -1), 'O'))

    o_stones = sorted(o_stones, reverse=True)


    x_stones = []
    x_stones.append(CountStonesInDirection(field, position, (1, 1), 'X'))
    x_stones.append(CountStonesInDirection(field, position, (-1, -1), 'X'))

    # DebugPrint((x_stones))

    x_stones.append(CountStonesInDirection(field, position, (1, 0), 'X'))
    x_stones.append(CountStonesInDirection(field, position, (-1, 0), 'X'))

    # DebugPrint((x_stones))

    x_stones.append(CountStonesInDirection(field, position, (1, -1), 'X'))
    x_stones.append(CountStonesInDirection(field, position, (-1, 1), 'X'))

    # DebugPrint((x_stones))

    x_stones.append(CountStonesInDirection(field, position, (0, 1), 'X'))
    x_stones.append(CountStonesInDirection(field, position, (0, -1), 'X'))


    x_stones = sorted(x_stones, reverse=True)
    # DebugPrint('position = (%d,%d)' % (position[0],position[1]))
    # DebugPrint((o_stones))
    # DebugPrint((x_stones))


    EnemyValue=0
    MyValue=0

    if o_stones[0] >= 5:
        return 0

    if x_stones[0] >= 5:
        return 0
    #禁じ手
    if x_stones[0] >= 4 and x_stones[1] >= 4:
        return 1
    #禁じ手
    if x_stones[0] >= 4 and x_stones[1] >= 3:
        return 1

    #禁じ手
    if x_stones[0] >= 3 and x_stones[1] >= 3:
        return 2


    #禁じ手
    if o_stones[0] >= 4 and o_stones[1]>=4:
        return 1
    #禁じ手
    if o_stones[0] >= 3 and o_stones[1] >= 3:
        return 3
    #禁じ手

    if x_stones[0] >= 4:
        return 4
    if o_stones[0] >= 4:
        return 5


    if x_stones[0] >= 3:
        return 4
    if x_stones[0] >= 2 and x_stones[1]>=2:
        return 5
    if x_stones[0] >= 3:
        return 8
    if x_stones[0] >= 2:
        return 10




    # if x_stones[0] == 3 and o_stones[1] == 2:
    #     EnemyValue = 6
    # if x_stones[0] == 3:
    #     EnemyValue = 8
    # if x_stones[0] == 2 and o_stones[1] == 2:
    #     EnemyValue = 10
    # if x_stones[0] == 2:
    #     Enemyvalue = 11


    if o_stones[0] >= 3:
        return 8
    if o_stones[0] >= 2:
        return 10

    # if o_stones[0] == 3 and o_stones[1] == 2:
    #     MyValue= 6
    #
    # if o_stones[0] == 3:
    #     MyValue= 8
    # if o_stones[0] == 2:
    #     MyValue= 11



    return 30


def CountLivingStonesInDirection(field,position,diff,stone):
    field[position[0]][position[1]]=stone
    mex_count = 0
    for start in range(5):
        row = position[0] - start * diff[0]
        col = position[1] - start * diff[1]
        i = 0
        count = 0
        while i < 5:
            if row < 0 or col < 0 or row >=N or col >= N:
                break
            if field[row][col]!=stone and field[row][col]!= '.':
                break
            if field[row][col] == stone:
                count += 1
            elif field[row][col] == '.':
                count = 0
            row += diff[0]
            col += diff[1]
            i+=1
        #iが5でないときはその5のラインに壁もしくは他のコマがある
        #つまり5で埋められる可能性が残っている。
        if i==5 and count > max_count:
            max_count = count
    field[position[0]][position[1]] = '.'
    return max_count

def CountStonesInDirection(field, position, diff, stone):
  field[position[0]][position[1]] = stone
  max_count = [0,0,0]
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
        #if count > 1:
            #DebugPrint((count))
        count = 0
      row += diff[0]
      col += diff[1]
      i += 1
    if i == 5 :
      max_count.append(count)
  field[position[0]][position[1]] = '.'
  max_count = sorted(max_count, reverse=True)

  ret_value=max_count[0]
  return ret_value

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
