###################
### 347. Top K Frequent Elements
### Given an integer array nums and an integer k,
### return the k most frequent elements. You may
### return the answer in any order.
###################

######################### PROBLEM COVERS #########################
# 

from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input: list and integer
        # output: list with top k most freq nums
        nums_count = {}

        for num in nums:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
        
        # sort by frequency decending to get most frequent
        sorted_items = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)

        # grab top k elements
        top_k = [num for num, count in sorted_items[:k]]

        return top_k


s = Solution()
result = s.topKFrequent([1,1,1,2,2,3], 2)
print(result)