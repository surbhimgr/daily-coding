# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Number of ZigZag Arrays I
# ║  Difficulty : Hard
# ║  Date       : 2026-06-23
# ║  URL        : https://leetcode.com/problems/number-of-zigzag-arrays-i/
# ╚══════════════════════════════════════════════════════════════╝

import collections

"""
Problem Analysis:
A ZigZag array of length n must satisfy:
1. Elements in range [l, r].
2. Adjacent elements are not equal: a[i] != a[i+1].
3. No three consecutive elements are strictly increasing or strictly decreasing.
   This means if a[i] < a[i+1], then we must have a[i+1] > a[i+2].
   If a[i] > a[i+1], then we must have a[i+1] < a[i+2].

Dynamic Programming State:
Let dp[i][val][direction] be the number of ZigZag arrays of length i ending with value 'val'.
- direction = 0: The current element 'val' is GREATER than the previous element (upward slope).
- direction = 1: The current element 'val' is SMALLER than the previous element (downward slope).

Transitions for length i+1:
- To end with direction 0 (upward): the previous state must have been direction 1 (downward), 
  and the new value must be greater than the previous value.
- To end with direction 1 (downward): the previous state must have been direction 0 (upward), 
  and the new value must be smaller than the previous value.

Base Case (n=2):
For every pair (v1, v2) where l <= v1, v2 <= r and v1 != v2:
- If v1 < v2, it's an 'up' transition to v2.
- If v1 > v2, it's a 'down' transition to v2.

Complexity:
- Time Complexity: O(n * (r-l)), since we use prefix sums to transition in constant time per value.
- Space Complexity: O(r-l) to store the DP states for the current and previous lengths.
"""

class Solution:
    def solve(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        # Normalize range to [0, m-1]
        m = r - l + 1
        
        # dp_up[v] is the number of arrays ending with value v, where v > previous
        # dp_down[v] is the number of arrays ending with value v, where v < previous
        dp_up = [0] * m
        dp_down = [0] * m
        
        # Base case for n = 2
        # For a fixed v2, any v1 < v2 creates an 'up' transition.
        # There are v2 such values (0, 1, ..., v2-1).
        for v in range(m):
            dp_up[v] = v
            dp_down[v] = (m - 1) - v
            
        # Transition from length 2 up to n
        for i in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m
            
            # To calculate new_up[v], we need sum of dp_down[prev] where prev < v.
            # To calculate new_down[v], we need sum of dp_up[prev] where prev > v.
            
            # Prefix sums for dp_down to optimize new_up
            prefix_down = 0
            for v in range(m):
                new_up[v] = prefix_down % MOD
                prefix_down += dp_down[v]
                
            # Suffix sums for dp_up to optimize new_down
            suffix_up = 0
            for v in range(m - 1, -1, -1):
                new_down[v] = suffix_up % MOD
                suffix_up += dp_up[v]
                
            dp_up = new_up
            dp_down = new_down
            
        return (sum(dp_up) + sum(dp_down)) % MOD

# To match LeetCode's class structure:
class SolutionWrapper(Solution):
    def numberOfZigZagArrays(self, n: int, l: int, r: int) -> int:
        return self.solve(n, l, r)

# Note: In LeetCode, the method name is usually numberOfZigZagArrays.
# I've used a wrapper for clarity.
