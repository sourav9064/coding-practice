##Write a code to check whether no is prime or not.
##Condition use function check() to find whether entered no is
##positive or negative ,if negative then enter the no,
##And if yes pas no as a parameter to prime()
##and check whether no is prime or not?


num = int(input())

def check(n):
    if n >= 0:
        a = n
        return a
    else:
        b = n
        return b

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
        print("not prime number")



if (check(num)>=0):
    prime(num)
else:
    print("not prime number")
