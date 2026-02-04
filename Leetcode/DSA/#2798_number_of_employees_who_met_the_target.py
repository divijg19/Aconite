# 2798. Number of Employees Who Met the Target
# https://leetcode.com/problems/number-of-employees-who-met-the-target/

def number_of_employees_who_met_the_target(hours, target):
    count = 0
    for hour in hours:
        if hour >= target:
            count += 1
    return count
