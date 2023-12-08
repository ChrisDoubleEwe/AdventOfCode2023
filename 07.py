filename = '07_in.txt';
game = [];
# Ace   = Z
# King  = R
# Queen = Q
# Jack  = J
# Ten   = D

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
      if c == 'J':
        d = 'J';
      if c == 'T':
        d = 'D';

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
      type = 1;
      score = '9' + orig_cards
      print "5 of a kind"

    # FOUR OF A KIND
    if (cards[0]==cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]!=cards[4]) or (cards[0]!=cards[1] and cards[1]==cards[2] and cards[2]==cards[3] and cards[3]==cards[4]):
      type = 2;
      score = '8' + orig_cards
      print "4 of a kind"

    # FULL HOUSE
    if (cards[0]==cards[1] and cards[1]!=cards[2] and cards[2]==cards[3] and cards[3]==cards[4]) or (cards[0]==cards[1] and cards[1]==cards[2] and cards[2]!=cards[3] and cards[3]==cards[4]):
      type = 2;
      score = '7' + orig_cards
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
      type = 3;
      score = '6' + orig_cards
      print "3 of a kind"

    if len(looking_for) == 3 and max(found) == 2 and found[1] == 2:
      type = 4;
      score = '5' + orig_cards
      print "2 Pair"

    if len(looking_for) == 4:
      type = 5;
      score = '4' + orig_cards
      print "1 Pair"

    # FIVE OF A KIND
    if cards[0]!=cards[1] and cards[1]!=cards[2] and cards[2]!=cards[3] and cards[3]!=cards[4]:
      type = 6;
      score = '3' + orig_cards
      print "High card"

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
