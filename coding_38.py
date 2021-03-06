##Nth Term of a Fibonacci Series of Primes formed by concatenating pairs of Primes in a given range
##Last Updated : 19 Oct, 2020
##Given two integers X and Y, the task is to perform the following operations:
##
##Find all prime numbers in the range [X, Y].
##Generate all numbers possible by combining every pair of primes in the given range.
##Find the prime numbers among all the possible numbers generated above. Calculate the count of primes among them, say N.
##Print the Nth term of a Fibonacci Series formed by having the smallest and largest primes from the above list as the first two terms of the series.
##Examples:
##
##Input: X = 2 Y = 40 
##Output: 34 
##Explanation: 
##All primes in the range [X, Y] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] 
##All possible numbers generated by concatenating each pair of prime = [23, 25, 27, 211, 213, 217, 219, 223, 229, 231, 32, 35, 37, 311, 313, 319, 323, 329, 331, 337, 52, 53, 57, 511, 513, 517, 519, 523, 529, 531, 537, 72, 73, 75, 711, 713, 717, 719, 723, 729, 731, 737, 112, 113, 115, 117, 1113, 1117, 1119, 1123, 1129, 1131, 1137, 132, 133, 135, 137, 1311, 1317, 1319, 1323, 1329, 1331, 1337, 172, 173, 175, 177, 1711, 1713, 1719, 1723, 1729, 1731, 1737, 192, 193, 195, 197, 1911, 1913, 1917, 1923, 1929, 1931, 1937, 232, 233, 235, 237, 2311, 2313, 2317, 2319, 2329, 2331, 2337, 292, 293, 295, 297, 2911, 2913, 2917, 2919, 2923, 2931, 2937, 312, 315, 317, 3111, 3113, 3117, 3119, 3123, 3129, 3137, 372, 373, 375, 377, 3711, 3713, 3717, 3719, 3723, 3729, 3731]
##All primes among the generated numbers=[193, 3137, 197, 2311, 3719, 73, 137, 331, 523, 1931, 719, 337, 211, 23, 1117, 223, 1123, 229, 37, 293, 2917, 1319, 1129, 233, 173, 3119, 113, 53, 373, 311, 313, 1913, 1723, 317]
##
##Count of the primes = 34 
##Smallest Prime = 23 
##Largest Prime = 3719 
##Therefore, the 34th term of the Fibonacci series having 23 and 3719 as the first two terms, is 13158006689.
##Input: X = 1, Y = 10 
##Output: 1053
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: 
##Follow the steps below to solve the problem:
##
##
##
##Generate all possible primes using the Sieve of Eratothenes.
##Traverse the range [X, Y] and generate all primes in the range with the help of primes[] array generated in the step above.
##Traverse the list of primes and generate all possible pairs from the list.
##For each pair, concatenate the two primes and check if their concatenation is a prime or not.
##Find the maximum and minimum of all such primes and count all such primes obtained.
##Finally, print the countth of a Fibonacci series having minimum and maximum obtained in the above step as the first two terms of the series.


prime = [True for i in range(100001)]

def genPrime():
    p = 2
    while(p*p <= 100000):
        if(prime[p] == True):
            for i in range(p*p, 100001, p):
                prime[i] = False
        p += 1

def fibonacciPrime(n1,n2):
    genPrime()
    initial = []
    for i in range(n1,n2):
        if prime[i]:
            initial.append(i)
    now = []
    for a in initial:
        for b in initial:
            if a!=b:
                c = str(a) + str(b)
                now.append(int(c))
    current = []
    for x in now:
        if prime[x]:
            current.append(x)
    current = set(current)
    first = min(current)
    second = max(current)
    count = len(current)-1
    curr = 1
    while curr<count:
        c = first+second
        first = second
        second = c
        curr += 1
    print(c)


x = 1#2
y = 10#40
fibonacciPrime(x,y)


    



























