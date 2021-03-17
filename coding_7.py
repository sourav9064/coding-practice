##Consider the below series:
##1, 2, 1, 3, 2, 5, 3, 7, 5, 11, 8, 13, 13, 17…..
##
##This series is a mixture of 2 series fail
##the odd terms in this series form a Fibonacci series and
##all the even terms are the prime numbers in ascending order
##
##Write a program to find the Nth term in this series
##
##The value N in a positive integer that should be read from mm.
##The Nth term that is calculated by the program should be written to STDOUT
##Otherthan the value of Nth term ,
##no other characters / string or message should be written to STDOUT.
##
##For example, when N:14, the 14th term in the series is 17
##So only the value 17 should be printed to STDOUT


def fib(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    

def prime(n):
    for n in range(2,end+1):
        if n> 1:
            for i in range(2,n):
                if n%i == 0:
                    break
            else:
                return n


n = int(input())
start = 0
end = int(input('enter last number of series: '))

##if (n%2) == 0:
##    print(prime(int(n/2)))
##else:
##    print(fib(int((n/2) + 1)))

print(prime(n))
