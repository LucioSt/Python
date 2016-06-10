"""Sample code to read in test cases:
INPUT SAMPLE:

Imprimir os números pares, de 1 a 99, um por linha

"""

y = [x for x in range(100) if (x%2!=0)]
print(*y, sep='\n')