import copy
filename = '14_in.txt';

map = []
skip = 0
with open(filename) as f:
  for l in f:
    row = []
    for c in l.strip():
      row.append(c);
    map.append(list(row));

def print_map():
  for row in map:
    r = ''
    for c in row:
      r+=c
    print r

print_map()
 
#iterations = 1000000000;
iterations = 1000000000;

remember = -1
while iterations > 0:
  iterations -= 1;
  print "Iteration: " + str(iterations)
  # Tilt north
  move = 1
  while move == 1:
    move = 0
    for y in range(1, len(map)):
      for x in range(0, len(map[0])):
        if map[y][x] == 'O':
          if map[y-1][x] == '.':
            map[y-1][x] = 'O';
            map[y][x] = '.';
            move = 1;

  # Tilt west
  move = 1
  while move == 1:
    move = 0
    for y in range(0, len(map)):
      for x in range(1, len(map[0])):
        if map[y][x] == 'O':
          if map[y][x-1] == '.':
            map[y][x-1] = 'O';
            map[y][x] = '.';
            move = 1;

  # Tilt south
  move = 1
  while move == 1:
    move = 0
    for y in range(0, len(map)-1):
      for x in range(0, len(map[0])):
        if map[y][x] == 'O':
          if map[y+1][x] == '.':
            map[y+1][x] = 'O';
            map[y][x] = '.';
            move = 1;

  # Tilt east
  move = 1
  while move == 1:
    move = 0
    for y in range(0, len(map)):
      for x in range(0, len(map[0])-1):
        if map[y][x] == 'O':
          if map[y][x+1] == '.':
            map[y][x+1] = 'O';
            map[y][x] = '.';
            move = 1;


  total = 0
  for y in range(0, len(map)):
    for x in range(0, len(map[0])):
      if map[y][x] == 'O':
        total += (len(map) - y)

  print "  load: " + str(total)
  if iterations == 999999827:
    remember = total
    last_iter = iterations

  if remember > -1:
    if total == remember:
      print str(iterations) + " : " + str(iterations - last_iter)
      diff = abs(iterations - last_iter)
      print diff
      last_iter = iterations
      if diff > 0 and skip == 0:
        skip = 1
        increm = iterations // diff
        iterations -= ((increm - 5) * diff)

      
print "PART B: " + str(total)
