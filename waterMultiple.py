



from  __future__ import print_function

def waterMult(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 3*waterMult(n-1)-waterMult(n-2)

def main():
    try:
        n = int(input("Enter n: "))
        for i in range(1, n + 1) :
            f = waterMult(i)
            print("waterMul(%d) = %d" % (i, f))
    except RecursionError:
        print("Error found")
        exit(0)


if __name__ == '__main__':
    main()
