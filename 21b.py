import copy
filename = '21_in.txt';

tot_steps = 200000

map = []


map_x = -1
map_y = -1
start_x = -1
start_y = -1;
x = -1
y = -1
with open(filename) as f:
  for l in f:
    row = []
    y += 1;
    x = -1;
    for c in l.strip():
      x += 1
      row.append(c)
      if c == 'S':
        start_x = x
        start_y = y

    map.append(list(row))
    map_x = len(row)-1
map_y = len(map)-1
map[start_y][start_x] = '.'

start = []
start.append(start_y)
start.append(start_x)
print map_x
print map_y
mod_val = map_x+1

points = []
points.append(list(start))


last = 0
last_diff = []
for i in range(0, map_x+1):
  last_diff.append(0)
rem = []
inc = []
last_rem = []
done_steps = 0;
for s in range(0, tot_steps):
  done_steps +=1
  new_points = []

  for p in points:
    px = p[1]
    py = p[0]

    pEx = (px+1) % (map_x+1);
    pWx = (px-1) % (map_x+1);
    pNx = px % (map_x+1)
    pSx = px % (map_x+1)

    pEy = py % (map_y+1)
    pWy = py % (map_y+1)
    pNy = (py-1) % (map_y+1)
    pSy = (py+1) % (map_y+1)



    # EAST
    if map[pEy][pEx] == '.':
      new_point = []
      new_point.append(py);
      new_point.append(px+1);
      if new_point not in new_points:
        new_points.append(list(new_point))
    # WEST
    if map[pWy][pWx] == '.':
      new_point = []
      new_point.append(py);
      new_point.append(px-1);
      if new_point not in new_points:
        new_points.append(list(new_point))
    # SOUTH
    if map[pSy][pSx] == '.':
      new_point = []
      new_point.append(py+1);
      new_point.append(px);
      if new_point not in new_points:
        new_points.append(list(new_point))
    # NORTH
    if map[pNy][pNx] == '.':
      new_point = []
      new_point.append(py-1);
      new_point.append(px);
      if new_point not in new_points:
        new_points.append(list(new_point))
  points = copy.deepcopy(new_points)
  #print "Step: " + str(s) + " -- " + str(points)

  if len(rem) < map_x:
    rem.append((len(points)-last) - last_diff[s%mod_val])
    inc.append(len(points)-last)
  else:
    print rem
    if rem == last_rem:
      print "WE HAVE A REPEATING MATCH!"
      rem.append((len(points)-last) - last_diff[s%mod_val])
      inc.append(len(points)-last)

      print rem
      print inc
      break
    else:
      last_rem = copy.deepcopy(rem)
      rem = []
      inc = []


  print "In " + str(done_steps) + " steps, we reach: " + str(len(points)) + " ; DIFF = " + str(len(points)-last) + " ; Diff2 = " + str((len(points)-last) - last_diff[s%mod_val])
  print "s= " + str(s) + "index: " + str(s%mod_val)
  print "======"

  this_last_diff = (len(points)-last)
  last_diff[s%mod_val] = this_last_diff

  last = len(points)

print "Steps done: " + str(done_steps)

total = len(points)
loop = 1
print inc
#done_steps -= 1
for x in range(0, 26501365-done_steps+5):
  done_steps += 1
  s = done_steps - 1
  inc[(s%mod_val)]+=rem[(s%mod_val)]
  total += inc[(s%mod_val)]
  if done_steps in [100,500,1000,5000, 26501365]:
    print "In " + str(done_steps) + " steps, we reach: " + str(total)


 
