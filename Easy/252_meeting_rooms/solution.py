###################
### 252. Meeting Rooms
### Given an array of meeting time intervals where 
### intervals[i] = [starti, endi], determine if a person could attend
### all meetings.
###################

######################### CONCEPTS COVERED #########################
# .RANGE()

from typing import List
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # input: array of meeting times (e.g. [[7,10], [2,4]])
        # output: true or false (depending on if meetings overlap)

        # sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # compare adjacent meetings
        for i in range(1, len(intervals)):
            # if previous meeting ends after the current starts
            if intervals[i][0] < intervals[i-1][1]:
                return False
            
        return True
    
s = Solution()
result = s.canAttendMeetings([[7,10], [2,4]])
print(result)