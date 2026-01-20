from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        numIndices = {}
        for i in range(n):
            num = nums[i]
            if num in numIndices:
                j = numIndices[num]
                if i - j <= k:
                    return True
            numIndices[num] = i
        return False


s = Solution()
assert s.containsNearbyDuplicate([1, 1, 3, 4], 1) == True  # 1-0 <= 1
assert s.containsNearbyDuplicate([1, 1, 3, 4], 2) == True  # 1-0 <= 2
assert s.containsNearbyDuplicate([1, 1, 3, 4], 0) == False  # 1-0 not <= 0

assert s.containsNearbyDuplicate([1], 0) == False  # there are not 2 distinct indices
assert s.containsNearbyDuplicate([1], 1) == False  # there are not 2 distinct indices
assert s.containsNearbyDuplicate([1], 2) == False  # there are not 2 distinct indices

assert (
    s.containsNearbyDuplicate([-10_000, 1, 4, 10_000, -10_000], 4) == True
)  # 4-0 <= 4
assert (
    s.containsNearbyDuplicate([-10_000, 1, 4, 10_000, -10_000], 100) == True
)  # 4-0 <= 4
assert (
    s.containsNearbyDuplicate([-10_000, 1, 4, 10_000, -10_000], 3) == False
)  # 4-0 <= 4
