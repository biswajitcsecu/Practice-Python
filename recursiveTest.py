



from __future__ import print_function


def mergrun (n):
    if n==0:
        return 1
    else:
        return  mergrun(n-1) + 1



def main():
    try:
        n = int (input("Enter your number:\t"))
        print("Your number is : %d\t"%n)
        for i in range(1, n+1) :
            f = mergrun(i)
            print("cost(%d) = %d" % (i, f))

    except RecursionError:
        print("Error found")
        exit(0)





if __name__ == '__main__':
    main()