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


for x in maps:
  print "------"
  for y in x:
    print y
  


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
    if row == prev:
      pots.append(count);
    prev = list(row);
  potentials.append(copy.deepcopy(pots));

print potentials

count = -1;
for pots in potentials: 
  count +=1 ;
  for p in pots:
    test_u = p;
    test_d = p-1;
    ok = 1
    while (test_d >=0 and test_u < len(maps[count])):
      if maps[count][test_u] != maps[count][test_d]:
        ok = 0;
        break;
      test_d -= 1;
      test_u += 1;
    if ok == 1:
      print "Map " + str(count) + " has vertical reflection at line " + str(p)
      parta += (100 * p)

      




# ROTATE MAPS
new_maps = []
for m in maps:
  new_map = []
  for i in range(0, len(m[0])):
    row = []
    for j in range(0, len(m)):
      row.append(m[j][i]);
    new_map.append(list(row))
  new_maps.append(copy.deepcopy(new_map));
      
print "======"
for n in new_maps:
  print "-----"
  for x in n:
    print x


potentials = []
for m in new_maps:
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
    if row == prev:
      pots.append(count);
    prev = list(row);
  potentials.append(copy.deepcopy(pots));

print potentials

count = -1;
for pots in potentials:
  count +=1 ;
  print "Doing map: " + str(count)
  for p in pots:
    test_u = p;
    test_d = p-1;
    ok = 1
    while (test_d >=0 and test_u < len(new_maps[count])):
      if new_maps[count][test_u] != new_maps[count][test_d]:
        ok = 0;
        break;
      test_d -= 1;
      test_u += 1;
    if ok == 1:
      print "Map " + str(count) + " has horizontal reflection at line " + str(p)
      parta += (p)


print "PART A: " + str(parta)
