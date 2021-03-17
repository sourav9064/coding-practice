##Counting Rock Samples | TCS Codevita 2020
##Difficulty Level : Easy
## Last Updated : 13 Oct, 2020
##John is a geologist, and he needs to count rock samples in order to send it to a chemical laboratory. He has a problem. The laboratory only accepts rock samples by a range of its size in ppm (parts per million). John needs your help. Your task is to develop a program to get the number of rocks in each range accepted by the laboratory.
##
##Problem Statement: Given an array samples[] denoting sizes of rock samples and a 2D array ranges[], the task is to count the rock samples that are in the range ranges[i][0] to ranges[i][1], for every possible 1 <= i <= N.
##
##Examples:
##
##Input: samples[] = {345, 604, 321, 433, 704, 470, 808, 718, 517, 811}, ranges[] = {{300, 380}, {400, 700}}
##Output: 2 4
##Explanation: 
##Range [300, 380]: Samples {345, 321} lie in the range. Therefore, the count is 2. 
##Range [400, 700]: Samples {433, 604, 517, 470} lie in the range. Therefore, the count is 4.
##
##Input: samples[] = {400, 567, 890, 765, 987}, ranges[] = {{300, 380}, {800, 1000}
##Output: 0 2
##
##
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: The idea is to iterate samples[] for every ranges[i] and count the number of samples that lie in the specified ranges. Follow the steps below to solve the problem:
##
##Traverse the array ranges[].
##For each row ranges[i], traverse the array samples[] and count the number of rock samples lying in the range [ranges[i][0], ranges[i][1]]




def findRockSample(ranges, n, r, samples):
    a = []
    for i in range(r):
        c = 0
        l, h = ranges[i][0], ranges[i][1]
        for val in samples:
            if l <= val <= h:
                c += 1
        a.append(c)
    return a

#n = 5
n = 10
r = 2
#arr = [400, 567, 890, 765, 987]
#ranges = [[300, 380], [800, 1000]]
arr = [345, 604, 321, 433, 704, 470, 808, 718, 517, 811]
ranges = [[300,380],[400,700]]

print(*findRockSample(ranges, n, r, arr))























