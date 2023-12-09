filename = '09_in.txt';
parta = 0
partb = 0


with open(filename) as f:
  for l in f:
    nums = []
    line = []
    for n in l.split():
      line.append(int(n));

    nums.append(line)

    cont = 1
    while cont == 1:
      next_line = []
      for i in range(1, len(line)):
        next_line.append(line[i]-line[i-1])
      if max(next_line) == 0 and min(next_line) == 0:
        cont = 0
        next_line.append(0);
      nums.append(next_line);
      line = next_line


    # PART A

    new_nums = [];
    new_nums.append(nums[len(nums)-1]);

    for i in range(len(nums)-2, -1, -1):
      # A = p + diff
      diff = nums[i+1][len(nums[i+1])-1]
      p = nums[i][len(nums[i])-1]
      A = p + diff
      new_line = nums[i]
      new_line.append(A)
      new_nums.append(new_line)

    new_nums.reverse()
    parta += new_nums[0][len(new_nums[0])-1]

    # PART B
    new_nums = [];
    new_nums.append(nums[len(nums)-1]);

    for i in range(len(nums)-2, -1, -1):
      # A = p - diff
      diff = nums[i+1][0]
      p = nums[i][0]
      A = p - diff

      new_line = []
      new_line.append(A)
      for n in nums[i]:
        new_line.append(n)
      new_nums.append(new_line)
      nums[i] = list(new_line)


    new_nums.reverse()
    partb += new_nums[0][0]


print "PART A: " + str(parta)
print "PART B: " + str(partb)

       

