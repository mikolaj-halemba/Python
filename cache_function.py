import functools
import time
@functools.lru_cache(maxsize=100)
def fib(n):
    if n <= 2:
        result = n
    else:
        result = fib(n - 1) + fib(n - 2)

    return result

start = time.time()
for i in range(100):
    result=fib(i)
    print("numer itracji:{}  czas: {} wynik {}".format(i,time.time()-start,result))



