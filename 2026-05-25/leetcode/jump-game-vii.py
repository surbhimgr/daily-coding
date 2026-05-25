# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game VII
# ║  Difficulty : Medium
# ║  Date       : 2026-05-25
# ║  URL        : https://leetcode.com/problems/jump-game-vii/
# ╚══════════════════════════════════════════════════════════════╝

import collections

class Solution:
    """
    Problem: Jump Game VII
    The goal is to determine if we can reach the end of a binary string starting from index 0,
    jumping only to indices containing '0' within the range [i + minJump, i + maxJump].
    
    Approach:
    We use Dynamic Programming combined with a sliding window (prefix sum/counter) 
    to efficiently check if any reachable index exists within the current jump range.
    
    Let dp[i] be True if index i is reachable from index 0.
    For dp[j] to be True, there must exist an index i such that:
    1. dp[i] is True
    2. j - maxJump <= i <= j - minJump
    3. s[j] == '0'
    
    Instead of iterating through all i for every j, we maintain a count of 'True' values 
    in the window [j - maxJump, j - minJump]. If the count > 0 and s[j] == '0', then dp[j] is True.
    
    Time Complexity: O(N), where N is the length of the string. We traverse the string once.
    Space Complexity: O(N) to store the DP array.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # dp[i] indicates if index i is reachable
        dp = [False] * n
        dp[0] = True
        
        # reachable_count keeps track of how many indices in the current 
        # window [i - maxJump, i - minJump] are reachable.
        reachable_count = 0
        
        # We start checking reachability from index 1 to n-1
        for i in range(1, n):
            # The window for index i is [i - maxJump, i - minJump]
            
            # 1. Add the new index entering the window from the right: (i - minJump)
            # Only add if the index is within bounds
            if i - minJump >= 0:
                if dp[i - minJump]:
                    reachable_count += 1
            
            # 2. Remove the index leaving the window from the left: (i - maxJump - 1)
            # If the index that just fell out of the window was reachable, decrement count
            if i - maxJump - 1 >= 0:
                if dp[i - maxJump - 1]:
                    reachable_count -= 1
            
            # 3. If there is at least one reachable index in the window 
            # and the current cell is '0', current cell becomes reachable.
            if s[i] == '0' and reachable_count > 0:
                dp[i] = True
        
        return dp[n - 1]

# Example usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Expected: True
# print(sol.canReach("01101110", 2, 3)) # Expected: False
