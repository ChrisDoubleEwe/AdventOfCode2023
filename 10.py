from copy import copy, deepcopy
filename = '10_in.txt';
parta = 0


map_size_x = 0;
map_size_y = 0;
map = []
dist = []

def print_map():
  for row in map:
    r = ''
    for c in row:
      r+=c 
    print r

def print_dist():
  for row in dist:
    r = ''
    for c in row:
      if c == -1:
        r += '.'
      else:
        r+=str(c)[-1]
    print r

def print_emap():
  for row in expand_map:
    r = ''
    for c in row:
      if c == -1:
        r += '.'
      else:
        r+=str(c)[-1]
    print r


first = 1
empty_row = []
empty_dest = []

with open(filename) as f:
  for l in f:
    map_size_x = len(l.strip())
    map_size_y += 1

    row = []
    row.append('.')
    
    if first == 1:
      for i in range(0, map_size_x+2):
        empty_row.append('.')
        empty_dest.append(-1)
      map.append(empty_row);
      dist.append(empty_dest);
      first = 0

    blank_row = []
    blank_row.append(-1);
    blank_row.append(-1);

    c_count = 1
    for c in l.strip():
      row.append(c)
      blank_row.append(-1);
      if c == "S":
        start_x = c_count
        start_y = map_size_y
      c_count += 1

    row.append('.')
    map.append(row)
    dist.append(blank_row)

map.append(list(empty_row));
dist.append(list(empty_dest));


dist[start_y][start_x] = 0

new_map = deepcopy(map);
for x in range(0, map_size_x+2):
  for y in range(0, map_size_y+2):
    new_map[y][x]= 'X'

new_map[start_y][start_x] = '-'

mapping = 1
loop = 0
while mapping == 1:
  loop += 1
  print "Mapping route... " + str(loop)
  last_map = deepcopy(new_map);
  mapping = 0
  for x in range(0, map_size_x+2):
    for y in range(0, map_size_y+2):
      if new_map[y][x] == '-':
        new_map[y][x] = ' '
        if map[y][x] == 'S':
          if map[y][x+1] in 'J-7':
            new_map[y][x+1] = '-'
          if map[y][x-1] in 'L-F':
            new_map[y][x-1] = '-'
          if map[y-1][x] in '|7F':
            new_map[y-1][x] = '-'
          if map[y+1][x] in '|LJ':
            new_map[y+1][x] = '-'

        if map[y][x] == '|':
          if map[y-1][x] in '|7F':
            new_map[y-1][x] = '-'
          if map[y+1][x] in '|LJ':
            new_map[y+1][x] = '-'

        if map[y][x] == '-':
          if map[y][x+1] in 'J-7':
            new_map[y][x+1] = '-'
          if map[y][x-1] in 'L-F':
            new_map[y][x-1] = '-'

        if map[y][x] == 'J':
          if map[y][x-1] in 'L-F':
            new_map[y][x-1] = '-'
          if map[y-1][x] in '|7F':
            new_map[y-1][x] = '-'

        if map[y][x] == '7':
          if map[y][x-1] in 'L-F':
            new_map[y][x-1] = '-'
          if map[y+1][x] in '|LJ':
            new_map[y+1][x] = '-'

        if map[y][x] == 'L':
          if map[y][x+1] in 'J-7':
            new_map[y][x+1] = '-'
          if map[y-1][x] in '|7F':
            new_map[y-1][x] = '-'

        if map[y][x] == 'F':
          if map[y][x+1] in 'J-7':
            new_map[y][x+1] = '-'
          if map[y+1][x] in '|LJ':
            new_map[y+1][x] = '-'

  for x in range(0, map_size_x+2):
    for y in range(0, map_size_y+2):
      if last_map[y][x] != new_map[y][x]:
        mapping = 1

