# 1603. Design Parking System
# https://leetcode.com/problems/design-parking-system/


class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.capacity = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        self.capacity[carType] -= 1
        return self.capacity[carType] >= 0
