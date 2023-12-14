import copy
filename = '13_in.txt';

parta = 0;

maps = [];
map = []
first = 1
prev = ''
potentials = []

with open(filename) as f:
  for l in f:
    if l.strip() == '':
      temp = copy.deepcopy(map);
      maps.append(temp);
      map = [];
      continue

    row = []
    for c in l.strip():
      row.append(c);
    map.append(list(row))

temp = copy.deepcopy(map);
maps.append(temp);



for m in maps:
  first = 1;
  prev = '' 
  count = -1;
  pots = [];
  for row in m:
    count += 1;
    if first == 1:
      prev = list(row);
      first = 0;
      continue;
    pots.append(count);
    prev = list(row);
  potentials.append(copy.deepcopy(pots));

remember_maps = copy.deepcopy(maps);

count = -1;
for pots in potentials:
  count +=1 ;
  diff_pot = -1
  for p in pots:
    test_u = p;
    test_d = p-1;
    ok = 1
    all_diffs = 0;
    diff_i = -1;
    diff_d = -1
    diff_row = 0;

    while (test_d >=0 and test_u < len(maps[count])):
      if maps[count][test_u] != maps[count][test_d]:
        diffs = 0;
        for i in range(0, len(maps[count][test_u])):
          if maps[count][test_u][i] != maps[count][test_d][i]:
            diffs += 1
            diff_row = test_u;
            diff_i = i;
            diff_d = test_d
            diff_p = p
        all_diffs += diffs
      test_d -= 1;
      test_u += 1;
    if all_diffs == 1:
      diff_pot = diff_p
      if maps[count][diff_row][diff_i] == '#':
        maps[count][diff_row][diff_i] = '.'
      else:
        maps[count][diff_row][diff_i] = '#'
      break;


  test_u = diff_pot;
  test_d = diff_pot-1;
  ok = 1
  while (test_d >=0 and test_u < len(maps[count])):
    if maps[count][test_u] != maps[count][test_d]:
      ok = 0;
      break;
    test_d -= 1;
    test_u += 1;
  if ok == 1 and diff_pot >= 0:
    print "Map " + str(count) + " has vertical reflection at line " + str(diff_pot)
    parta += (100 * diff_pot)


# ROTATE MAPS
new_maps = []
for m in remember_maps:
  new_map = []
  for i in range(0, len(m[0])):
    row = []
    for j in range(0, len(m)):
      row.append(m[j][i]);
    new_map.append(list(row))
  new_maps.append(copy.deepcopy(new_map));


maps = copy.deepcopy(new_maps);

potentials = []

for m in maps:
  first = 1;
  prev = ''
  count = -1;
  pots = [];
  for row in m:
    count += 1;
    if first == 1:
      prev = list(row);
      first = 0;
      continue;
    pots.append(count);
    prev = list(row);
  potentials.append(copy.deepcopy(pots));

count = -1;
for pots in potentials:
  count +=1 ;

  diff_pot = -1
  for p in pots:
    test_u = p;
    test_d = p-1;
    ok = 1
    all_diffs = 0;
    diff_i = -1;
    diff_row = 0;
    diff_d = -1;
    diff_p = -1

    while (test_d >=0 and test_u < len(maps[count])):
      if maps[count][test_u] != maps[count][test_d]:
        diffs = 0;
        for i in range(0, len(maps[count][test_u])):
          if maps[count][test_u][i] != maps[count][test_d][i]:
            diffs += 1
            diff_row = test_u;
            diff_d = test_d;
            diff_i = i;
            diff_p = p
        all_diffs += diffs
      test_d -= 1;
      test_u += 1;
    if all_diffs == 1:
      diff_pot = diff_p

      if maps[count][diff_row][diff_i] == '#':
        maps[count][diff_row][diff_i] = '.'
      else:
        maps[count][diff_row][diff_i] = '#'
      break;


  test_u = diff_pot;
  test_d = diff_pot-1;
  ok = 1
  while (test_d >=0 and test_u < len(maps[count])):
    if maps[count][test_u] != maps[count][test_d]:
      ok = 0;
      break;
    test_d -= 1;
    test_u += 1;
  if ok == 1 and diff_pot >=0:
    print "Map " + str(count) + " has horizontal reflection at line " + str(diff_pot)
    parta +=  diff_pot

print "PART B: " + str(parta)

      

