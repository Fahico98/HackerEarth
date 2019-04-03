
def numbersToMatchsticks(num):
	if(num == 0 or num == 6 or num == 9):
		return 6
	elif(num == 1):
		return 2
	elif(num == 2 or num == 3 or num == 5):
		return 5
	elif(num == 4):
		return 4
	elif(num == 7):
		return 3
	elif(num == 8):
		return 7

T = int(input())
Ns = []
output = []

for i in range(T):
	Ns.append(input())

for i in range(T):
	bufferList = []
	for j in list(Ns[i]):
		bufferList.append(j)
	bufferList = list(map(int, bufferList))
	matchsticksList = list(map(numbersToMatchsticks, bufferList))
	totalMatchsticks = 0
	for k in matchsticksList:
		totalMatchsticks += k
	TMBuffer = totalMatchsticks
	ones = 0
	sevents = 0
	while(TMBuffer != 0):
		if(TMBuffer - 2 == 1):
			TMBuffer -= 3
			sevents += 1
		else:
			TMBuffer -= 2
			ones += 1
	outNumber = 0
	for t in range(ones + 1):
		if(t != ones):
			outNumber += pow(10, t)
		elif(sevents == 1):
			outNumber += 7 * pow(10, t)
	output.append(outNumber)

for element in output:
	print(element)
