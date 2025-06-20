###################
### 217. Contains Duplicate
### Given an integer array nums, return true if any value appears
### at least twice in the array, and return false if every
### element is distinct.
###################

######################### CONCEPTS COVERED #########################

from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # creating an empty dict to store seen nums
        numbers = {}
        # looping through values in list
        for num in nums:
            # if the value is in the dict
            if num in numbers:
                # return true
                return True
            # mark num as seen by setting val to true
            numbers[num] = True
        return False
    

s = Solution()
result = s.containsDuplicate([1,2,3,1])
print(result)