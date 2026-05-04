"""
1. Two Sum
https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: Arrays & Hashing

Approach:
[scrivi qui in 2-4 righe il tuo ragionamento, in italiano o inglese
 come preferisci. Lo riempirai DOPO aver risolto.]

Time complexity:  O(?)
Space complexity: O(?)
"""

from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        # TODO: tua implementazione qui
        pass


# Quick local test
if __name__ == "__main__":
    sol = Solution()
    assert sol.two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.two_sum([3, 2, 4], 6) == [1, 2]
    assert sol.two_sum([3, 3], 6) == [0, 1]
    print("All tests passed.")