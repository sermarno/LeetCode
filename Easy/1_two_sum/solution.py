###################
### 1. Two Sum
### Given an array of integers nums and an integer target, return indices of the two
### numbers such that they add up to target. You may assume that each input would have 
### exactly one solution, and you may not use the same element twice.
### You can return the answer in any order.
###################

######################### CONCEPTS COVERED #########################
# CLASSES 
# DICTIONARYS
# FOR LOOP
# ENUMERATE
# INSTANCE OF CLASS
# CALLING METHOD


class Solution(object):
    #defining a method that takes nums (list of ints) and target value
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # dictionary to store each value and index position
        # val_ind = {value: index, value: index...}
            # nums = [1, 5, 11, 19]
            # val_ind = {1: 0, 5: 1, 11: 2, 19: 3}
        val_ind = {}

        # looping through list for value and index position with enumerate
            # for each index, value in nums list
            # enumerate: first loop - i = 0; num = 1
            #            second loop - i = 1; num = 5 ...
        for i, num in enumerate(nums):
            # finding complement = value needed for target
            # first loop = i = 0; num = 1; so 6 - 1 = 5
            comp = target - num
            # if comp is in list
                # nums = [1, 5, 11, 19]
                # first loop: 5 is in list !
                # second loop: 1 is in list !
            if comp in val_ind:
                # return pair(list) of indices
                # val_ind[comp] = index where comp was 
                # i = index of current num
                return [val_ind[comp], i] # returns [0, 1]
                # nums at index 0 and 1 (1 + 5) add up to 6.

            # stores current num in dictionary to be matched later
            val_ind[num] = i


#nums and target values
nums = [1, 5, 11, 19]
target = 6

#creating instance of class and calling its method
s = Solution()
answer = s.twoSum(nums, target)
print(answer)