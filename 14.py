import copy
filename = '14_in.txt';

map = []
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

print "--------------------------"
print_map()

total = 0
for y in range(0, len(map)):
  for x in range(0, len(map[0])):
    if map[y][x] == 'O':
      total += (len(map) - y)

print "PART A: " + str(total)

