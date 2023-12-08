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

starting_nodes = []
results = []

for n in list(map.keys()):
  if n[-1] == 'A':
    starting_nodes.append(n)
    results.append(-1);

steps = 0
finish = 0;

while finish == 0:
  for d in dirs:
    steps += 1;
    if d == 'L':
      for i in range(0, len(starting_nodes)):
        starting_nodes[i] = map[starting_nodes[i]][0]
    else:
      for i in range(0, len(starting_nodes)):
        starting_nodes[i] = map[starting_nodes[i]][1]

    finish = 1;

    for i in range(0, len(starting_nodes)):
      if starting_nodes[i][-1] == 'Z' and results[i] == -1:
        results[i] = steps;

    for x in results:
      if x == -1:
        finish = 0;


# Calculate Lowest Common Multiple

z = 0
startloop = 1000000;
loop = startloop
finish = 0;
while finish == 0:
  z += max(results)
  
  finish = 1
  for i in results:
    if z % i != 0:
      finish = 0;

  loop -= 1;
  if loop == 0:
    #print z
    loop = startloop

print z

print "PART B: " + str(z)
