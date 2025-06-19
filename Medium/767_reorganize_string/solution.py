###################
### 767. Reorganize String
### Given a string s, rearrange the characters of s so that any
### two adjacent characters are not the same.

### Return any possible rearrangement of s or return "" if not
### possible.
###################

######################### PROBLEM COVERS #########################
# COUNTER
# .VALUES()
# .ITEMS()
# WORST-CASE SPACING FORMULA
# SORTED
# LAMBDA
# SORTED()
# .JOIN()
# GREEDY STRATEGY

# importing counter to count char frequencies
from collections import Counter

class Solution:
    def reorganizeString(self, s: str) -> str:
        # count freq of each char (stored in dict)
        count = Counter(s)
        #print(count) # Counter({'a': 2, 'b': 1})

        # num of chars in string
        n = len(s)

        # first validation:
        # no char should appear more than (n + 1) // 2 times
        max_freq = max(count.values())
        if max_freq > (len(s) + 1) // 2:
            return ""
        
        # sort chars by decending freq
        sorted_chars = sorted(count.items(), key=lambda x: -x[-1])
        # count.items() returns [('a', 2), ('b', 1)]
        # (char, freq)

        # Prepare empty result list of length n
        res = [''] * n
        # fill even indices first (0, 2, 4, ...)
        i = 0 # pointer for index position is res

        for char, freq in sorted_chars:
            for _ in range(freq):
                res[i] = char # place char at curr index
                i += 2 # move to next even index
                if i >= n:
                    # if even indices full, place in odd indices (1, 3, ...)
                    i = 1

        # join list into string and return result
        return ''.join(res)
        


            
            

s = Solution()
result = s.reorganizeString('aabas')
print(result)