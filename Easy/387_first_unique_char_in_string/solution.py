###################
### 387. First Unique Character in a String
### Given a string s, find the first non-repeating character
### and return it's index. If it doesn't exist, return -1.
###################

######################### CONCEPTS COVERED #########################
# ENUMERATE()
# FOR LOOP
# IF ELSE
# DICTIONARY

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # empty dict to store char count
        char_count = {}
        # for each index and character in dict of s
        for i, char in enumerate(s):
            # add each char and it's count to dict
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        # last loop to see if char is repeating
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        return - 1
            
s = Solution()
result = s.firstUniqChar('loveleetcode')
print(result)