def numberOfDiagonals(n):

    return n * (n - 3) // 2
 



def main():

    n = int(input())
    print(numberOfDiagonals(n))
 

if __name__ == '__main__':

    main()