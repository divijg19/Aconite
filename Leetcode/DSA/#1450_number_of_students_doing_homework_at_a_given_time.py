# 1450. Number of Students Doing Homework at a Given Time
# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given

def busy_student(startTime, endTime, queryTime):
    count = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    return count
