import copy
filename = '18_in.txt';

map = []

def print_map():
  for row in map:
    r = ''
    for c in row:
      r+=c
    print r


dirs = []

x = 0
y = 0
max_x = 0
min_x = 0
max_y = 0
min_y = 0

with open(filename) as f:
  for l in f:
    line = l.strip().split()
    print line
    d = line[0]
    steps = int(line[1])
    if d == 'R':
      x += steps;
    if d == 'L':
      x -= steps;
    if d == 'U':
      y -= steps;
    if d == 'D':
      y += steps;
    if x < min_x:
      min_x = x
    if x > max_x:
      max_x = x
    if y < min_y:
      min_y = y
    if y > max_y:
      max_y = y
 


    col = line[2]
    col = col.replace('(', '')
    col = col.replace(')', '')
    col = col.replace('#', '')
    tup = []
    tup.append(d)
    tup.append(steps)
    tup.append(col)
    dirs.append(list(tup))

print dirs

print min_x
print max_x
print min_y
print max_y

x_shift = abs(min_x)+5
y_shift = abs(min_y)+5

print x_shift
print y_shift

for y in range(0, max_y+y_shift+10):
  map_row = []
  for x in range(0, max_x+x_shift+10):
    map_row.append('.')
  map.append(list(map_row))

  
x = x_shift
y = y_shift

for d in dirs:
  for s in range(0, d[1]):
    map[y][x] = '#'
    if d[0] == 'R':
      x += 1;
    if d[0] == 'L':
      x -= 1;
    if d[0] == 'U':
      y -= 1;
    if d[0] == 'D':
      y += 1;

#new_map = []
#for row in map:
#  print row
#  inside = 0
#  in_wall = 0;
#  new_row = []
#  for c in row:
#    print c
#    if c == '#':
#      if inside == 1 and in_wall == 0:
#        inside = 0
#      elif inside == 0 and in_wall == 0:
#        inside = 1
#      in_wall = 1
#    if c == '.':
#      in_wall = 0
#    print str(inside) + " ; " + str(in_wall)
#    if inside == 1:
#      new_row.append('#')
#    else:
#      new_row.append(c)
#  new_map.append(list(new_row))

for x in range(0, max_x+x_shift+10):
  if map[0][x] == '.':
    map[0][x] = '!'
  if map[max_y+y_shift][x] == '.':
    map[max_y+y_shift][x] = '!'

for y in range(0, max_y+y_shift+10):
  if map[y][0] == '.':
    map[y][0] = '!'
  if map[y][max_x+x_shift+5] == '.':
    map[y][max_x+x_shift+5] = '!'



filling = 1
while filling == 1:
  filling = 0;
  for y in range(0, max_y+y_shift+10):
    for x in range(0, max_x+x_shift+10):
      if map[y][x] == '!':
        if y > 0:
          if map[y-1][x] == '.': map[y-1][x] = '!' ; filling = 1
          if x > 0:
            if map[y-1][x-1] == '.': map[y-1][x-1] = '!' ; filling = 1
          if x < max_x+x_shift+1:
            if map[y-1][x+1] == '.': map[y-1][x+1] = '!' ; filling = 1
        if x > 0:
          if map[y][x-1] == '.': map[y][x-1] = '!' ; filling = 1
        if x < max_x+x_shift+9:
          if map[y][x+1] == '.': map[y][x+1] = '!' ; filling = 1
        if y < max_y+y_shift+1:
          if map[y+1][x] == '.': map[y+1][x] = '!' ; filling = 1
          if x > 0:
            if map[y+1][x-1] == '.': map[y+1][x-1] = '!' ; filling = 1
          if x < max_x+x_shift+1:
            if map[y+1][x+1] == '.': map[y+1][x+1] = '!' ; filling = 1


 



for y in range(0, max_y+y_shift+10):
  for x in range(0, max_x+x_shift+10):
    if map[y][x] == '.':
      map[y][x] = '#'



for y in range(0, max_y+y_shift+10):
  for x in range(0, max_x+x_shift+10):
    if map[y][x] == '!':
      map[y][x] = '.'

print_map();

parta = 0
for y in range(0, max_y+y_shift+10):
  for x in range(0, max_x+x_shift+10):
    if map[y][x] == '#':
      parta += 1


print "PART A: " + str(parta)
