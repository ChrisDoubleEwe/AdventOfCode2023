import copy
filename = '15_in.txt';

def calc(s):
  val = 0;
  for c in s:
    val += ord(c);
    val = val * 17;
    val = val % 256
  return val;

parta = 0;

with open(filename) as f:
  for l in f:
    for c in l.strip().split(','):
      res = calc(c)
      parta += res

print "PART A: " + str(parta)

box = {}

with open(filename) as f:
  for l in f:
    for c in l.strip().split(','):
      label = ''
      lens = -1;
      op = -1;
      
      if '=' in c:
        op = 1
        label = c.split('=')[0];
        lens = int(c.split('=')[1]);
      else:
        op = 0
        label = c.split('-')[0];
        
      box_num = calc(label)

      if op == 1: # EQUALS
        if box_num not in box.keys():
          new_list = []
          pair=[]
          pair.append(label)
          pair.append(lens)
          new_list.append(list(pair))
          box[box_num] = list(new_list)
        else:
          lens_list = box[box_num]
          found = 0
          for l in lens_list:
            if l[0] == label:
              l[1] = lens
              found = 1;
          if found == 0:
            pair = []
            pair.append(label)
            pair.append(lens)
            box[box_num].append(list(pair))
      else:  # MINUS
        if box_num in box.keys():
          new_box = []
          lens_list = box[box_num]
          for l in lens_list:
            if l[0] != label:
              new_box.append(l)
          box[box_num] = copy.deepcopy(new_box)


        
# CALC RESULT
partb = 0
for box_num in box.keys():
  slot = 0
  for l in box[box_num]:
    slot += 1
    fp = (int(box_num) + 1) *  slot * l[1]
    partb += fp

print "PART B: " + str(partb)



