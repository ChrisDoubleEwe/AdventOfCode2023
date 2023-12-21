import copy
filename = '20_in.txt';

broadcaster = []
net = {}
# net[0] = type
# net[1] = outputs list
# net[2] = state
# net[3] = inputs

with open(filename) as f:
  for l in f:
    if 'broadcaster' in l:
      for c in l.split('>')[1].strip().split(','):
        broadcaster.append(c.strip())
    else:
      type = l[0]
      name = l.split(' ')[0][1:]
      outs = []
      for o in l.split('>')[1].strip().split(','):
        outs.append(o.strip())
      val = [];
      val.append(type)
      val.append(outs)
      val.append(0)
      ins = []
      val.append(ins)
      net[name] = copy.deepcopy(val)
queue = []

# Work out connected inputs
for c in net.keys():
  if net[c][0] == '&':
    inputs = []
    for z in net.keys():
      if c in net[z][1]:
        inputs.append(z)
    net[c][3] = copy.deepcopy(inputs);

for c in net.keys():
  if net[c][0] == '&':
    states = []
    for z in net[c][3]:
      states.append(0)
    net[c][2] = copy.deepcopy(states);

lo_pulses = 0
hi_pulses = 0

def push_button():
  global lo_pulses
  global hi_pulses

  action=['broadcast', 0, '']
  queue.append(list(action))

  while len(queue) > 0:
    #print queue

    a = queue.pop(0);
    if a[1] == 1:
      hi_pulses += 1;
    else:
      lo_pulses += 1;

    # BROADCAST
    if a[0] == 'broadcast':
      for c in broadcaster:
        x = []
        x.append(c)
        x.append(0)
        x.append('broadcast')
        queue.append(list(x))
      continue;

    # DEAL WITH UNCONNECTED OUTPUTS
    if a[0] not in net.keys():
      continue;

    # FLIP FLOP
    if net[a[0]][0] == '%':
      if a[1] > 0:
        continue
      if net[a[0]][2] == 1:
        net[a[0]][2] = 0;
      else:
        net[a[0]][2] = 1;
      for c in net[a[0]][1]:
        x = []
        x.append(c)
        x.append(net[a[0]][2])
        x.append(a[0])
        queue.append(list(x))

    # CONJUNCTION
    if net[a[0]][0] == '&':
      f = a[2];
      pulse = a[1]
      fidx = net[a[0]][3].index(f);
      net[a[0]][2][fidx] = pulse
      if min(net[a[0]][2]) == 1:
        for c in net[a[0]][1]:
          x = []
          x.append(c)
          x.append(0)
          x.append(a[0])
          queue.append(list(x))
      else:
        for c in net[a[0]][1]:
          x = []
          x.append(c)
          x.append(1)
          x.append(a[0])
          queue.append(list(x))

  
for i in range(0, 1000):
  push_button()    


 
    
  

print "lo_pulses: " + str(lo_pulses)
print "hi_pulses: " + str(hi_pulses)
parta = lo_pulses * hi_pulses
print "PART A: " + str(parta)
 
