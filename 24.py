import copy
import numpy as np 

filename = '24_in.txt';

points = []
with open(filename) as f:
  for l in f:
    line = l.strip().split(' @ ')
    px = line[0].strip().split(', ')[0].strip() 
    py = line[0].strip().split(', ')[1].strip()
    pz = line[0].strip().split(', ')[2].strip()
    vx = line[1].strip().split(', ')[0].strip()
    vy = line[1].strip().split(', ')[1].strip()
    vz = line[1].strip().split(', ')[2].strip()

    p = []
    p.append(float(px))
    p.append(float(py))
    p.append(float(pz))
    p.append(float(vx))
    p.append(float(vy))
    p.append(float(vz))

    points.append(list(p))


min = 200000000000000
max = 400000000000000
#min = 7
#max = 27

parta = 0
seen = []
p1_index = -1
for p1 in points:
  p1_index += 1
  p1_px = p1[0]
  p1_py = p1[1]
  p1_pz = p1[2]
  p1_vx = p1[3]
  p1_vy = p1[4]
  p1_vz = p1[5]

  # At min Y boundary, what is order in X dimension
  t1y_min = (min -  p1_py) / (p1_vy )
  t1y_max = (max -  p1_py) / (p1_vy )
  x1_min = p1_px + (p1_vx * t1y_min)
  x1_max = p1_px + (p1_vx * t1y_max)

  t1x_min = (min -  p1_px) / (p1_vx )
  t1x_max = (max -  p1_px) / (p1_vx )
  y1_min = p1_py + (p1_vy * t1x_min)
  y1_max = p1_py + (p1_vy * t1x_max)


  p2_index = -1
  for p2 in points:
    p2_index += 1
    if p2_index < p1_index:
      key = "++"+str(p2_index)+"--"+str(p1_index)+"++"
    else:
      key = "++"+str(p1_index)+"--"+str(p2_index)+"++"

    if key in seen:
      continue
    seen.append(key)
    if p1 == p2:
      continue

    p2_px = p2[0]
    p2_py = p2[1]
    p2_pz = p2[2]
    p2_vx = p2[3]
    p2_vy = p2[4]
    p2_vz = p2[5]

    # AT WHAT TIME DO  COORDS CROSS?
    # Hailstone A: 19, 13, 30 @ -2, 1, -2
    # Hailstone B: 18, 19, 22 @ -1, -1, -2
    # 19 + (-2 x t1) = 18 + (-1 x t2)
    # 19 -2a = 18 -b ; 13 + a = 19 -b 
    #
    # p1_px + (p1_vx * t1) = p2_px + (p2_vx * t2)
    # (p1_vx * t1) - (p2_vx * t2) = p2_px - p1_px
    # (p1_vy * t1) - (p2_vy * t2) = p2_py - p1_py
    A = np.array([[p1_vx,(0-p2_vx)], [p1_vy,(0-p2_vy)]])
    B = np.array([(p2_px - p1_px),(p2_py - p1_py)])
    print A
    print B
    try:
      C = np.linalg.solve(A, B)
    except np.linalg.LinAlgError as err:
      if 'Singular matrix' in str(err):
        print "PARALLEL"
        continue;
    print(C)
    t1 = C[0]
    t2 = C[1]
    if t1 < 0 or t2 < 0:
      print "IN THE PAST"
      continue


    cross_x = p1_px + (p1_vx * t1)
    cross_y = p1_py + (p1_vy * t1)
    print "Cross at x=" + str(cross_x) + " ; y=" + str(cross_y)
    if (min <= cross_x <= max) and (min <= cross_y <= max):
      parta += 1


print "PART A: " + str(parta)
