###################
### 3. Longest Substring Without Repeating Characters
### Given a string s, find the length of the longest
### substring without duplicate characters.
###################

######################### PROBLEM COVERS #########################
# SUBSTRINGS
# DATA TYPES / STRUCTURES
# SET()
# WHILE LOOP
# LEFT/RIGHT POINTERS


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # length of longest substring without repeating chars:
        # must find: a continuous section (substring), section must contain
        # no duplicates, need to return the length of the longest one
        """
        :type s: str
        :rtype: int
        """

        # set to store unique chars in curr window
        seen = set()

        # defining points for window (for tracking start and end)
        left = 0

        # tracking max length found
        max_length = 0

        # iterate through string with right pointer
        for right in range(len(s)):
            # if dup char is found, shrink window from left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # add curr char to set
            seen.add(s[right])
            # update max_length if curr window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
# instance of solution
s = Solution()

answer = s.lengthOfLongestSubstring("abcabcbb")

print(answer)

# "pwwkew":
# left 0, right 0, char 'p', seen {'p'}, action: add 'p', max_length 1
# left 0, right 1, char 'w', seen {'p', 'w'}, action: add 'w', max_length 2
# left 0, right 2, char 'w', seen {}, action: add 'w', max_length 2
# left 2, right 3, char 'k', seen {'w', 'k'}, action: add 'k', max_length 2
# left 2, right 4, char 'e', seen {'w', 'k', 'e'}, action: add 'e', max_length 3
# left 2, right 5, char 'w', seen {'w', 'k', 'e'}, action: keep max 3