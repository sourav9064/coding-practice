##Print the first N terms of the series 6, 28, 66, 120, 190, 276, …
##Difficulty Level : Hard
## Last Updated : 14 Sep, 2020
##Given a number N, the task is to print the first N terms of the series 6, 28, 66, 120, 190, 276, and so on.
##Examples:
##
##Input: N = 10 
##Output: 6 28 66 120 190 276 378 496 630 780
##
##Input: N = 4 
##Output: 6 28 66 120
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: To solve the problem mentioned above, we have to observe the below pattern:
##
##
##
##
##
##The general formula is given by: 
##k * (2 * k – 1), where initially, k = 2
##

def printSeries(n):
    k = 2
    for i in range(0,n):
        print(k*(2*k -1), end = ' ')
        k = k+2

n = 10
printSeries(n)




























