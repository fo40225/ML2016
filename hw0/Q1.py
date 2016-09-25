import sys

col = int(sys.argv[1])
fileName = sys.argv[2]

nums = []

file = open(fileName, "r")
for line in file:
    cols = line.split()
    num = cols[col]
    nums.append(num)
file.close()

nums.sort(key=lambda x: float(x))
result = ",".join(nums)

ans = open("ans1.txt", "w")
ans.write(result)
ans.close()
