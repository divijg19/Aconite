# 27. Remove Element
# https://leetcode.com/problems/remove-element/

def remove_element(nums, val):
    write_index = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[write_index] = nums[i]
            write_index += 1

    return write_index
