import copy
filename = '25_in.txt';

net = []
with open(filename) as f:
  for l in f:
    line = l.strip().split(': ')
    fr = line[0]
    to = line[1]
    for t in to.strip().split(' '):
      pair = []
      pair.append(fr)
      pair.append(t)
      net.append(list(pair))

print "Read net"
all_comps = []
for p in net:
  if p[0] not in all_comps:
    all_comps.append(p[0])
  if p[1] not in all_comps:
    all_comps.append(p[1])

comp_count = len(all_comps)
print "Identified " + str(comp_count) + " components"

net_copy = copy.deepcopy(net)


node_groups = []
empty_list = []
for c in all_comps:
  node_groups.append(list(empty_list))

net_travel_count = []
for n in net:
  net_travel_count.append(0)

cindex = -1
for c in all_comps:
  cindex += 1
  print str(cindex) + " / " + str(len(all_comps)-1)


  if node_groups[cindex] != []:
    continue
  nodes = []
  nodes.append(c)
  last_len = -1
  while len(nodes) > last_len:
    last_len = len(nodes)
    for n in nodes:
      zindex = -1
      for z in net:
        zindex += 1
        if z[0] == n or z[1] == n:
          if z[0] not in nodes:
            nodes.append(z[0])
            net_travel_count[zindex]+= 1
          if z[1] not in nodes:
            nodes.append(z[1])
            net_travel_count[zindex]+= 1
  nodes.sort()
  node_groups[cindex] = copy.deepcopy(nodes)

removable = []
print "============"
m = max(net_travel_count)
while m > max(net_travel_count)*.5:
  zindex = -1
  for z in net:
    zindex += 1
    if net_travel_count[zindex] == m:
      print str(z) + " : " + str(net_travel_count[zindex])
      removable.append(z)
  m -=1

net_copy = copy.deepcopy(net)

print "Removing connections..."


for n1 in removable:
  for n2 in removable:
    for n3 in removable:
      if n1 == n2 or n2 == n3 or n3 == n1:
        continue

      net = copy.deepcopy(net_copy)
      net.remove(n1)
      net.remove(n2)
      net.remove(n3)

      print "  Removing " + str(n1) + " ; " + str(n2) + " ; " + str(n3)


      node_groups = []
      empty_list = []
      for c in all_comps:
        node_groups.append(list(empty_list))

      cindex = -1
      for c in all_comps:
        cindex += 1
        for prev in node_groups:
          if c in prev:
            node_groups[cindex] = copy.deepcopy(prev)
            break

        if node_groups[cindex] != []:
          continue
        nodes = []
        nodes.append(c)
        last_len = -1
        while len(nodes) > last_len:
          last_len = len(nodes)
          for n in nodes:
            for z in net:
              if z[0] == n or z[1] == n:
                if z[0] not in nodes:
                  nodes.append(z[0])
                if z[1] not in nodes:
                  nodes.append(z[1])
        nodes.sort()
        node_groups[cindex] = copy.deepcopy(nodes)

 
      seen = []
      for ng in node_groups:
        if ng not in seen:
          seen.append(copy.deepcopy(ng))

      
      nums = []
      ng_count = len(seen)
      print str(ng_count) + " Component groups:"
      for s in seen:
        print "  " + str(len(s))
        nums.append(len(s))

      if ng_count == 2:
        parta = 1
        for n in nums:
          parta = parta * n

        print "PART A: " + str(parta)
        exit()


  
  
  
