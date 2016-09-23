import sys
col = int(sys.argv[1])
fileName = sys.argv[2]

file = open(fileName,"r")
nums = []

for line in file:
    cols = line.split()
    num = float(cols[col])
    nums.append(num)

file.close()

nums.sort()
result = ",".join(map(lambda x:"{:.3f}".format(x),nums))

ans = open("ans1.txt","w")
ans.write(result)
ans.close()
