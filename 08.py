filename = '08_in.txt';

map = {}

first = 1;
dirs = []

with open(filename) as f:
  for l in f:
    if first == 1:
      for d in l.strip():
        dirs.append(d)
      first = 0
    else:
      if len(l) <2:
        continue
      node = l.split('=')[0].strip();
      left = l.split('=')[1].strip().split(',')[0].strip();
      left = left.replace("(","").strip();
      right = l.split('=')[1].strip().split(',')[1].strip();
      right = right.replace(")","").strip();
      pair = [];
      pair.append(left);
      pair.append(right);
      map[node] = pair;

node = 'AAA'
steps = 0

while node != 'ZZZ':
  for d in dirs:
    steps += 1;
    if d == 'L':
      node = map[node][0]
    else:
      node = map[node][1]

print "PART A: " + str(steps)


