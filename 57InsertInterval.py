"""
INSTRUCTIONS
given
    array of non overlap intervals
    intervals[i] = [start_i, end_i]
    intervals is sorted asscending by start

    newInterval = [start, end]

insert newInterval into intervals
s.t. intervals is still sorted and no overlaps

rturn intervals after insertion. does not need to be in place

THINKING
since intervals are alread sorted by starts we can just
make a pass through them adding intervals to output as needed
make sure to insert interval when appropriate
thee appropriate time is when start fits into sorted order

3 cases
nested
overlap
disjoint

(EDGE) CASES
start = end in interval
end of one interval is exactly start of another
nested intervals
overlapping intervals
disjoint

examples
nested
[1, 5], [7, 9] new = [2, 4]
[1, 5], [7, 9] new = [0, 10]

overlap
[1, 5], [7, 9] new = [5, 7]
[1, 5], [7, 9] new = [5, 6]
[1, 5], [7, 9] new = [6, 7]
[1, 5], [7, 9] new = [8, 10]

disjoint
[1, 5], [7, 9] new = [6, 6]
[1, 5], [7, 9] new = [10, 11]

find "position" to insert interval
the see how many existing intervals it consumes or is consumed by. could be none, could be all

"""

from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        n = len(intervals)
        newBeg, newEnd = newInterval
        output = []

        i = 0
        while i < n:
            currBeg, currEnd = intervals[i]
            if currEnd < newBeg:
                output.append(intervals[i])
                i += 1
            else:
                break

        while i < n:
            currBeg, currEnd = intervals[i]
            if currBeg <= newEnd:
                newBeg = min(newBeg, currBeg)
                newEnd = max(newEnd, currEnd)
                i += 1
            else:
                break

        output.append([newBeg, newEnd])

        while i < n:
            output.append(intervals[i])
            i += 1

        return output


s = Solution()
assert s.insert([[1, 5], [7, 9]], [2, 4]) == [[1, 5], [7, 9]]
assert s.insert([[1, 5], [7, 9]], [0, 10]) == [[0, 10]]

assert s.insert([[1, 5], [7, 9]], [5, 7]) == [[1, 9]]
assert s.insert([[1, 5], [7, 9]], [5, 6]) == [[1, 6], [7, 9]]
assert s.insert([[1, 5], [7, 9]], [6, 7]) == [[1, 5], [6, 9]]
assert s.insert([[1, 5], [7, 9]], [8, 10]) == [[1, 5], [7, 10]]

assert s.insert([[1, 5], [7, 9]], [10, 11]) == [[1, 5], [7, 9], [10, 11]]
assert s.insert([[1, 5], [7, 9]], [6, 6]) == [[1, 5], [6, 6], [7, 9]]
