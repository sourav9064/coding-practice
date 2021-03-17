num = int(input())


def prime(n):
    if n>1:
        for i in range(2,n):
            if n%i == 0:
                print("not prime number")
                break
        else:
            print("prime number")
            print(n)
    else:
        print("not prime number 2")


prime(num)
