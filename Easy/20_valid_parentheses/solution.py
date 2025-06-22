###################
### 20. Valid Parentheses
### Given a string s containing just the characters '(',
### ')', '{', '}', '[', and ']', determine if the input
### string is valid.

### Valid if:
###     - Open brackets must be closed by same type 
###       of brackets
###     - Open brackets must be closed in the correct
###       order
###     - Every close bracket has a corresponding open
###       bracket of same type
###################

######################### CONCEPTS COVERED #########################
# 


class Solution:
    def isValid(self, s: str) -> bool:
        # input: string - brackets
        # output: boolean - true if string is valid

        # empty list to store
        stack = []
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        # loop through chars in string
        for char in s:
            # checking if the char is a key in the bracket map dict
            # if something in dict: - always checks the keys
            # if something in dict.values() - checks the values
            if char in bracket_map:
                # if the stack is not empty, get top item by popping it
                # if empty, assign # that will never match a bracket
                top = stack.pop() if stack else '#'
                if bracket_map[char] != top:
                    return False
            else:
                stack.append(char)

        return not stack
            


s = Solution()
result = s.isValid('()[]{}')
print(result)