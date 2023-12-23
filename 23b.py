import copy
filename = '23_in.txt';

seen = []
map = []
steps = []
routes = []

def print_map(steps):
  print "----------------"
  for row in steps:
    r = ''
    for c in row:
      if c > -1:
        r+=str(c)[-1]
      else:
        r+=' '
    if len(r.replace(' ','')) > 0:
      print r


with open(filename) as f:
  for l in f:
    row = []
    s_row = []
    for c in l.strip():
      if c == '>':
        row.append('.');
      elif c == '<':
        row.append('.');
      elif c == '^':
        row.append('.');
      elif c == 'v':
        row.append('.');
      else:
        row.append(c);
      s_row.append(-1);
    map.append(list(row))
    steps.append(list(s_row))
    seen.append(list(s_row))


map_x = len(map[0])-1
map_y = len(map)-1
print "MAP X " + str(map_x)
print "MAP Y " + str(map_y)



x = 1
y = 0

end_x = map_x -1
end_y = map_y 

steps[y][x] = 0


def move(steps, x, y, d):
  global routes
  #print_map(steps)
  if d > 2100:
    return

  if steps[y][x] < (seen[y][x] - 2000):
    return
  if steps[y][x] > (seen[y][x]):
    seen[y][x] = steps[y][x]
  choices = 1
  new_x = -1
  new_y = -1
  new_steps = -1
  while choices == 1:
    choices = 0
    if y == map_y:
      if x == map_x -1:
        routes.append(steps[y][x]);
        print "New route, steps: " + str(steps[y][x])
        print "  Best so far: " + str(max(routes))
        return;

    s = steps[y][x] + 1
    if y > 0:
      if (map[y-1][x] == '.' or map[y-1][x] == '^')  and steps[y-1][x] == -1:
        choices += 1
        new_steps = s
        new_x = x
        new_y = y-1
    if y < map_y:
      if (map[y+1][x] == '.' or map[y+1][x] == 'v') and steps[y+1][x] == -1:
        choices += 1
        new_steps = s
        new_x = x
        new_y = y+1
    if x > 0:
      if (map[y][x-1] == '.' or map[y][x-1] == '<') and steps[y][x-1] == -1:
        choices += 1
        new_steps = s
        new_x = x-1
        new_y = y
    if x < map_x:
      if (map[y][x+1] == '.' or map[y][x+1] == '>') and steps[y][x+1] == -1:
        choices += 1
        new_steps = s
        new_x = x+1
        new_y = y
    if choices == 1:
      x = new_x
      y = new_y
      steps[y][x] = new_steps




  if y == map_y:
    if x == map_x -1:
      routes.append(steps[y][x]);
      print "New route, steps: " + str(steps[y][x])
      return;
  if steps[y][x] > -1:
    s = steps[y][x] + 1
    if y > 0:
      if (map[y-1][x] == '.' or map[y-1][x] == '^')  and steps[y-1][x] == -1:
        scopy = copy.deepcopy(steps)
        scopy[y-1][x] = s
        move(scopy, x, y-1, d+1)
    if y < map_y:
      if (map[y+1][x] == '.' or map[y+1][x] == 'v') and steps[y+1][x] == -1:
        scopy = copy.deepcopy(steps)
        scopy[y+1][x] = s
        move(scopy, x, y+1, d+1)
    if x > 0:
      if (map[y][x-1] == '.' or map[y][x-1] == '<') and steps[y][x-1] == -1:
        scopy = copy.deepcopy(steps)
        scopy[y][x-1] = s
        move(scopy, x-1, y, d+1)
    if x < map_x:
      if (map[y][x+1] == '.' or map[y][x+1] == '>') and steps[y][x+1] == -1:
        steps[y][x+1] = s
        scopy = copy.deepcopy(steps)
        scopy[y][x+1] = s
        move(scopy, x+1, y, d+1)
  return

move(copy.deepcopy(steps), 1, 0, 0)


print "PART B: " + str(max(routes))  


  
