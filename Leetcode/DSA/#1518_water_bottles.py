# 1518. Water Bottles
# https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = 0
        empty_bottles = 0

        while numBottles > 0:
            # Drink all the current full bottles
            total_drunk += numBottles
            empty_bottles += numBottles

            # Exchange empty bottles for new full bottles
            numBottles = empty_bottles // numExchange
            empty_bottles = empty_bottles % numExchange

        return total_drunk
