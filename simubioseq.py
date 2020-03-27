

from __future__ import print_function
from Bio.Seq import Seq
import Bio
print(Bio.__version__)



def main():
    try:
        my_seq = Seq("AGTACACTGGT")
        print(my_seq, end='\n')
        my_seq.complement()
        print(my_seq, end='\n')

    except:
        pass


if __name__ == "__main__":
    main()
