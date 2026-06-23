# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Maximum Building Height
# ║  Difficulty : Hard
# ║  Date       : 2026-06-20
# ║  URL        : https://leetcode.com/problems/maximum-building-height/
# ╚══════════════════════════════════════════════════════════════╝

"""
Problem Analysis:
The goal is to find the maximum height any building can reach given:
1. Building 1 starts at height 0.
2. Height difference between adjacent buildings is at most 1.
3. Certain buildings have a maximum height restriction.

Approach:
The height of a building is constrained by:
- The distance from building 1 (height 0).
- The restrictions given in the `restrictions` array.
- The distance from other restricted buildings.

Specifically, if building 'i' has height 'h_i' and building 'j' has height 'h_j', 
then |h_i - h_j| <= |i - j|.

We can solve this using a two-pass approach (similar to the "Trapping Rain Water" 
or "Candy" problems) but on a sparse set of points:
1. Add building 1 (height 0) and building n (max possible height n-1) to the restrictions.
2. Sort restrictions by building index.
3. Forward Pass: Ensure height constraints are respected moving from building 1 to n.
   If building i is at height h_i, building j (j > i) cannot exceed h_i + (j - i).
4. Backward Pass: Ensure constraints are respected moving from building n back to 1.
   If building j is at height h_j, building i (i < j) cannot exceed h_j + (j - i).
5. Calculate the peak height between any two adjacent restricted buildings i and j.
   The maximum height between i and j is: 
   floor((h_i + h_j + (j - i)) / 2).

Time Complexity: O(R log R), where R is the number of restrictions.
Space Complexity: O(R) to store the processed restrictions.
"""

from typing import List

class Solution:
    def maximizeH(self, n: int, restrictions: List[List[int]]) -> int:
        # 1. Prepare constraints. Add building 1 with height 0.
        # We treat the end building 'n' as a restriction with max height 'n-1'.
        res = sorted(restrictions)
        res = [[1, 0]] + res + [[n, n - 1]]
        
        # 2. Forward Pass: Propagate constraints from left to right
        # height[i] = min(height[i], height[i-1] + (id[i] - id[i-1]))
        for i in range(1, len(res)):
            res[i][1] = min(res[i][1], res[i-1][1] + (res[i][0] - res[i-1][0]))
            
        # 3. Backward Pass: Propagate constraints from right to left
        # height[i] = min(height[i], height[i+1] + (id[i+1] - id[i]))
        for i in range(len(res) - 2, -1, -1):
            res[i][1] = min(res[i][1], res[i+1][1] + (res[i+1][0] - res[i][0]))
            
        max_h = 0
        
        # 4. Calculate the local maximum between every two adjacent restricted buildings
        for i in range(len(res) - 1):
            id1, h1 = res[i]
            id2, h2 = res[i+1]
            
            # The max height between two points (x1, y1) and (x2, y2) 
            # with slope constraint 1 is given by:
            # h = floor((h1 + h2 + (id2 - id1)) / 2)
            # Example: (1, 0) and (4, 1) -> (0 + 1 + 3)//2 = 2. Heights: 0, 1, 2, 1.
            current_max = (h1 + h2 + (id2 - id1)) // 2
            max_h = max(max_h, current_max)
            
        return max_h
