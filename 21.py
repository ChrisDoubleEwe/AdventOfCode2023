import copy
filename = '21_in.txt';

map = []
moves = []

def print_moves():
  global map_x, map_y
  for y in range(0, map_y):
    r = ''
    for x in range(0, map_x):
      if moves[y][x] == -1:
        r+=map[y][x];
      else:
        r+=str(moves[y][x])
    print r

map_x = -1
map_y = -1
start_x = -1
start_y = -1;
x = -1
y = -1
with open(filename) as f:
  for l in f:
    row = []
    moves_row = []
    y += 1;
    x = -1;
    for c in l.strip():
      x += 1
      row.append(c)
      moves_row.append(-1)
      if c == 'S':
        start_x = x
        start_y = y

    map.append(list(row))
    moves.append(list(moves_row))
    map_x = len(row)-1
map_y = len(map)-1
map[start_y][start_x] = '.'

empty_moves = copy.deepcopy(moves)

new_moves = copy.deepcopy(empty_moves)

moves[start_y][start_x] = 0

for s in range(0, 64):
  new_moves = copy.deepcopy(empty_moves)

  for x in range(0, map_x):
    for y in range(0, map_y):
      if moves[y][x] != '-1':
        steps = moves[y][x]
        if steps > -1:
          if y > 0:
            if map[y-1][x] == '.':
              new_moves[y-1][x] = steps +1;
          if x > 0:
            if map[y][x-1] == '.':
              new_moves[y][x-1] = steps +1;
          if x < map_x:
            if map[y][x+1] == '.':
              new_moves[y][x+1] = steps +1;
          if y < map_y:
            if map[y+1][x] == '.':
              new_moves[y+1][x] = steps +1;
          new_moves[y][x] = -1
  moves = copy.deepcopy(new_moves)
  print "------"
  print_moves();

plots = 0
for x in range(0, map_x):
  for y in range(0, map_y):
    if moves[y][x] > -1:
      plots += 1;

print "PART A: " + str(plots)



 
