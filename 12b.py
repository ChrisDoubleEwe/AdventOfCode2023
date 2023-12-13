from copy import copy, deepcopy
filename = '12_in.txt';


partb = 0;

def new_calc(s):
  res = ''

  counting = 0
  count = 0
  for c in s:
    if c == '.':
      if counting == 0:
        continue;
      else:
        res += str(count) + ','
        count = 0;
        counting = 0;
        continue;
    elif c == '#':
      if counting == 1:
        count += 1;
      else:
        counting = 1;
        count = 1;
    elif c == '?':
        counting = 0;
        break
  if counting == 1:
    res += str(count) + ','
  return res[:-1]

cache = {}

def count_ways(s, n):

  if (s, tuple(n)) in cache:
    return cache[(s, tuple(n))]

  #if len(n) == 0:
  #  if '#' in s:
  #    return 0;
  #  else:
  #    return 1;
  if len(n) == 0:
    return 1 if "#" not in s else 0


  size = n[0]
  result = 0;

  for i in range(0, len(s)):
    if i + size <= len(s):
      found_dot = 0;
      for c in s[i:i+size]:
        if c == '.':
          found_dot=1;
      if found_dot == 0:
        if (i == 0 or s[i - 1] != "#"):
          if (i + size == len(s) or s[i + size] != "#"):
            result += count_ways(s[i + size + 1 :], n[1:])

    if s[i] == '#':
      break;
  cache[(s, tuple(n))] = result

  return result

def calc(s):
  res = ''

  counting = 0
  count = 0
  for c in s:
    if c == '.':
      if counting == 0:
        continue;
      else:
        res += str(count) + ','
        count = 0;
        counting = 0;
        continue;
    else:
      if counting == 1:
        count += 1;
      else:
        counting = 1;
        count = 1;
  if counting == 1:
    res += str(count) + ','
  return res[:-1]

count = -1
partb = 0;

with open(filename) as f:
  for l in f:
    count += 1
    row=l.strip().split(' ');

    new_input = row[0] + '?'
    new_input += row[0] + '?'
    new_input += row[0] + '?'
    new_input += row[0] + '?'
    new_input += row[0]
  
    new_match = row[1] + ','
    new_match += row[1] + ','
    new_match += row[1] + ','
    new_match += row[1] + ','
    new_match += row[1]


    nums = new_match.split(',')
    int_nums = []
    for z in nums:
      int_nums.append(int(z));
    result = count_ways(new_input, int_nums)

    print "Line " + str(count) + " : " + str(result)

    partb += result;


print "PART B: " + str(partb)    
