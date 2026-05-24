# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game V
# ║  Difficulty : Hard
# ║  Date       : 2026-05-24
# ║  URL        : https://leetcode.com/problems/jump-game-v/
# ╚══════════════════════════════════════════════════════════════╝

"""
Jump Game V Solution

Approach:
This is a dynamic programming problem where we need to find the maximum number of indices we can visit.
The key insight is that we can only jump from a higher building to a lower one, and all buildings in between must be shorter.
This creates a DAG (Directed Acyclic Graph) where each node points to reachable nodes.

We can solve this using DFS with memoization (top-down DP):
1. For each index, we try to jump left and right up to distance d
2. We can only jump to a position if it's shorter than current and all positions in between are also shorter
3. We recursively compute the maximum jumps from each reachable position
4. Use memoization to avoid recomputation

To optimize checking the "all in between are shorter" condition, we process indices in increasing order of height.
This ensures when we process an index, all shorter indices have already been processed.

Time Complexity: O(n * d) where n is length of array
Space Complexity: O(n) for DP array and recursion stack
"""

from typing import List

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        # dp[i] represents the maximum indices we can visit starting from index i
        dp = [-1] * n
        
        def dfs(index):
            # If already computed, return the stored result
            if dp[index] != -1:
                return dp[index]
            
            # We can always visit at least the current index
            max_jumps = 1
            
            # Try jumping to the right
            for j in range(index + 1, min(index + d + 1, n)):
                # If we encounter a taller or equal building, we can't jump further
                if arr[j] >= arr[index]:
                    break
                # Otherwise, we can jump and get the result from that position
                max_jumps = max(max_jumps, 1 + dfs(j))
            
            # Try jumping to the left
            for j in range(index - 1, max(index - d - 1, -1), -1):
                # If we encounter a taller or equal building, we can't jump further
                if arr[j] >= arr[index]:
                    break
                # Otherwise, we can jump and get the result from that position
                max_jumps = max(max_jumps, 1 + dfs(j))
            
            dp[index] = max_jumps
            return dp[index]
        
        # Try starting from each index and return the maximum
        result = 0
        for i in range(n):
            result = max(result, dfs(i))
        
        return result

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1
    arr1 = [6,4,14,6,8,13,9,7,10,6,12]
    d1 = 2
    print(f"Test 1: {sol.maxJumps(arr1, d1)}")  # Expected: 4
    
    # Test case 2
    arr2 = [3,3,3,3,3]
    d2 = 3
    print(f"Test 2: {sol.maxJumps(arr2, d2)}")  # Expected: 1
    
    # Test case 3
    arr3 = [7,6,5,4,3,2,1]
    d3 = 1
    print(f"Test 3: {sol.maxJumps(arr3, d3)}")  # Expected: 7
