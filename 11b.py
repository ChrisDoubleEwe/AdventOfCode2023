from copy import copy, deepcopy
filename = '11_in.txt';
partb = 0


map = []

def print_map():
  for row in map:
    r = ''
    for c in row:
      r+=c 
    print r

empty_rows = [];

row_count = -1;
with open(filename) as f:
  for l in f:
    row_count += 1;
    row = []
    for c in l.strip(): 
      row.append(c);
    map.append(list(row));
    if '#' not in row:
      empty_rows.append(row_count);

empty_cols = [];

for i in range(0, (len(map[0]))):
  no_gals = 0;
  for m in map:
    if m[i] == '#':
      no_gals = 1
  if no_gals == 0:
    empty_cols.append(i)

empty_cols.reverse()
empty_rows.reverse()

points = []
for x in range(0, len(map[0])):
  for y in range(0, len(map)):
    if map[y][x] == '#':
      pair = []
      pair.append(y);
      pair.append(x);
      points.append(pair);


inc = 1000000;
inc -= 1;

for y in empty_rows:
  for p in points:
    if p[0] > y:
      p[0] += inc

for x in empty_cols:
  for p in points:
    if p[1] > x:
      p[1] += inc


dists = {}
for p1 in points:  
  for p2 in points:
    if p1 == p2:
      continue

    if p1[0] < p2[0]:
      key = '++'+str(p1[0])+'_'+str(p1[1])+'--'+str(p2[0])+'_'+str(p2[1])+'++'
    else:
      if p1[0] > p2[0]:
        key = '++'+str(p2[0])+'_'+str(p2[1])+'--'+str(p1[0])+'_'+str(p1[1])+'++'
      else:
        if p1[1] < p2[1]:
          key = '++'+str(p1[0])+'_'+str(p1[1])+'--'+str(p2[0])+'_'+str(p2[1])+'++'
        else:
          key = '++'+str(p2[0])+'_'+str(p2[1])+'--'+str(p1[0])+'_'+str(p1[1])+'++'



    dist = 0;
    if p1[0] > p2[0]:
      dist += p1[0] - p2[0];
    else:
      dist += p2[0] - p1[0];
    if p1[1] > p2[1]:
      dist += p1[1] - p2[1];
    else:
      dist += p2[1] - p1[1];

    dists[key] = dist



partb = 0
for d in dists.keys():
  partb += dists[d]

print "PART B: " + str(partb)
