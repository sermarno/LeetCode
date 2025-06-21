###################
### 14. Longest Common Prefix
### Write a function to find the longest common prefix
### strong amongst an array of strings.

### if there is no common prefix, return an empty
### "" string.
###################

######################### CONCEPTS COVERED #########################
# .STARTSWITH()

from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # input: list of strings
        # output: similar chars in strings

        # start with first word as prefix
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
                
        return prefix


            

s = Solution()
result = s.longestCommonPrefix(['flower', 'flow', 'flight'])
print(result) # should be fl