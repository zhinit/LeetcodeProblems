"""
given
    unsorted array of ints: nums
return
    length of longest consec ele seq

must write this in O(n) time

an easy solution would be to just sort and then count sequences and store the longes
let's code this first and see if we can optimize it

we can use a first pass to create a set of nums
then we only compute the streak if we are at the lowest num on the second pass

"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        numSet = set(nums)

        longestStreak = 0

        for num in numSet:
            if num - 1 not in numSet:
                currNum = num
                currStreak = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currStreak += 1

                longestStreak = (
                    longestStreak if longestStreak > currStreak else currStreak
                )

        return longestStreak


s = Solution()
result = s.longestConsecutive([100, 4, 200, 1, 3, 2])
assert result == 4
result = s.longestConsecutive([5, 4, 3, 2, 1])
assert result == 5
result = s.longestConsecutive([5, 4, 100, 2, 1])
assert result == 2
result = s.longestConsecutive([])
assert result == 0
result = s.longestConsecutive([1])
assert result == 1
