# list comprehensions cria listas a partir de uma sequencia ou qualquer outro tipo iterativo, filtrando e transformando os items
# 
# Usar no lugar de lambda
# 
# Python supports a concept called "list comprehensions". It can be used to construct lists in a very natural, easy way, like a mathematician is used to do.
# 
# The following are common ways to describe lists (or sets, or tuples, or vectors) in mathematics.
# 
# S = {x² : x in {0 ... 9}}
# V = (1, 2, 4, 8, ..., 2¹²)
# M = {x | x in S and x even}
# 
# 

colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors for size in sizes]



