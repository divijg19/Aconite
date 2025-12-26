# 1732. Find the highest altitude
# https://leetcode.com/problems/find-the-highest-altitude/

def largestAltitude(gain):
    altitude = 0
    max_altitude = 0
    for i in gain:
        altitude += i
        if altitude > max_altitude:
            max_altitude = altitude
    return max_altitude