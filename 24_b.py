import copy
import numpy as np 
from collections import Counter
resx = 0
resy = 0
resz = 0

filename = '24_in.txt';

 
def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]


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


min = -400000000000000
max = 400000000000000
#min = 7
#max = 27


n = 300
if n > 1:
  for rock_x in range(0-n, n):
   for rock_y in range(0-n, n):

    #print "ROCK X = " + str(rock_x) + "  Y= " + str(rock_y)

    parta = 0
    seen = []
    p1_index = -1


    crossings = []
    actualx = []
    actualy = []



    for p1 in points:
      if len(crossings) > 1:
        break

      p1_index += 1
      p1_px = p1[0]
      p1_py = p1[1]
      p1_pz = p1[2]
      p1_vx = p1[3] - rock_x
      p1_vy = p1[4] - rock_y
      p1_vz = p1[5]

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
        p2_vx = p2[3] - rock_x
        p2_vy = p2[4] - rock_y
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
        #print A
        #print B
        try:
          C = np.linalg.solve(A, B)
        except np.linalg.LinAlgError as err:
          if 'Singular matrix' in str(err):
            #print "PARALLEL"
            continue;
        #print(C)
        t1 = C[0]
        t2 = C[1]
        if t1 <= 0 or t2 <= 0:
          #print "IN THE PAST"
          continue


        cross_x_actual = int((p1_px + (p1_vx * t1)))
        cross_y_actual = int((p1_py + (p1_vy * t1)))

        cross_x = int((p1_px + (p1_vx * t1))/10000)
        cross_y = int((p1_py + (p1_vy * t1))/10000)
        #print "Cross at x=" + str(cross_x) + " ; y=" + str(cross_y)
        parta += 1
        pair = []
        pair.append(cross_x)
        pair.append(cross_y)
        if pair not in crossings:
          crossings.append(copy.deepcopy(pair))
        actualx.append(cross_x_actual)
        actualy.append(cross_y_actual)

        if len(crossings) > 1:
          break

    if len(crossings) == 1:
      print "Rock_x = " + str(rock_x) + " ; Rock_y = " + str(rock_y) + " ; crossings = " + str(parta)
      resx = most_frequent(actualx)
      resy = most_frequent(actualy)



n = 300
if n > 1:
  for rock_x in range(0-n, n):
   for rock_z in range(0-n, n):


    parta = 0
    seen = []
    p1_index = -1


    crossings = []
    actualx = []
    actualz = []



    for p1 in points:
      if len(crossings) > 1:
        break

      p1_index += 1
      p1_px = p1[0]
      p1_py = p1[1]
      p1_pz = p1[2] 
      p1_vx = p1[3] - rock_x
      p1_vy = p1[4] 
      p1_vz = p1[5] - rock_z

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
        p2_vx = p2[3] - rock_x
        p2_vy = p2[4]
        p2_vz = p2[5] - rock_z

        # AT WHAT TIME DO  COORDS CROSS?
        # Hailstone A: 19, 13, 30 @ -2, 1, -2
        # Hailstone B: 18, 19, 22 @ -1, -1, -2
        # 19 + (-2 x t1) = 18 + (-1 x t2)
        # 19 -2a = 18 -b ; 13 + a = 19 -b 
        #
        # p1_px + (p1_vx * t1) = p2_px + (p2_vx * t2)
        # (p1_vx * t1) - (p2_vx * t2) = p2_px - p1_px
        # (p1_vy * t1) - (p2_vy * t2) = p2_py - p1_py
        A = np.array([[p1_vx,(0-p2_vx)], [p1_vz,(0-p2_vz)]])
        B = np.array([(p2_px - p1_px),(p2_pz - p1_pz)])
        #print A
        #print B
        try:
          C = np.linalg.solve(A, B)
        except np.linalg.LinAlgError as err:
          if 'Singular matrix' in str(err):
            #print "PARALLEL"
            continue;
        #print(C)
        t1 = C[0]
        t2 = C[1]
        if t1 <= 0 or t2 <= 0:
          #print "IN THE PAST"
          continue


        cross_x_actual = int((p1_px + (p1_vx * t1)))
        cross_z_actual = int((p1_pz + (p1_vz * t1)))

        cross_x = int((p1_px + (p1_vx * t1))/10000)
        cross_z = int((p1_pz + (p1_vz * t1))/10000)
        #print "Cross at x=" + str(cross_x) + " ; y=" + str(cross_y)
        parta += 1
        pair = []
        pair.append(cross_x)
        pair.append(cross_z)
        if pair not in crossings:
          crossings.append(copy.deepcopy(pair))
        actualx.append(cross_x_actual)
        actualz.append(cross_z_actual)

        if len(crossings) > 1:
          break

    if len(crossings) == 1:
      print "Rock_x = " + str(rock_x) + " ; Rock_y = " + str(rock_y) + " ; crossings = " + str(parta)
      print "Z"
      resz = most_frequent(actualz)


      print "X: " + str(resx)
      print "Y: " + str(resy)
      print "Z: " + str(resz)
      total = resx + resy + resz
      print "RESULT: " + str(total)


      exit()


