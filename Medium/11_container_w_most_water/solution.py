###################
### 11. Container with Most Water
### You are given an integer array height of length n. There
### are n vertical lines drawn such that the two endpoints of 
### the ith line are (i, 0) and (i, height[i]).

### Find two lines that together with the x-axis form a container,
### such that the container contains the most water.

### Return the maximum amount of water a container can store.

### Notice that you may not slant the container.
###################

######################### PROBLEM COVERS #########################
# TWO POINTERS STRATEGY


from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # input: array of heights
        # output: area of the two highest nums w/ most space between

        left = 0 # first index
        right = len(height) - 1 # last index
        max_area = 0

        # while the leftmost index is less than the last index
        while left < right:
            # calculate area
            h = min(height[left], height[right])
            w = right - left
            area = h * w
            max_area = max(max_area, area)

            # move shorter line inward (so water doesn't spill over)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


s = Solution()
result = s.maxArea([1,8,6,2,5,4,8,3,7])
print(result)