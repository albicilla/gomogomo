#!/usr/bin/python3

N = 15


# ループで8方向を見るための配列
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,-1,-1,-1,0,1,1,1]

#field配列の範囲内かをちぇっくする
def inboard(position):
    if(position[0]>14 or position[0]<0 or position[1]>14 or position[1]<0):
        return 0
    else:
        return 1



#postion に置いた時の 盤面の　評価関数 引数 (field 盤面　which_player 敵か味方か 次に置く位置　position depth 深さ)
#which_player が 0だったら自分　1だったら敵
def calcValue(field,which_player,position,depth):


    value = 0
    # if which_player==0:
    #     value += CountStonesOnLine(field, position, (1, 1),'O')
    #     value += CountStonesOnLine(field, position, (1, 0),'O')
    #     value += CountStonesOnLine(field, position, (1, -1),'O')
    #     value += CountStonesOnLine(field, position, (0, 1),'O')
    # else:
    #     value += CountStonesOnLine(field, position, (1, 1),'X')
    #     value += CountStonesOnLine(field, position, (1, 0),'X')
    #     value += CountStonesOnLine(field, position, (1, -1),'X')
    #     value += CountStonesOnLine(field, position, (0, 1),'X')
    #
    # value += CountStonesOnLine(field, position, (1, 1),'.')
    # value += CountStonesOnLine(field, position, (1, 0),'.')
    # value += CountStonesOnLine(field, position, (1, -1),'.')
    # value += CountStonesOnLine(field, position, (0, 1),'.')


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
        value = 12
    if x_stones[0] == 5:
        value = 12
    if o_stones[0] == 4:
        value = 11
    if x_stones[0] == 4:
        value = 11
    if o_stones[0] == 3 and o_stones[1] == 3:
        return 10
    if x_stones[0] == 3 and x_stones[1] == 3:
        return 10
    if o_stones[0] == 3 and o_stones[1] == 2:
        return 9
    if x_stones[0] == 3 and x_stones[1] == 2:
        return 9
    if o_stones[0] == 3:
        return 8
    if x_stones[0] == 3:
        return 8
    if o_stones[0] == 2 and o_stones[1] == 2:
        return 7
    if o_stones[0] == 2:
        return 7

    return value

# The main routine of AI.
# input: str[N][N] field : state of the field.
# output: int[2] : where to put a stone in this turn.
def Think(field):
    CENTER = (int(N / 2), int(N / 2))

    best_position = (0, 0)



    #置けるマスを列挙 上下斜め左右で隣接しているところに置くことを考える。
    temp_value = 0
    for i in range(N):
        for j in range(N):
            temp_position = (i,j)
            if inboard(temp_position):
                if CanPutStone(field,temp_position):
                    #DebugPrint('I can put stone at (%d, %d)' % (temp_position[0], temp_position[1]))
                    v = calcValue(field,0,temp_position)
                    #DebugPrint('value = (%d)' % (v))

                    if(int(v)>int(temp_value)):
                        #DebugPrint('refine = (%d, %d)' % (i,j))
                        temp_value=v
                        best_position=temp_position

    #DebugPrint('best_position = (%d,%d)' % (best_position[0],best_position[1]))


    return best_position

# positionの位置に石が置けるかを判定　置ける時 1 置けない時 0
def CanPutStone(field,position):
    #8方向ループ
    for i in range(8):
        pos = (position[0]+dy[i],position[1]+dx[i])
        if (inboard(pos) and (field[pos[0]][pos[1]]=='O' or field[pos[0]][pos[1]]=='X') and (field[position[0]][position[1]]=='.')):
            return 1
    return 0




# Returns true if you have five stones from |position|. Returns false otherwise.
def CanHaveFiveStones(field, position):
    return (CountStonesOnLine(field, position, (1, 1),'O') >= 5 or
            CountStonesOnLine(field, position, (1, 0),'O') >= 5 or
            CountStonesOnLine(field, position, (1, -1),'O') >= 5 or
            CountStonesOnLine(field, position, (0, 1),'O') >= 5)


# Returns the number of stones you can put around |position| in the direction specified by |diff|.
def CountStonesOnLine(field, position, diff,koma):
    count = 0

    row = position[0]
    col = position[1]

    cnt1 = 0
    cnt2 = 0

    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != koma:
            break
        row += diff[0]
        col += diff[1]
        count += 1
        cnt1 += 1
        if(cnt1 > 5):
            break


    row = position[0] - diff[0]
    col = position[1] - diff[1]
    while True:
        if row < 0 or col < 0 or row >= N or col >= N or field[row][col] != koma:
            break
        row -= diff[0]
        col -= diff[1]
        count += 1
        if(cnt2 > 5):
            break


    return count

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


# Returns the Manhattan distance from |a| to |b|.
def GetDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


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


# Outputs |msg| to stderr; This is actually a thin wrapper of print().
def DebugPrint(*msg):
    import sys
    print(*msg, file=sys.stderr)


if __name__    == '__main__':
    main()
