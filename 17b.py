import copy
import os
filename = '17_in.txt';
best_route = ''
best = 99999999999

map = []
route = []

def print_map():
  for row in map:
    r = ''
    for c in row:
      r+=c
    print r

def print_route_map():
  os.system('clear')
  for row in route:
    r = ''
    for c in row:
      if c == 999999999:
       r += ' '
      else:
       r += '#'
    print r

myqueue = []

new_row = []
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);
new_row.append(999999999);


with open(filename) as f:
  for l in f:
    row = [];
    route_row = [];
    for c in l.strip():
      row.append(int(c));
      route_row.append(list(new_row));
    map.append(list(row));
    route.append(list(route_row));

map_x = len(map[0])-1;
map_y = len(map)-1;
end_x = map_x
end_y = map_y


def move():
  global best
  global best_route
  global myqueue
  global route

  while len(myqueue) > 0:

    #print_route_map()
  
    i = -1;
    lowest = 9999999999999;
    for z in range(0, len(myqueue)):
      if myqueue[z][2] < lowest:
        lowest = myqueue[z][2]
        i = z

      
    node = myqueue.pop(i)
    x = node[0]
    y = node[1]
    h = node[2]
    d = node[3]
    s = node[4]
    print h

    s += 1
    if s > 10:
      continue;
    steps = s


    if steps > 10:
      print "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEK"
    mod_x = 0;
    mod_y = 0;
    dir = -1
    if d == 'n':
      mod_y = -1;
      dir = 0 
    if d == 's':
      mod_y = 1;
      dir = 10
    if d == 'e':
      mod_x = 1;
      dir = 20
    if d == 'w':
      mod_x = -1;
      dir = 30
    x = x + mod_x
    y = y + mod_y
    dir += steps-1

    if x < 0 or x > map_x or y < 0 or y > map_y:
      continue;
    h = h + map[y][x]

    if route[y][x][dir] != 999999999:
      continue;

    if h > route[y][x][dir]:
      continue

    if h < route[y][x][dir]:
      if y == end_y and x == end_x:
        if steps > 3:
          route[y][x][dir] = h
      else:
        route[y][x][dir] = h

    if y == end_y and x == end_x and steps > 3:
      if min(route[y][x]) < best:
        best = min(route[y][x])
        print "New best route: " + str(best)
    if y == end_y and x == end_x and steps > 3:
      continue


    if d == 'n':
      myqueue.append([x, y, h, 'n', s])
      if s > 3:
        myqueue.append([x, y, h, 'e', 0])
        myqueue.append([x, y, h, 'w', 0])
    elif d == 's':
      myqueue.append([x, y, h, 's', s])
      if s > 3:
        myqueue.append([x, y, h, 'e', 0])
        myqueue.append([x, y, h, 'w', 0])
    elif d == 'e':
      myqueue.append([x, y, h, 'e', s])
      if s > 3:
        myqueue.append([x, y, h, 's', 0])
        myqueue.append([x, y, h, 'n', 0])
    elif d == 'w':
      myqueue.append([x, y, h, 'w', s])
      if s > 3:
        myqueue.append([x, y, h, 's', 0])
        myqueue.append([x, y, h, 'n', 0])

myqueue.append([0, 0, 0, 'e', 0])
myqueue.append([0, 0, 0, 's', 0])
move()



partb = min(route[end_y][end_x])
print "PART B: " + str(partb)

