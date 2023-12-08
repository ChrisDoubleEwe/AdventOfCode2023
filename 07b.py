filename = '07_in.txt';
game = [];
# Ace   = Z
# King  = R
# Queen = Q
# Ten   = D
# Joker = 1

# Five of a kind       9
# Four of a kind       8
# Full house           7
# Three of a kind      6
# Two pair             5
# One pair             4
# High card            3

scores = []

with open(filename) as f:
  for l in f:
    line = l.strip()
    print line
    hand = line.split();
    bid = hand[1];
    cards = [];
    orig_cards = ''
    for c in hand[0]:
      d = c;
      if c == 'A':
        d = 'Z';
      if c == 'K':
        d = 'R';
      if c == 'Q':
        d = 'Q';
      if c == 'T':
        d = 'D';
      if c == 'J':
        d = '1';


      cards.append(d)
      orig_cards += d

    cards.sort()
    this_hand = [];
    this_hand.append(cards);
    this_hand.append(bid);
    score = -1
    print cards

    # FIVE OF A KIND
    if cards[0]==cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]==cards[4]:
      type = 9;
      print "5 of a kind"

    # FOUR OF A KIND
    if (cards[0]==cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]!=cards[4]) or (cards[0]!=cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]==cards[4]):
      type = 8;
      print "4 of a kind"

    # FULL HOUSE
    if (cards[0]==cards[1] and cards[1]!=cards[2] and cards[2]==cards[3] and cards[3]==cards[4]) or (cards[0]==cards[1] and cards[1]==cards[2] and cards[2]!=cards[3] and cards[3]==cards[4]):
      type = 7;
      print "Full house"

    # THREE OF A KIND
    looking_for = [];
    for c in cards:
      if c not in looking_for:
        looking_for.append(c);

    found = [];
    for i in looking_for:
      found.append(cards.count(i));
    found.sort()
    print looking_for
    print found

    if len(looking_for) == 3 and max(found) == 3 and min(found) == 1:
      type = 6;
      print "3 of a kind"

    if len(looking_for) == 3 and max(found) == 2 and found[1] == 2:
      type = 5;
      print "2 Pair"

    if len(looking_for) == 4:
      type = 4;
      print "1 Pair"

    # High card
    if cards[0]!=cards[1] and cards[1]!=cards[2] and cards[2]!=cards[3] and cards[3]!=cards[4]:
      type = 3;
      print "High card"

    # Jokers
    jokers = orig_cards.count('1');
    old_type = type

    if type == 9:
      # FIVE OF A KIND
      dummy = 1;
    elif type == 8:
      # FOUR OF A KIND 
      if jokers == 1: # -> FIVE OF A KIND
        type = 9;
      if jokers == 4: # -> FIVE OF A KIND
        type = 9;
    elif type == 7:
      # FULL HOUSE
      if jokers == 2: # -> FIVE OF A KIND
        type = 9;
      if jokers == 3: # -> FIVE OF A KIND
        type = 9;
    elif type == 6:
      # THREE OF A KIND 
      if jokers == 1: # -> FOUR OF A KIND
        type = 8;
      if jokers == 2: # -> FIVE OF A KIND
        type = 9;
      if jokers == 3: # -> FOUR OF A KIND
        type = 8;
    elif type == 5:
      # TWO PAIR
      if jokers == 1: # -> FULL HOUSE
        type = 7;
      if jokers == 2: # -> FOUR OF A KIND
        type = 8;
    elif type == 4:
      # ONE PAIR
      if jokers == 1: # -> THREE OF A KIND
        type = 6;
      if jokers == 2: # -> THREE OF A KIND
        type = 6;
    elif type == 3:
      # HIGH CARD
      if jokers == 1: # -> ONE PAIR
        type = 4;




    if type == 9:
      print "=> Five of a kind      " 
    if type == 8:
      print "=> Four of a kind     "  
    if type == 7:
      print "=> Full house        "   
    if type == 6:
      print "=> Three of a kind  "    
    if type == 5:
      print "=> Two pair   "          
    if type == 4:
      print "=> One pair  "           
    if type == 3:
      print "=> High card"            








    score = str(type) + orig_cards
    if jokers > 0:
      print hand[0] + "  JOKERS: " + str(jokers) + " ; " + str(old_type) + " => " + str(type) + "    " + score

    if score == -1:
      print "MISS"
    print "-----"
    this_hand.append(score);
    scores.append(score);

    game.append(this_hand);

print "====="
scores.sort()
for s in scores:
  print s
print "====="


rank = 1
parta = 0
for s in scores:
  for g in game:
    if g[2] == s:
      print "Rank: " + str(rank)
      print "Score: " + str(g[1])
      print "----"
      parta = parta + (rank * int(g[1]));
      rank += 1

print "PART A: " + str(parta)
