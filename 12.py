from copy import copy, deepcopy
filename = '12_in.txt';


parta = 0;

def calc(s):
  res = ''

  counting = 0
  count = 0
  for c in s:
    if c == '.':
      if counting == 0:
        continue;
      else:
        res += str(count) + ','
        count = 0;
        counting = 0;
        continue;
    else:
      if counting == 1:
        count += 1;
      else:
        counting = 1;
        count = 1;
  if counting == 1:
    res += str(count) + ','
  return res[:-1]

count = -1
with open(filename) as f:
  for l in f:
    count += 1
    print "Line: " + str(count)
    row=l.strip().split(' ');

    poss = []
    poss.append(row[0])


    loop = 1
    while loop == 1:
      new_poss = []
      for p in poss:
        new0 = p.replace('?','#',1);
        new1 = p.replace('?','.',1);
        new_poss.append(new0);
        new_poss.append(new1);

      poss = list(new_poss);

      loop = 0;

      for p in poss:
        if '?' in p:
          loop = 1


    count_ways = 0
    for p in poss:
      r = calc(p);
      if r == row[1]:
        count_ways += 1
        
    parta += count_ways

print "PART A: " + str(parta)
