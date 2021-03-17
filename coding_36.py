##Television Sets | TCS MockVita 2020
##Difficulty Level : Medium
## Last Updated : 17 Sep, 2020
##Problem Description
##
##Dr. Vishnu is opening a new world-class hospital in a small town designed to be the first preference of the patients in the city. Hospital has N rooms of two types with TV and without TV, with daily rates of R1 and R2 respectively. However, from his experience Dr. Vishnu knows that the number of patients is not constant throughout the year, instead, it follows a pattern. The number of patients on any given day of the year is given by the following formula:
##
##Patients per day = (6 – M)2 + |D – 15|
##where,
##M: the number of month starting from 1 to 12
##D: the date from 1 to 31
##
##All patients prefer without TV rooms as they are cheaper, but will opt for with TV rooms only if without TV rooms are not available. Hospital has a revenue target for the first year of operation. Given this target and the values of N, R1, and R2 you need to identify the number of TVs the hospital should buy so that it meets the revenue target. Assume the Hospital opens on 1st Jan and year is a non-leap year.
##
##Examples:
##
##
##
##Input: N = 20, R1 = 1500, R2 = 1000, target = 7000000
##Output: 14
##Explanation:
##Using the formula:
##The number of patients on 1st Jan will be 39, on 2nd Jan will be 38 and so on.
##Considering there are only twenty rooms and rates of both type of rooms are 1500 and 1000 respectively.
##Therefore, 14 TV sets are needed to get the revenue of 7119500 with 13 TV sets.
##The total revenue will be less than 7000000.
##
##Input: N = 10, R1 = 1000, R2 = 1500, target = 10000000
##Output: 10
##Explanation:
##In the above example, the target will not be achieved, even by equipping all the rooms with TV.
##Hence, the answer is 10 i.e., total number of rooms in the hospital.
##
##Recommended: Please try your approach on {IDE} first, before moving on to the solution.
##Approach: The idea is to traverse through the whole year and generate revenue for each day. Find the revenue for the first year for every possible number of rooms that can have a TV. Follow the below steps to solve the problem:
##
##Suppose the total number of rooms having a TV is tvs, where 0 ≤ tvs ≤ N.
##For each number for TVs, revenue for the first year can be found by traversing through each day.
##The above formula can be used to find the number of patients per day. Suppose np is the current number of patients.
##The current number of patients np can have the value of the number of patients today or the total number of rooms whichever is minimum.
##If the number of patients is less than the number of rooms without TV, then the total revenue for today will be np*R1 because it is cheap.
##Else if the number of patients is greater than the rooms without TV, then the total revenue for today is given by:
##(N – tvs)*R2 + (np – (N – tvs))*R1
##
##Add the revenue for each day in target value and print the maximum target value generated after checking all possible combinations.



def getPatients(M,D):
    return(((6-M)*(6-M))+ abs(D-15))

def countTV(n, r1, r2, target):
    #np, tvs, current_target = 0
    days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    for tvs in range(n+1):
        current_target = 0
        for m in range(12):
            for d in range(days[m]):
                np = getPatients(m,d)
                np = min(np,n)
                if np <= (n-tvs):
                    current_target += np*r2
                else:
                    current_target += ((n-tvs)*r2 + ((np-(n-tvs))*r1))
        if current_target >= target:
            break
    return (min(tvs,n))

N = 20#10
R1 = 1500#1000
R2 = 1000#1500
Target = 7000000#10000000
print(countTV(N, R1, R2, Target))




























