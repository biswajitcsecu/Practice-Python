

from __future__ import  print_function

class mybox:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sumdigit(self):
        self.z= self.x + self.y
        print('Sum of %d and %d is: %d\t'%(self.x, self.y, self.z), end ='')

def main():
    try:
        a = int (input("Enter first number=\t"))
        print(f'You enter: %d\t'%(a))
        b = int (input("Enter second number=\t"))
        print(f'You enter: %d\t' %(b))
        box = mybox(a, b)
        box.sumdigit()

    except:
        print("Error Found")




if __name__ == '__main__':
    main()






