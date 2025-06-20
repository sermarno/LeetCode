###################
### 202. Happy Number
### Write an algorith to determine if a number n is happy.
### A happy number is a number defined by the following
### process:
### - Starting with any positive integer, replace the number
###   by the sum of the square of its digits.
### - Repeat the process until the number equals 1 (where it 
###   will stay), or it loops endlessly in a cycle which does
###   not include 1.
### - Those numbers for which the process ends in 1 are happy.
### Return true if n is happy, else false.
###################

######################### CONCEPTS COVERED #########################
# SET()

class Solution:
    def isHappy(self, n: int) -> bool:
        # initializing empty set to keep track of nums processed
        seen = set()

        # while the value in the set is not 1
        while n != 1:
            # if value is found again, it can't become 1
            if n in seen:
                return False # repeated number = loop
            seen.add(n) # records number as seen in set

            # converting num to string to iterate over nums
            # str(n): converting n into str to iterate values
            # int(digit): converting back to int for operations
            # sum(): adding the squares
            n = sum(int(digit) ** 2 for digit in str(n))
        return True


s = Solution()
result = s.isHappy(19)
print(result)