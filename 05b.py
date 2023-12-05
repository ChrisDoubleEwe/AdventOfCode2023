parta = 99999999999999;
filename = '05_test.txt';

s2s = 0;
s2f = 0;
f2w = 0;
w2l = 0;
l2t = 0;
t2h = 0;
h2l = 0;

s2s_array = [];
s2f_array = [];
f2w_array = [];
w2l_array = [];
l2t_array = [];
t2h_array = [];
h2l_array = [];

seeds = []

with open(filename) as f:
  for l in f:
    line = l.strip()

    if "seeds: " in line:
      seedstr = line.split(":")[1].split()
      for s in seedstr:
        seeds.append(int(s));

    if line == "seed-to-soil map:":
      s2s = 1;
      continue;

    if line == "soil-to-fertilizer map:":
      s2f = 1;
      continue;

    if line == "fertilizer-to-water map:":
      f2w = 1;
      continue;

    if line == "water-to-light map:":
      w2l = 1;
      continue;

    if line == "light-to-temperature map:":
      l2t = 1;
      continue;

    if line == "temperature-to-humidity map:":
      t2h = 1;
      continue;

    if line == "humidity-to-location map:":
      h2l = 1;
      continue;

    if line == "":
      s2s = 0;
      s2f = 0;
      f2w = 0;
      w2l = 0;
      l2t = 0;
      t2h = 0;
      h2l = 0;
      continue;

    parts = [];

    if s2s == 1 or s2f == 1 or f2w == 1 or w2l == 1 or l2t == 1 or t2h == 1 or h2l == 1:
      parts_str = line.split();
      for s in parts_str:
        parts.append(int(s));

    if s2s == 1:
      s2s_array.append(parts);
    if s2f == 1:
      s2f_array.append(parts);
    if f2w == 1:
      f2w_array.append(parts);
    if w2l == 1:
      w2l_array.append(parts);
    if l2t == 1:
      l2t_array.append(parts);
    if t2h == 1:
      t2h_array.append(parts);
    if h2l == 1:
      h2l_array.append(parts);


total = 0
for i in range(0, len(seeds),2):
 start = seeds[i]
 length = seeds[i+1]
 total += length;

print "Number of seeds: " + str(total);

count = 0
for i in range(0, len(seeds),2):
 count += 1
 start = seeds[i]
 length = seeds[i+1]

      
 for seed in range(start, start+length):
  count += 1

  soil = 0;
  fertilizer =0;
  water = 0;
  light = 0;
  temperature = 0;
  humidity = 0;
  location = 0;

  
  soil = seed
  for p in s2s_array:
    if seed >= p[1] and seed < p[1]+p[2]:
      soil = p[0] + (seed - p[1])
      break;

  fertilizer = soil
  for p in s2f_array:
    if soil >= p[1] and soil < p[1]+p[2]:
      fertilizer = p[0] + (soil - p[1])
      break;

  water = fertilizer
  for p in f2w_array:
    if fertilizer >= p[1] and fertilizer < p[1]+p[2]:
      water = p[0] + (fertilizer - p[1])
      break;

  light = water
  for p in w2l_array:
    if water >= p[1] and water < p[1]+p[2]:
      light = p[0] + (water - p[1])
      break;

  temperature = light
  for p in l2t_array:
    if light >= p[1] and light < p[1]+p[2]:
      temperature = p[0] + (light - p[1])
      break;

  humidity = temperature
  for p in t2h_array:
    if temperature >= p[1] and temperature < p[1]+p[2]:
      humidity = p[0] + (temperature - p[1])
      break;

  location = humidity
  for p in h2l_array:
    if humidity >= p[1] and humidity < p[1]+p[2]:
      location = p[0] + (humidity - p[1])
      break;



  #print "Seed " + str(seed) + ", soil " + str(soil) + ", fertilizer " + str(fertilizer) + ", water " + str(water) + ", light " + str(light) + ", temperature " + str(temperature) + ", humidity " + str(humidity) + ", location " + str(location)
  if location < parta:
    parta = location
    print "NEW LOWEST LOCATION: " + str(parta)

print "PART B: " + str(parta)
