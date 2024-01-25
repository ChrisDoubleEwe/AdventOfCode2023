import copy
filename = '18_in.txt';

map = []

dirs_partb = []
dirs_parta = []


with open(filename) as f:
  for l in f:
    all_line = l.strip()
    a = all_line.split(' ');
    if a[0] == 'R':
      a_dir = 0
    if a[0] == 'D':
      a_dir = 1
    if a[0] == 'L':
      a_dir = 2
    if a[0] == 'U':
      a_dir = 3
    a_dist = int(a[1])
    a_pair = []
    a_pair.append(a_dist)
    a_pair.append(a_dir)

    lin = all_line.split('#')[1]
    line = lin.replace(')','')
    dir = int(line[-1])
    print dir
    dis = line[0:-1]
    print dis
    dist = int(dis, 16)
    print dist
    pair = []
    pair.append(dist)
    pair.append(dir)
    dirs_partb.append(list(pair))
    dirs_parta.append(list(a_pair))
    print all_line
    print pair


dirs = []
dirs = dirs_partb
perimeter = 0
for d in dirs:
  perimeter += d[0]

x = 100
y = 100

xs = []
ys = []
xs.append(0);
ys.append(0);

for p in dirs:
  if p[1] == 0: 
    x+=p[0]
  if p[1] == 2: 
    x-=p[0]
  if p[1] == 1: 
    y+=p[0]
  if p[1] == 3: 
    y-=p[0]

  xs.append(x)
  ys.append(y)

area = 0
triangle_area = 0
xs.reverse()
ys.reverse()

n = len(xs)-1;
for i in range(0, n):
  print 
  j = i+1
  if j > n-1:
    j = 0
  print "*******"
  print "i = " + str(i) + " ; j = " + str(j) + " ; n = " + str(n)
  print "x[i]=" + str(xs[i]) + ", y[i]=" + str(ys[i]) + "   ;   x[j]=" + str(xs[j]) + ", y[j]=" + str(ys[j]) 
  #print xs[i]
  #print ys[i]
  #print "----"
  this_area = (ys[i] + ys[j]) * (xs[i] - xs[j])
  triangle_area += ((xs[i] * ys[j]) - (xs[j] * ys[i]))
  area += this_area

area = 0.5*area
triangle_area = 0.5*(triangle_area)

if area < 0:
  area = 0 - area
if triangle_area < 0:
  triangle_area = 0 - triangle_area

area = area + (perimeter / 2 ) + 1
triangle_area = triangle_area + (perimeter / 2 ) + 1



print "= PART B using TRAPEZOID FORMULA ======="
print (int(triangle_area))
print "========"

print "= PART B using TRIANGLE FORMULA ======="
print (int(triangle_area))
print "========"


  


