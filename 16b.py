import copy
filename = '16_in.txt';

id = 0;

map = []
map_act = []

def print_map_act():
  for row in map_act:
    r = ''
    for c in row:
      r+=c
    print r

with open(filename) as f:
  for l in f:
    row = [];
    row_act = [];
    for c in l.strip():
      if c != "\\" and c != '.' and c != '-' and c != '|':
        c = 'f'
      if c == '\\':
        c = 'b'
      row.append(c);
      row_act.append(' ');
    map.append(list(row));
    map_act.append(list(row_act));

possibles = []
map_x = len(map[0])-1;
map_y = len(map)-1;

for x in range(0, map_x):
  poss = []
  poss.append(-1)
  poss.append(x)
  poss.append('s')
  possibles.append(list(poss))
  poss = []
  poss.append(map_y+1)
  poss.append(x)
  poss.append('n')
  possibles.append(list(poss))

for y in range(0, map_y):
  poss = []
  poss.append(y)
  poss.append(-1)
  poss.append('e')
  possibles.append(list(poss))
  poss = []
  poss.append(y)
  poss.append(map_x+1)
  poss.append('w')
  possibles.append(list(poss))

poss = []
poss.append(-1)
poss.append(-1)
poss.append('s')
possibles.append(list(poss))
poss = []
poss.append(-1)
poss.append(-1)
poss.append('e')
possibles.append(list(poss))

poss = []
poss.append(-1)
poss.append(map_x+1)
poss.append('s')
possibles.append(list(poss))
poss = []
poss.append(-1)
poss.append(map_x+1)
poss.append('w')
possibles.append(list(poss))

poss = []
poss.append(map_y+1)
poss.append(-1)
poss.append('n')
possibles.append(list(poss))
poss = []
poss.append(map_y+1)
poss.append(-1)
poss.append('e')
possibles.append(list(poss))

poss = []
poss.append(map_y+1)
poss.append(map_x+1)
poss.append('n')
possibles.append(list(poss))
poss = []
poss.append(map_y+1)
poss.append(map_x+1)
poss.append('w')
possibles.append(list(poss))





empty_map = copy.deepcopy(map_act)

partb = -1

for po in possibles:
 map_act = copy.deepcopy(empty_map)
 print "Trying..."
 print po
 p = []
 p.append(po[0])
 p.append(po[1])
 p.append(po[2])
 p.append(id)
 id+=1;
 #map_act[p[0]][p[1]] = '#'

 parts = []
 parts.append(p)

 last_acts = -1;
 final_countdown = 100000

 splits = [];

 while len(parts) > 0 and final_countdown > 0:
  #map_act = []
  #for row in map:
  #  map_act.append(list(row))

  final_countdown -= 1;

  num_acts = 0
  for row in map_act:
    for c in row:
      if c == '#':
        num_acts += 1
  if num_acts != last_acts:
    last_acts = num_acts
    final_countdown = 1000




  for p in parts:
    if p[2] == 'e':
      mod_x = 1;
      mod_y = 0;
    if p[2] == 'w':
      mod_x = -1;
      mod_y = 0;
    if p[2] == 's':
      mod_x = 0;
      mod_y = 1;
    if p[2] == 'n':
      mod_x = 0;
      mod_y = -1;


    if p[0]+mod_y < 0:
      parts.remove(p);
      continue;
    if p[0]+mod_y > map_y:
      parts.remove(p);
      continue;
    if p[1]+mod_x < 0:
      parts.remove(p);
      continue;
    if p[1]+mod_x > map_x:
      parts.remove(p);
      continue;

    if map[p[0]+mod_y][p[1]+mod_x] == '.':
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      map_act[p[0]][p[1]]='#'
      continue;
    if map[p[0]+mod_y][p[1]+mod_x] == 'f':
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x

      split_add = list(p[:-1])
      if split_add not in splits:
        splits.append(list(split_add));
        if mod_x == 1:
          p[2] = 'n'
        if mod_x == -1:
          p[2] = 's'
        if mod_y == 1:
          p[2] = 'w'
        if mod_y == -1:
          p[2] = 'e'
      else:
        parts.remove(p)
      map_act[p[0]][p[1]]='#'
      continue;
    if map[p[0]+mod_y][p[1]+mod_x] == 'b':
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      split_add = list(p[:-1])
      if split_add not in splits:
        splits.append(list(split_add));
        if mod_x == 1:
          p[2] = 's'
        if mod_x == -1:
          p[2] = 'n'
        if mod_y == 1:
          p[2] = 'e'
        if mod_y == -1:
          p[2] = 'w'
      else:
        parts.remove(p)
      map_act[p[0]][p[1]]='#'
      continue;
    if map[p[0]+mod_y][p[1]+mod_x] == '-' and mod_x != 0:
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      map_act[p[0]][p[1]]='#'
      continue;
    if map[p[0]+mod_y][p[1]+mod_x] == '|' and mod_y != 0:
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      map_act[p[0]][p[1]]='#'
      continue;
    if map[p[0]+mod_y][p[1]+mod_x] == '-' and mod_x == 0:
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      split_add = list(p[:-1])
      if split_add not in splits:
        splits.append(list(split_add));
        p[2] = 'e'
        new_p = list(p)
        new_p[2] = 'w'
        new_p[3] = id;
        id += 1;
        parts.append(list(new_p));
      else:
        parts.remove(p)
      map_act[p[0]][p[1]]='#'
      continue
    if map[p[0]+mod_y][p[1]+mod_x] == '|' and mod_y == 0:
      p[0] = p[0] + mod_y
      p[1] = p[1] + mod_x
      split_add = list(p[:-1])
      if split_add not in splits:
        splits.append(list(split_add));
        map_act[p[0]][p[1]]='#'
        p[2] = 'n'
        new_p = list(p)
        new_p[2] = 's'
        new_p[3] = id;
        id += 1;
        parts.append(list(new_p));
      else:
        parts.remove(p)
      map_act[p[0]][p[1]]='#'
      continue
  
 this_res = 0
 for row in map_act:
   for c in row:
     if c == '#':
       this_res += 1

 print this_res
 #print_map_act()
 if this_res > partb:
   partb = this_res

print "PART B: " + str(partb)










