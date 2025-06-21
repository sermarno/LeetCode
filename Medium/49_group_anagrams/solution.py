###################
### 49. Group Anagrams
### Given an array of strings strs, group the anagrams
### together. You can return the answer in any order.
###################

######################### PROBLEM COVERS #########################
# ANAGRAMS
# SORTED()
# DICTIONARYS
# LIST() WITH .VALUES()

from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams: string with same chars & same num of chars
        # input: list of strings
        # output: list of lists

        # dict to map sorted chars to list of words
        anagram_groups = {}

        # loop through each word in list of words
        for word in strs:
            # sort alphabetically
            # E.g. 'eat' -> ['a', 'e', 't']
            sorted_words = sorted(word)

            # converting back to string to use as dict key
            # E.g. ['a', 'e', 't'] -> 'aet'
            key = ''.join(sorted_words)

            # appending original word to dictionary
            if key in anagram_groups:
                anagram_groups[key].append(word)
            else:
                anagram_groups[key] = [word]

        # anagram_groups.values will return 
        # dict_values([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])
        # using list() removes dict_values()
        return list(anagram_groups.values())
                

s = Solution()
result = s.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
print(result)