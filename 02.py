parta = 0;
partb = 0;
filename = '02_in.txt';

max_red=12;
max_green=13;
max_blue=14;

with open(filename) as f:
  for l in f:
    line = l.strip()
    x = line.split(":")
    game_id = int(x[0].split(" ")[1]);
    print "Game: " + str(game_id);
    possible = 1;
    for g in x[1].strip().split("; "):
      num_red = 0;
      num_blue = 0;
      num_green = 0;
      for c in g.split(", "):
        pair = c.split(" ");
        color = pair[1].strip()
        num = int(pair[0].strip());
        if color == "red": num_red = num;
        if color == "blue": num_blue = num;
        if color == "green": num_green = num;
      if (num_red <= max_red) and (num_green <= max_green) and (num_blue <= max_blue):
        # POSSIBLE
        dummy = 1;
      else:
        # IMPOSSIBLE
        possible = 0;
    if possible == 1:
      parta += game_id;


print "PART A: " + str(parta); 

with open(filename) as f:
  for l in f:
    line = l.strip()
    x = line.split(":")
    game_id = int(x[0].split(" ")[1]);
    print "Game: " + str(game_id);
    min_red = -1;
    min_blue = -1;
    min_green = -1;

    for g in x[1].strip().split("; "):
      num_red = 0;
      num_blue = 0;
      num_green = 0;
      for c in g.split(", "):
        pair = c.split(" ");
        color = pair[1].strip()
        num = int(pair[0].strip());
        if color == "red": num_red = num;
        if color == "blue": num_blue = num;
        if color == "green": num_green = num;

        #print "red: " + str(num_red) + " ; green: " + str(num_green) + " ; blue: " + str(num_blue);


        if num_red > min_red: min_red = num_red;
        if num_blue > min_blue: min_blue = num_blue;
        if num_green > min_green: min_green = num_green;

    print "Min red: " + str(min_red) + " ; Min green: " + str(min_green) + " ; Min blue: " + str(min_blue);
    power = min_red*min_green*min_blue;
    print str(power);
    partb += power

print "PART B: " + str(partb);




