parta = 0;
partb = 0;
filename = '01_in.txt';

with open(filename) as f:
  for l in f:
    line = l.strip()

    first = '99';
    last = '99';
    for c in line:
      if c in '0123456789':
        if first == '99':
          first = int(c);
        last = int(c);
    value_string = str(first) + str(last);
    value = int(value_string);
    parta += value;

print("PART A: " + str(parta));


with open(filename) as f:
  for l in f:
    sofar = '';
    line = l.strip()

    first = '';
    last = '';
    for c in line:
      sofar += c;
      if 'one' in sofar: c = '1' ; sofar = '';
      if 'two' in sofar: c = '2' ; sofar = '';
      if 'three' in sofar: c = '3' ; sofar = '';
      if 'four' in sofar: c = '4' ; sofar = '';
      if 'five' in sofar: c = '5' ; sofar = '';
      if 'six' in sofar: c = '6' ; sofar = '';
      if 'seven' in sofar: c = '7' ; sofar = '';
      if 'eight' in sofar: c = '8' ; sofar = '';
      if 'nine' in sofar: c = '9' ; sofar = '';

      if c in '0123456789':
        sofar = '';
        if first == '':
          first = int(c);

    rev_line = line[::-1]
    sofar = '';
    for c in rev_line:
      sofar = c + sofar;
      if 'one' in sofar: c = '1' ; sofar = '';
      if 'two' in sofar: c = '2' ; sofar = '';
      if 'three' in sofar: c = '3' ; sofar = '';
      if 'four' in sofar: c = '4' ; sofar = '';
      if 'five' in sofar: c = '5' ; sofar = '';
      if 'six' in sofar: c = '6' ; sofar = '';
      if 'seven' in sofar: c = '7' ; sofar = '';
      if 'eight' in sofar: c = '8' ; sofar = '';
      if 'nine' in sofar: c = '9' ; sofar = '';

      if c in '0123456789':
        sofar = '';
        if last == '':
          last = int(c);

    value_string = str(first) + str(last);
    value = int(value_string);
    partb += value;


print("PART B: " + str(partb));

