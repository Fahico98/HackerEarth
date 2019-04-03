
def reverseSlicing(str):
    return str[::-1]

n = int(input())
output = []

zerosStr = ""
for i in range(n):
	zerosStr += "0"

bufferStr = zerosStr

for ones in range(1, n + 1):
	onesStr = ""
	for i in range(ones):
		onesStr += "1"
	for i in range(n - ones + 1):
		bufferStr = bufferStr[:i] + onesStr + bufferStr[i + ones:]
		output.append(int(reverseSlicing(bufferStr), 2))
		bufferStr = zerosStr

for i in output:
	print(str(i) + " ", end="")

