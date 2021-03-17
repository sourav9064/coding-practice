##Super ASCII String Checker | TCS CodeVita
##Difficulty Level : Hard
## Last Updated : 03 Feb, 2021
##In the Byteland country, a string S is said to super ASCII string if and only if the count of each character in the string is equal to its ASCII value. In the Byteland country ASCII code of ‘a’ is 1, ‘b’ is 2, …, ‘z’ is 26. The task is to find out whether the given string is a super ASCII string or not. If true, then print “Yes” otherwise print “No”.
##
##Examples:
##
##Input: S = “bba” 
##Output: Yes
##Explanation:
##The count of character ‘b’ is 2 and the ASCII value of ‘b’ is also 2.
##The count of character ‘a’ is 1. and the ASCII value of ‘a’ is also 1. 
##Hence, string “bba” is super ASCII String.
##
##Input: S = “ssba”
##Output: No
##Explanation:
##The count of character ‘s’ is 2 and the ASCII value of ‘s’ is 19.
##The count of character ‘b’ is 1. and the ASCII value of ‘b’ is 2.
##Hence, string “ssba” is not a super ASCII String.
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: The ASCII value of a character ‘ch‘ in Byteland can be calculated by the following formula:
##
##
##
##The ASCII value of ch = integer equivalent of ch – integer equivalent of ‘a'(97) + 1
##
##Now, using this formula, the frequency count of each character in the string can be compared with its ASCII value. Follow the below steps to solve the problem:
##
##Initialize an array to store the frequency count of each character of the string.
##Traverse the string S and increment the frequency count of each character by 1.
##Again, traverse the string S and check if any character has non-zero frequency and is not equal to its ASCII value then print “No”.
##After the above steps if there doesn’t any such character in the above step then print “Yes”.





def checkSuperASCII(s):
    b = [0 for i in range(26)]

    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1
        b[index - 1] += 1

    for i in range(len(s)):
        index = ord(s[i]) - 97 + 1
        if (b[index - 1] != index):
            print("no")
            return
    print("yes")

s = input("input string: ")
checkSuperASCII(s)

    





















