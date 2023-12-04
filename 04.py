parta = 0;
filename = '04_in.txt';

with open(filename) as f:
  for l in f:
    line = l.strip()
    card = l.split(':')[1];
    card_num = l.split(':')[0];
    card_num = card_num.replace('  ',' ');
    card_num = card_num.replace('  ',' ');
    card_num = card_num.replace('  ',' ');
    card_num = card_num.split(' ')[1];
    numbers = card.split('|');
    win = numbers[0].strip().split(' '); 
    num = numbers[1].strip().split(' '); 
    nums = [];
    wins = [];

    for x in num:
      if x != '':
        nums.append(x);
    for x in win:
      if x != '':
        wins.append(x);

    score = 0;
    for n in nums:
      if n in wins:
        if score == 0:
          score = 1;
        else:
          score = score * 2;

    parta += score

print "PART A: " + str(parta)

entries = []
with open(filename) as f:
  for l in f:
    line = l.strip()
    card = l.split(':')[1];
    card_num = l.split(':')[0];
    card_num = card_num.replace('  ',' ');
    card_num = card_num.replace('  ',' ');
    card_num = card_num.replace('  ',' ');
    card_num = card_num.split(' ')[1];
    numbers = card.split('|');
    win = numbers[0].strip().split(' '); 
    num = numbers[1].strip().split(' '); 
    nums = [];
    wins = [];

    for x in num:
      if x != '':
        nums.append(x);
    for x in win:
      if x != '':
        wins.append(x);

    entry = [];
    entry.append(1);
    entry.append(int(card_num));
    entry.append(nums);
    entry.append(wins);
    entries.append(entry)

    
for e in entries:
  score = 0;
  for n in e[2]:
    if n in e[3]:
      score += 1;

  for i in range (1, score+1):
    for z in entries:
      if z[1] == e[1]+i:
        z[0] += e[0];


total_cards = 0
for e in entries:
  total_cards += e[0]

print "PART B: " + str(total_cards)
