# 1672. Richest Customer Wealth
# https://leetcode.com/problems/richest-customer-wealth/

def maximumWealth(accounts):
    max_wealth = 0
    for customer in accounts:
        wealth = sum(customer)
        if wealth > max_wealth:
            max_wealth = wealth
    return max_wealth

print("Maximum wealth in [[1,2,3],[3,2,1]]:", maximumWealth([[1,2,3],[3,2,1]]))
print("Maximum wealth in [[1,5],[7,3],[3,5]]:", maximumWealth([[1,5],[7,3],[3,5]]))