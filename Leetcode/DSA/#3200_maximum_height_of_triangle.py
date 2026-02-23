# 3200. Maximum Height of Triangle
# https://leetcode.com/problems/maximum-height-of-triangle/

import math


class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def get_h(m, n):
            def h_for_odds(n):
                return int(math.sqrt(n))

            def h_for_evens(n):
                m = int(math.sqrt(n))
                if m * (m + 1) > n:
                    m -= 1
                return m

            h_odds = h_for_odds(m)
            h_evens = h_for_evens(n)

            if h_odds == h_evens:
                return h_odds * 2
            elif h_odds > h_evens:
                return h_evens * 2 + 1
            else:
                return h_odds * 2

        return max(get_h(red, blue), get_h(blue, red))
