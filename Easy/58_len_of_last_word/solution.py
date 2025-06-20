###################
### 58. Length of Last Word
### Given a string s consisting of words and spaces,
### return the length of the last word in the string.

### A word is a maximal substring consisting of non-
### space characters only.
###################

######################### CONCEPTS COVERED #########################
# .SPLIT()
# LEN()
# NEGATIVE INDEXING

class Solution:
    # (self, s: str) = parameters (inputs) self and s
    # -> int return type hint: function returns an int
    def lengthOfLastWord(self, s: str) -> int:
        # input: string
        # output: string, no whitespace
        words_list = s.split()
        return len(words_list[-1])

s = Solution()
result = s.lengthOfLastWord(' fly me    to the moon  ')
print(result)