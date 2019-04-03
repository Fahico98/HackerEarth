
T = int(input())
M = int(input())

output = []

for i in range(T):
	namesList = []
	bankBalances = []
	commas = []
	for j in range(M):
		inputStr = input()
		inputList = str.split(inputStr)
		if(len(inputList) == 2):
			namesList.append(str.split(inputStr)[0])
			bankBalances.append(str.split(inputStr)[1])
		else:
			namesList.append(str.split(inputStr)[0])
	for j in bankBalances:
		commas.append(j.count(","))
	maxCommas = max(commas)
	namesList.reverse()
	bankBalances.reverse()
	commas.reverse()
	maxIndex = commas.index(maxCommas)
	output.append(namesList[maxIndex] + " " + str(commas[maxIndex]))

for i in output:
	print(i)
