###################
### 648. Replace Words
### In English, we have a concept called root, which can
### be followed by some other word to form another
### longer word - let's call this a derivative. For
### example, when the root "help" is followed by the
### word "ful", we can form "helpful".

### Given a dictionary consisting of many roots and a 
### sentence consisting of words separated by spaces,
### replace all derivatives in the sentence with the root
### forming it. If a derivative can be replaced by more
### than one root, replace it with the root that has the
### shortest length.

### Return the sentence after the replacement.
###################

######################### PROBLEM COVERS #########################
# 

from typing import List
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        # converting string into list of words
        words = sentence.split() # ['the', 'cattle', 'was', 'rattled', 'by', 'the', 'battery']

        # dictionary to look up words
        dictionary_set = set(dictionary)
        print(dictionary_set)

        # loop through words
        for i in range(len(words)):
            word = words[i]
            for j in range(1, len(word) + 1):
                prefix = word[:j]
                if prefix in dictionary_set:
                    words[i] = prefix
                    break
        return " ".join(words)
                


s = Solution()
dictionary = ['cat', 'bat', 'rat']
sentence = "the cattle was rattled by the battery"
result = s.replaceWords(dictionary, sentence)
print(result)