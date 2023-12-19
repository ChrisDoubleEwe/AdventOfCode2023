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


routes = []

def get_paths(node, sofar):
  if node == 'R':
    return;
  if node == 'A':
    sofar.append(node);
    routes.append(sofar);
    return;
  rule = rules[node]
  for r in rule:
    if ":" not in r:
      get_paths(r, sofar)
      break;
    else:
      test = r.split(':')[0]
      dest = r.split(':')[1]
      if '>' in test:
        inv_test = test.replace('>','<=');
      else:
        inv_test = test.replace('<','>=');
      fail = copy.deepcopy(sofar)
      fail.append(test);
      sofar.append(inv_test)
      get_paths(dest, fail)
       
get_paths('in', [])

total = 0
for route in routes:
  print route
  x_lower = 0
  x_upper = 4000
  m_lower = 0
  m_upper = 4000
  a_lower = 0
  a_upper = 4000
  s_lower = 0
  s_upper = 4000

  for r in route:
    b = r[0]
    num = -1;
    if '=' in r:
      num = int(r.split('=')[1])
    elif '<' in r:
      num = int(r.split('<')[1])
    elif '>' in r:
      num = int(r.split('>')[1])

    if b == 'x':
      if '>=' in r:
        if num-1 > x_lower:
          x_lower = num-1
      elif '>' in r:
        if num > x_lower:
          x_lower = num
      elif '<=' in r:
        if num < x_upper:
          x_upper = num
      elif '<' in r:
        if num-1 < x_upper:
          x_upper = num-1
    if b == 'm': 
      if '>=' in r:
        if num-1 > m_lower:
          m_lower = num-1
      elif '>' in r:
        if num > m_lower:
          m_lower = num
      elif '<=' in r:
        if num < m_upper:
          m_upper = num
      elif '<' in r:
        if num-1 < m_upper:
          m_upper = num-1
    if b == 'a': 
      if '>=' in r:
        if num-1 > a_lower:
          a_lower = num-1
      elif '>' in r:
        if num > a_lower:
          a_lower = num
      elif '<=' in r:
        if num < a_upper:
          a_upper = num
      elif '<' in r:
        if num-1 < a_upper:
          a_upper = num-1
    if b == 's': 
      if '>=' in r:
        if num-1 > s_lower:
          s_lower = num-1
      elif '>' in r:
        if num > s_lower:
          s_lower = num
      elif '<=' in r:
        if num < s_upper:
          s_upper = num
      elif '<' in r:
        if num-1 < s_upper:
          s_upper = num-1


  print str(x_lower) + "<<x<<" + str(x_upper) + " : " + str(m_lower) + "<<m<<" + str(m_upper) + " : " + str(a_lower) + "<<a<<" + str(a_upper) + " : " + str(s_lower) + "<<s<<" + str(s_upper)

  total += (x_upper-x_lower)*(m_upper-m_lower)*(a_upper-a_lower)*(s_upper-s_lower)


print "PART B: " + str(total)
