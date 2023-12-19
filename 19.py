import copy
filename = '19_in.txt';

blank = 0
parts = []
rules = {}
with open(filename) as f:
  for l in f:
    if l.strip() == '':
      blank = 1
      continue
    if blank == 1:
      line = l.strip();
      line = line.replace('{','')
      line = line.replace('}','')
      p = line.split(',')
      lst = []
      for x in p:
        lst.append(int(x.split('=')[1]))
      parts.append(list(lst))
  
      
    else:
      name = l.strip().split('{')[0]
      r = l.strip().split('{')[1]
      r = r.replace('}','')
      rules[name] = r.split(',')

total = 0
accepted = 0
for p in parts:
  print "Doing part: " + str(p)
  x=p[0]
  m=p[1]
  a=p[2]
  s=p[3]
  
  flow_name = 'in'
  processing = 1
  while processing == 1:
    print flow_name
    if flow_name == 'A':
      accepted += 1;
      processing = 0;
      total += x;
      total += m;
      total += a;
      total += s;
      break;
    if flow_name == 'R':
      processing = 0;
      break;
    flow = rules[flow_name]
    for r in flow:
      if ":" not in r:
        flow_name = r
        break;
      else:
        test = r.split(':')[0]
        dest = r.split(':')[1]
        result = 0
        if '>' in test:
          if test.split('>')[0] == 'x':
            if x > int(test.split('>')[1]): result = 1
          if test.split('>')[0] == 'm':
            if m > int(test.split('>')[1]): result = 1
          if test.split('>')[0] == 'a':
            if a > int(test.split('>')[1]): result = 1
          if test.split('>')[0] == 's':
            if s > int(test.split('>')[1]): result = 1
        if '<' in test:
          if test.split('<')[0] == 'x':
            if x < int(test.split('<')[1]): result = 1
          if test.split('<')[0] == 'm':
            if m < int(test.split('<')[1]): result = 1
          if test.split('<')[0] == 'a':
            if a < int(test.split('<')[1]): result = 1
          if test.split('<')[0] == 's':
            if s < int(test.split('<')[1]): result = 1
        if result == 1:
          flow_name = dest;
          break
        else:
          continue;


          
      
print "PART A: " + str(total)
