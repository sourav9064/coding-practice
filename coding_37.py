##Print the Vowels in the Order of their occurrence in the given Matrix
##Difficulty Level : Hard
## Last Updated : 23 Oct, 2020
##Given a character matrix arr[][] of dimensions 3 * N, consisting of three characters {#, *, . }, the task is to find the vowels(A, E, I, O, U) represented by ‘*’ from the given string.
##
##Note: Vowel A is denoted in a 3×3 block, as shown in the examples below.
##
##Explanation:
##
##Input: N = 18
##
##* . * # * * * # * * * # * * * . * .
##* . * # * . * # . * . # * * * * * *
##* * * # * * * # * * * # * * * * . *
##Output: U#O#I#E#A
##Input: N = 12 
## 
##
##
##
##* . * # . * * * # . * .
##* . * # . . * . # * * *
##* * * # . * * * # * . *
##Output: U#I#A 
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: The idea is to observe the pattern of row indices and column indices of the dots for each vowel {‘A’, ‘E’, ‘I’, ‘O’, ‘E’} and check the following conditions for every jth column:  
##
##Initialize the final result, res as an empty string
##If arr[0][j] is equal to ‘#’, then append “#” to the final result.
##If arr[0][j] is equal to ‘.’ and arr[1][j] and arr[2][j] are both equal to ‘.’, it denotes an empty space.
##If arr[0][j] is equal to ‘.’ and arr[0][j + 2] is equal to ‘.’ and arr[2][j + 1] is equal to ‘.’, then append “A” to the final result.
##If arr[0][j + 1] is equal to ‘.’ and arr[1][j + 1] is equal to ‘.’, then append “U” to the final result.
##If arr[0][j + 1] is not equal to ‘.’ and arr[1][j + 1] is equal to ‘.’, then append “O” to the final result.
##If arr[1][j] is equal to ‘.’ and arr[1][j + 2] is equal to ‘.’, then append “I” to the final result.
##Otherwise, append “E” to the final result.

def helper(n,arr):
    res = ""
    for j in range(n):
        if (arr[0][j] == '#'):
            res += "#" 
            #j += 3
            continue
        elif (arr[0][j] == '.' and arr[1][j] == '.' and arr[2][j] == '.'):
            #j += 3
            continue
        elif (j < n - 2 and arr[0][j] == '.' and arr[0][j + 2] == '.' and arr[2][j + 1] == '.'):
            res += 'A'
            #j += 3
            continue
        elif(j < n - 1 and arr[0][j + 1] == '.' and arr[1][j + 1] == '.'):
            res += 'U'
            #j += 3
            continue
        elif(j < n - 1 and arr[1][j + 1] == '.'):
            res += 'O'
            if(j >n-1):
                res += 'E'
            j += 3
            continue
        elif(j < n - 2 and arr[1][j] == '.' and arr[1][j + 2] == '.'):
            res += 'I'
            #j += 3
            continue
        elif(j < n-2):
            res += 'E'
            #j += 3
            continue
    #j += 3
    #res = "U#O#I#EA"
    return res

#n = 18
#arr = [['*', '.', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '.', '*', '.'],
#       ['*', '.', '*', '#', '*', '.', '*', '#', '.', '*', '.', '#', '*', '*', '*', '*', '*', '*'],
#       ['*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '#', '*', '*', '*', '*', '.', '*']]

n = 12
arr = [['*', '.', '*', '#', '.', '*', '*', '*', '#', '.', '*', '.'],
       ['*', '.', '*', '#', '.', '.', '*', '.', '#', '*', '*', '*'],
       ['*', '*', '*', '#', '.', '*', '*', '*', '#', '*', '.', '*']]
print(helper(n,arr))




























