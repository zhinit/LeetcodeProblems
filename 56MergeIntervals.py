"""
Given
    array of intervals
    intervals[i] = [start_i, end_i]

merge all overlapping intervals

return
    array of non overlapp intervals

when we encounter a new interval we should have a data structure to hold past intervals
we need to updata this ds with the new interval

how do we know if it is a new range or within existing interval

seems like sorting would help
do we sort by start or end?

we can probably sort by end time and use greedy approach
we know start is always before end a duhhh

may be we dont need a ds after all
we just need to keep track of curr interval end and append when we get a new

what if we sorted in decreasing order
[0, 10][5, 7][1, 3]

start with [0, 10]
intBeg = 0
intEnd = 10

next is [5, 7]
since currBeg = 5 >= 0 = intBeg this is contained in prev interval

so for each new interval either
    the int is contained if currBeg >= intBeg
    the int is extened if currBeg < intBeg and currEnd >= intBeg
        so update intBeg = currBeg
    we end prev int and start a new one
    else meaning currBeg < intBeg and currEnd < intBeg
append remaining int
after loop append final interval!!!!!!!!

sort is O(nlogn) where n is the number of intervals
then out pass throught the intervalse is just O(n)

so in total the runtime is O(nlogn)
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        intervals.sort(key=lambda x: x[1], reverse=True)
        output = []
        intBeg, intEnd = intervals[0]
        for i in range(1, n):
            currBeg, currEnd = intervals[i]
            if currBeg >= intBeg:  # nested
                pass
            elif currBeg < intBeg and currEnd >= intBeg:  # extend
                intBeg = currBeg
            else:  # non overlap so start anew
                output.append([intBeg, intEnd])
                intBeg = currBeg
                intEnd = currEnd
        output.append([intBeg, intEnd])
        return output


def norm(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))


s = Solution()
assert norm(s.merge([[1, 5], [15, 20], [3, 7], [5, 10]])) == norm([[1, 10], [15, 20]])
assert norm(s.merge([[1, 5], [3, 7], [5, 10], [15, 20]])) == norm([[1, 10], [15, 20]])
assert norm(s.merge([[15, 20], [1, 5], [3, 7], [5, 10]])) == norm([[1, 10], [15, 20]])

assert norm(s.merge([[1, 5], [10, 12], [12, 15]])) == norm([[1, 5], [10, 15]])

assert norm(s.merge([[1, 1]])) == norm([[1, 1]])
assert norm(s.merge([[1, 1]])) == norm([[1, 1]])

assert norm(s.merge([[1, 4], [0, 4]])) == norm([[0, 4]])
assert norm(s.merge([[1, 4], [2, 3]])) == norm([[1, 4]])
assert norm(s.merge([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]])) == norm([[1, 10]])
