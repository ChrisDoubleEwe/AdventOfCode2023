parta = 0;
partb = 0;
filename = '03_in.txt';

max_red=12;
max_green=13;
max_blue=14;

map = [];
result = [];
with open(filename) as f:
  for l in f:
    line = l.strip()
    l = [];
    res_l = [];
    for x in line:
      res = [];
      l.append(x);
      res_l.append(res);
    map.append(l);
    result.append(res_l);

# map[y][x]

max_y = len(map)-1;
max_x = len(map[0])-1;

found = 0;
part = 0;
this_num = '';
for y in range(0, max_y+1):
  for x in range(0, max_x+1):
    if map[y][x] in "0123456789":
      if y > 0:
        if  map[y-1][x] != '.' and map[y-1][x] not in '0123456789': part = 1;
      if y > 0 and x > 0:
        if map[y-1][x-1] != '.' and map[y-1][x-1] not in '0123456789': part = 1;
      if y > 0 and x < max_x: 
        if map[y-1][x+1] != '.' and map[y-1][x+1] not in '0123456789': part = 1;
      if x > 0: 
        if map[y][x-1] != '.' and map[y][x-1] not in '0123456789': part = 1;
      if x < max_x:
        if map[y][x+1] != '.' and map[y][x+1] not in '0123456789': part = 1;
      if y < max_y: 
        if  map[y+1][x] != '.' and map[y+1][x] not in '0123456789': part = 1;
      if y < max_y and x > 0: 
        if map[y+1][x-1] != '.' and map[y+1][x-1] not in '0123456789': part = 1;
      if y < max_y and x < max_x:
        if map[y+1][x+1] != '.' and map[y+1][x+1] not in '0123456789': part = 1;
      if found == 0:
        found = 1;
        this_num = map[y][x];
      else:
        this_num += map[y][x];
    else:
      found = 0;
      if this_num != '':
        if part == 1:
          parta += int(this_num);
      this_num = '';
      part = 0;


print "PART A: " + str(parta)
gear = 0;
gear_x = -1;
gear_y = -1;

for y in range(0, max_y+1):
  for x in range(0, max_x+1):
    if map[y][x] in "0123456789":
      if y > 0:
        if  map[y-1][x] == '*': gear = 1 ; gear_x = x ; gear_y = y-1;
      if y > 0 and x > 0:
        if map[y-1][x-1] == '*': gear = 1; gear_x = x-1 ; gear_y = y-1;
      if y > 0 and x < max_x:
        if map[y-1][x+1] == '*': gear = 1; gear_x = x+1 ; gear_y = y-1;
      if x > 0:
        if map[y][x-1] == '*': gear = 1; gear_x = x-1 ; gear_y = y;
      if x < max_x:
        if map[y][x+1] == '*': gear = 1; gear_x = x+1 ; gear_y = y;
      if y < max_y:
        if  map[y+1][x] == '*': gear = 1; gear_x = x ; gear_y = y+1;
      if y < max_y and x > 0:
        if map[y+1][x-1] == '*': gear = 1; gear_x = x-1 ; gear_y = y+1;
      if y < max_y and x < max_x:
        if map[y+1][x+1] == '*': gear = 1; gear_x = x+1 ; gear_y = y+1;
      if found == 0:
        found = 1;
        this_num = map[y][x];
      else:
        this_num += map[y][x];
    else:
      found = 0;
      if this_num != '':
        if gear == 1:
          result[gear_y][gear_x].append(int(this_num));
      this_num = '';
      gear = 0;


for y in range(0, max_y+1):
  for x in range(0, max_x+1):
    if len(result[y][x]) == 2:
      partb += (result[y][x][0] * result[y][x][1])

print "PART B: " + str(partb)
