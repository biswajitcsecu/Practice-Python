

from  __future__ import print_function
from toolz.curried import excepts


def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def main():
    try:
        n = int(input("Enter n: "))
        for i in range(1, n + 1) :
            f = fib(i)
            print("fib(%d) = %d" % (i, f))
    except RecursionError:
        print("Error found")
        breakpoint()



if __name__ == '__main__':
    main()
