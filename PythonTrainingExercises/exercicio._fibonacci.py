"""

fibonacci usando o decorador @functools.lru_cache() Técnica de memoização, evitando repetir processamento em argumentos já usados anteriormente.

"""

import functools
import sys

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)


with open(sys.argv[1]) as f:
    for line in f:
        print(fibonacci(int(line.rstrip('\n'))))
f.close()

