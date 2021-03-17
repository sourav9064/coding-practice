##TCS NQT 2020 | Trains
##Difficulty Level : Easy
## Last Updated : 29 Oct, 2020
##Problem:
##
##In one pass, Train A can start from the source station at time T[0], halt at each station for h unit of time until it reaches the last station at time T[N – 1], where N is the positive integer representing a total number of stations. 
##
##Given, Train A’s timings at each unit of time as T[] = {10.00, 10.04, 10.09, 10.15, 10.19, 10.22}.
##
##Now, suppose Railway Admin wants to add more trains to increase the frequency. So, to launch other Train B, for the same stations as of Train A’s. Provided the Train B starts at time t, they would like to know the timings for Train B. The program should return a String array S (timestamp(in float) for Train B at each station from first to the last station like train A).  
##
##Note:
##
##
##
##The time is represented in 24-Hour.
##Start Hour should be in the range [0, 23].
##Start Minute should be in the range [0, 59].
##Enter start time(24 Hrs)
##Examples:
##
##Input: t = 11.00
##Output: 11.00 11.04 11.09 11.15 11.19 11.22
##Explanation: Start time for train B is 11.00 and also the time difference between the stations for train B is same as for train A.
##
##Input: t = -26.15
##Output: Invalid Input
##Explanation: No such time as -26.15 exists. Hence, print “Invalid Input”.
##
##Approach: The idea is to calculate the time differences between the stations from the given timings of Train A. Follow the steps below to solve the problem:
##
##From the given array T[], generate an array train_B[] where train_B[i] is the time difference between T[i] and T[i – 1], where train_B[0] = 0.00 and 1 ≤ i ≤ 5.
##Therefore, train_B[] = {0.00, 0.04, 0.05, 0.06, 0.04, 0.03}.
##If the integer part of t is not in the range [0, 24] or the decimal part of t is not in the range [0, 60], then print “Invalid Input” because the integer part represents the hours and the decimal part represents the minutes.
##Otherwise, traverse over the range [0, 5] and print t + train_B[i] denoting the time for train B for the ith station. Then update t as t = t + train_B[i].





##def findTime(train_A , N, t):
##    x = 0.00
##    train_B = []
##    #train_B[0] = 0
##
##    for i in range(0,N-1):
##        train_B.append(train_A[i] - train_A[i-1])
##
##    #int(it)
##    #int(ix)
##    it = int(t)
##
##    if ( (t>=0.00 and t<=24.00) and ( t-it)<= 60.00 ):
##        for i in range(0,6):
##            x = t + train_B[i]
##            ix = int(x)
##            if (x - ix)>= 0.60:
##                x = x + 0.40
##            if (x > 24.00):
##                x = x - 24.00
##            print(x)
##            t = x
##    else:
##        print("Invalid Input")
##
##
##train_A = [ 10.00, 10.04, 10.09, 10.15, 10.19, 10.22 ]
##N = len(train_A)
##t = 11.00
##
##findTime(train_A, N, t)

train_A = [ 10.00, 10.04, 10.09, 10.15, 10.19, 10.22 ]
t = 23.59

N = len(train_A)
v1  = [train_A[i]-train_A[i] for i in range(1)]
v2  = [train_A[i]-train_A[i-1] for i in range(1,N)]
lst1 = [ '%.2f' % elem for elem in v1 ]
lst2 = [ '%.2f' % elem for elem in v2 ]
lst = lst1 + lst2
#print(lst)
if t>= 0.00 and t<= 24.60:
    t = str(t)
    new_lst = [ float(t)+float(i) for i in lst]
    n_lst = [ '%.2f' % elem for elem in new_lst]
    #print(new_lst)
    res = " ".join([str(i) for i in new_lst])
    print(res)
else:
    print("Invalid Input")











































