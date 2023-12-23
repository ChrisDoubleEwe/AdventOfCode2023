import copy
filename = '22_in.txt';

bricks = []
with open(filename) as f:
  for l in f:
    b = l.strip().split('~');
    p1 = []
    p2 = []
    for c in b[0].split(','):
      p1.append(int(c))
    for c in b[1].split(','):
      p2.append(int(c))
    pair = []
    pair.append(list(p1))
    pair.append(list(p2))
    bricks.append(list(pair))


blist = ['A','B','C','D','E','F','G']
supported_by = []
supports = []
empty_list = []
falling = 1;
for b in bricks:
  supported_by.append(list(empty_list))
  supports.append(list(empty_list))

while falling == 1:
  falling = 0;

  bindex = -1
  for b in bricks:
    bindex += 1

    # If lowest z is 1, we're already grounded
    if b[0][2] == 1 or b[1][2] == 1:
      continue

    bx_start = b[0][0]
    by_start = b[0][1]
    bz_start = b[0][2]
    bx_end = b[1][0]
    by_end = b[1][1]
    bz_end = b[1][2]

    zindex = -1
    highest_support = 0
    for z in bricks:
      zindex += 1
      zx_start = z[0][0]
      zy_start = z[0][1]
      zz_start = z[0][2]
      zx_end = z[1][0]
      zy_end = z[1][1]
      zz_end = z[1][2]
      if zindex == bindex:
        continue

      # Is B supported by Z? 
      sup = 0
      if zx_start <= bx_end and zx_end >= bx_start:
        if zy_start <= by_end and zy_end >= by_start:
          if bz_start > zz_end and bz_end > zz_end:
            sup = 1
      if sup == 1:
        if zz_end > highest_support:
          highest_support = zz_end
    if bindex == 278:
      print "highest_support = " + str(highest_support)
      print "sup = " + str(sup)

    if highest_support+1 < bz_start:
      brick_height = bz_end - bz_start
      bricks[bindex][0][2] = highest_support+1
      bricks[bindex][1][2] = highest_support+1+brick_height
      falling = 1
 
bindex = -1
for b in bricks:
  bindex += 1
  bz_start = b[0][2]
  bz_end = b[1][2]
  print str(bindex) + " : z_start " +  str(bz_start)



# WORK OUT SUPPORTS
bindex = -1
for b in bricks:
  bindex += 1

  # If lowest z is 1, we're already grounded

  bx_start = b[0][0]
  by_start = b[0][1]
  bz_start = b[0][2]
  bx_end = b[1][0]
  by_end = b[1][1]
  bz_end = b[1][2]

  zindex = -1
  for z in bricks:
    zindex += 1
    zx_start = z[0][0]
    zy_start = z[0][1]
    zz_start = z[0][2]
    zx_end = z[1][0]
    zy_end = z[1][1]
    zz_end = z[1][2]
    if zindex == bindex:
      continue

    # Is B supported by Z?
    sup = 0
    if zx_start <= bx_end and zx_end >= bx_start:
      if zy_start <= by_end and zy_end >= by_start:
        if bz_start == zz_end+1:
          sup = 1
    if sup == 1:
      supported_by[bindex].append(zindex)
      supports[zindex].append(bindex)



    
# Count how many bricks are supported by each individual brick
dis = 0
dis_count = 0
bindex = -1
for b in bricks:
  bindex += 1
  print ""
  print "Brick " + str(bindex) + " supports: " + str(supports[bindex])
  if len(supports[bindex]) == 0:
    print "Brick " + str(bindex) + " can be removed (no other bricks rely on it)"
    dis += 1
  else:
    supported_by_others = 0
    print "  This brick supports supports[bindex]=" + str(supports[bindex])
    for i in supports[bindex]:
      print "    One of those supports is supported_by[i]=" + str(supported_by[i])
      if len(supported_by[i]) > 1:
        print "     (supported by another brick)"
        supported_by_others += 1
    if supported_by_others == len(supports[bindex]):
      print "Brick " + str(bindex) + " can be removed (supported by others)"
      dis += 1
    else:
      print "supported_by_others=" + str(supported_by_others)
      continue 
  if dis > 0:
    dis_count+=1

    

print "PART A: " + str(dis_count)
