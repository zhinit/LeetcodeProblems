"""
given
    sorted unique int array nums

a range [a, b] is the set of all ints from a to b inc

return
    smallest sorted list of ranges
    that cover all nums in the array exactly
    output range as string like "a->b" if a != b or "a"

its sorted AND nums are unique so all we need to do is put a range for consec ints
if nums[i] == nums[i-1] + 1
    expand range
else
    add prev range to output

at end dont for get the last range!!!!!
"""

from typing import List


class Solution:
    def SummaryRanges(self, nums: List[int]) -> List[str]:
        prevNum = float("-inf")
        output = []
        beg = end = 0
        for num in nums:
            if num != prevNum + 1:
                if prevNum != float("-inf"):
                    if beg == end:
                        output.append(str(beg))
                    else:
                        output.append(str(beg) + "->" + str(end))
                beg = num
                end = num
            else:
                end = num
            prevNum = num

        if prevNum != float("-inf"):
            if beg == end:
                output.append(str(beg))
            else:
                output.append(str(beg) + "->" + str(end))
        return output


s = Solution()
assert s.SummaryRanges([1, 3, 5]) == ["1", "3", "5"]
assert s.SummaryRanges([1, 2, 5]) == ["1->2", "5"]
assert s.SummaryRanges([1, 3, 4]) == ["1", "3->4"]
assert s.SummaryRanges([1, 2, 3, 4, 5]) == ["1->5"]
assert s.SummaryRanges([]) == []
assert s.SummaryRanges([1]) == ["1"]