mapping = 1
loop = 0
while mapping == 1:
  mapping = 0
  loop += 1
  print "Calculating distances... " + str(loop)

  for x in range(0, map_size_x+2):
    for y in range(0, map_size_y+2):

      if dist[y][x] == -1 and new_map[y][x] != "X" :
        if map[y][x] == '|':
          dists = []
          if dist[y-1][x] != -1:
            dists.append(dist[y-1][x])
          if dist[y+1][x] != -1:
            dists.append(dist[y+1][x])
          if len(dists) > 0:
            if max(dists) > -1:
              dist[y][x] = max(dists)+1
              mapping = 1

        if map[y][x] == '-':
          dists = []
          if dist[y][x-1] != -1:
            dists.append(dist[y][x-1])
          if dist[y][x+1] != -1:
            dists.append(dist[y][x+1])
          if len(dists) > 0:
            if max(dists) > -1:
              dist[y][x] = max(dists)+1
              mapping = 1

        if map[y][x] == 'L':
          dists = []
          if dist[y-1][x] != -1:
            dists.append(dist[y-1][x])
          if dist[y][x+1] != -1:
            dists.append(dist[y][x+1])
          if len(dists) > 0:
            if max(dists) > -1:
              dist[y][x] = max(dists)+1
              mapping = 1
 
        if map[y][x] == 'J':
          dists = []
          if dist[y-1][x] != -1:
            dists.append(dist[y-1][x])
          if dist[y][x-1] != -1:
            dists.append(dist[y][x-1])
          if len(dists) > 0:
            if max(dists) > -1:
              dist[y][x] = max(dists)+1
              mapping = 1

        if map[y][x] == '7':
          dists = []
          if dist[y+1][x] != -1:
            dists.append(dist[y+1][x])
          if dist[y][x-1] != -1:
            dists.append(dist[y][x-1])
          if len(dists) > 0:
            if max(dists) > -1:
              dist[y][x] = max(dists)+1
              mapping = 1

        if map[y][x] == 'F':
          dists = []
          if dist[y+1][x] != -1:
            dists.append(dist[y+1][x])
          if dist[y][x+1] != -1:
            dists.append(dist[y][x+1])
          if len(dists) > 0:
            if max(dists) > -1:     
              dist[y][x] = max(dists)+1
              mapping = 1


parta = 0;
for x in range(0, map_size_x+2):
  for y in range(0, map_size_y+2):
    if dist[y][x] > parta:
      parta = dist[y][x] 

print "PART A: " + str(parta)

expand_map = []
row = []
for x in range(0, (map_size_x+2)*3):
  row.append('x');
for y in range(0, (map_size_y+2)*3):
  expand_map.append(list(row))




print_dist()
for x in range(0, map_size_x+2):
  for y in range(0, map_size_y+2):
    if dist[y][x] == -1:
      map[y][x] = '.'
print_map()

for x in range(0, map_size_x+2):
  for y in range(0, map_size_y+2):
    if map[y][x] == "S":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     'X'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     'X'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = 'X'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = 'X'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == ".":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     '.'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     '.'
      expand_map[(y*3)+1][(x*3)+1] = 'O'
      expand_map[(y*3)+1][(x*3)+2] = '.'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = '.'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "-":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     '.'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     'X'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = 'X'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = '.'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "|":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     'X'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     '.'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = '.'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = 'X'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "J":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     'X'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     'X'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = '.'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = '.'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "L":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     'X'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     '.'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = 'X'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = '.'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "7":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     '.'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     'X'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = '.'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = 'X'
      expand_map[(y*3)+2][(x*3)+2] = '.'
    if map[y][x] == "F":
      expand_map[y*3][x*3] =         '.'
      expand_map[y*3][(x*3)+1] =     '.'
      expand_map[y*3][(x*3)+2] =     '.'
      expand_map[(y*3)+1][x*3] =     '.'
      expand_map[(y*3)+1][(x*3)+1] = 'X'
      expand_map[(y*3)+1][(x*3)+2] = 'X'
      expand_map[(y*3)+2][x*3] =     '.'
      expand_map[(y*3)+2][(x*3)+1] = 'X'
      expand_map[(y*3)+2][(x*3)+2] = '.'







expand_map[0][0] = ' ';

doing = 1
while doing == 1:
  doing = 0
  for x in range(0, (map_size_x+2)*3):
    for y in range(0, (map_size_y+2)*3):
      if expand_map[y][x] == ' ':
        if x > 0:
          if expand_map[y][x-1] not in 'X ': 
            expand_map[y][x-1] = ' ';
            doing = 1;
        if x < ((map_size_x+2)*3)-1:
          if expand_map[y][x+1] not in 'X ': 
            expand_map[y][x+1] = ' ';
            doing = 1;
        if y > 0:
          if expand_map[y-1][x] not in 'X ':
            expand_map[y-1][x] = ' ';
            doing = 1;
        if y < ((map_size_y+2)*3)-1:
          if expand_map[y+1][x] not in 'X ':
            expand_map[y+1][x] = ' ';
            doing = 1;

 
print_emap()    
    
partb = 0
for x in range(0, (map_size_x+2)*3):
  for y in range(0, (map_size_y+2)*3):
    if expand_map[y][x] == 'O':
      partb+=1

print "PART B: " + str(partb)

