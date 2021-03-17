##Make all strings from a given array equal by replacing minimum number of characters
##Difficulty Level : Medium
## Last Updated : 21 Jan, 2021
##Given an array of equal-length strings arr[], the task is to make all the strings of the array equal by replacing any character of a string with any other character, minimum number of times.
##
##Examples:
##
##Input: arr[] = { “west”, “east”, “wait” } 
##Output: 3 
##Explanation: 
##Replacing arr[0][1] with ‘a’ modifies arr[] to { “west”, “east”, “wait” }. 
##Replacing arr[1][0] with ‘w’ modifies arr[] to { “wast”, “wast”, “wait” }. 
##Replacing arr[2][2] with ‘s’ modifies arr[] to { “wast”, “wast”, “wast” }. 
##Therefore, the required output is 3.
##
##Input: arr[] = { “abcd”, “bcde”, “cdef” } 
##Output: 8
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach:The problem can be solved using Hashing. Follow the steps below to solve the problem:
##
##Initialize a 2D array, say hash[][], where hash[i][j] stores the frequency of the character i present at the jth index of all the strings.
##Traverse the array arr[] using variable i. For every ith string encountered, count the frequency of each distinct character of the string and store it into the hash[][] array.
##Initialize a variable, say cntMinOp, to store the minimum count of operations required to make all the strings of the array equal.
##Traverse the array hash[][] using variable i. For every ith column encountered, calculate the sum of the column, say Sum, the maximum element in the column, say Max, and update cntMinOp += (Sum – Max).
##Finally, print the value of cntMinOp.







def minOperation(arr,N):
    cntMinOp = 0
    M = len(arr[0])
    hash = [[0 for i in range(M)] for j in range(256)]

    for i in range(N):
        for j in range(M):
            hash[ord(arr[i][j])][j] += 1

    for i in range(M):
        Sum,Max = 0,0
        for j in range(256):
            Sum += hash[j][i]
            Max = max(Max, hash[j][i])

        cntMinOp += (Sum - Max)
    return cntMinOp

arr = list(input("enter the arrays: ").strip().split())
N = len(arr)

print(minOperation(arr,N))





            




















