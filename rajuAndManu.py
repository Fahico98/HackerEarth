
'''
El metodo "format()", cuando se usa tal y como se muestra en el siguiente ejercicio, devuelve
el valor de "j" en numero binario, con el primer bit a la izquierda, es decir, el numero se
lee de izquierda a derecha.
'''

T = int(input())
output = []

for i in range(T):
	max = 0
	toAppend = ""
	N = int(input())
	for j in range(N, 0, -1):
		binaryNum = format(j, "b")
		ones = binaryNum.count("1")
		if(ones > max):
			max = ones
			toAppend = int(binaryNum, 2)
	output.append(toAppend)

for i in output:
	print(i)