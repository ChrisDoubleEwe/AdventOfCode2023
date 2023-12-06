filename = '06_in.txt';
times = []
dists = []
parta = 1

with open(filename) as f:
  for l in f:
    line = l.strip()
    if "Time" in line:
      timestr = line.split(":")[1].split();
      for t in timestr:
        times.append(int(t));
    if "Distance" in line:
      diststr = line.split(":")[1].split();
      for d in diststr:
        dists.append(int(d));


for i in range(0,len(times)):
  speed = 0;
  ways_to_win = 0;
  for t in range(0, times[i]+1):
    this_dist = speed * (times[i] - t)
    if this_dist > dists[i]:
      ways_to_win += 1;
    speed += 1    
  parta = parta * ways_to_win

print "PART A: " + str(parta)

timestr = ''
diststr = ''
for t in times:
  timestr += str(t)
for d in dists: 
  diststr += str(d)

time = int(timestr)
dist = int(diststr)


speed = 0;
ways_to_win = 0;
for t in range(0, time+1):
  this_dist = speed * (time - t)
  if this_dist > dist:
    ways_to_win += 1;
  speed += 1
partb = ways_to_win

print "PART B: " + str(partb)

