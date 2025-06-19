###################
### 9. Palindrome Number
### Given an integer x, return true if x is a palindrome,
### and false otherwise.
###################

######################### CONCEPTS COVERED #########################
# PALINDROME
# STR()
# STRING SLICING


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert x to string
        x_str = str(x)
        # slicing string
        return x_str == x_str[::-1]
    
s = Solution()
result = s.isPalindrome('121')
print(result)