# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game VII
# ║  Difficulty : Medium
# ║  Date       : 2026-05-25
# ║  URL        : https://leetcode.com/problems/jump-game-vii/
# ╚══════════════════════════════════════════════════════════════╝

from collections import deque

class Solution:
    """
    Problem Analysis:
    We need to determine if the last index of a binary string is reachable from index 0.
    A jump from index i to index j is valid if:
    1. minJump <= j - i <= maxJump
    2. s[j] == '0'

    Approach:
    This is a reachability problem that can be solved using Dynamic Programming.
    Let dp[i] be true if index i is reachable.
    dp[i] = (s[i] == '0') AND (there exists j such that dp[j] is true AND minJump <= i - j <= maxJump)

    To optimize the search for j, we use a sliding window (via a Queue) to keep track of 
    all indices 'j' that are currently reachable and within the range [i - maxJump, i - minJump].

    Time Complexity: O(n), where n is the length of the string. Each index is added and removed from the queue at most once.
    Space Complexity: O(n) to store the reachability state or the queue.
    """

    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
        
        # Queue stores indices 'j' that are reachable and could potentially 
        # satisfy the jump condition for future indices.
        reachable_indices = deque([0])
        
        # We iterate through the string starting from the first possible jump destination
        for i in range(1, n):
            # 1. Maintain the window: Remove indices from the queue that are too far back
            # to reach index i (i - j > maxJump)
            while reachable_indices and i - reachable_indices[0] > maxJump:
                reachable_indices.popleft()
            
            # 2. Check if index i is reachable:
            # It must be '0' and there must be a reachable index 'j' in the queue
            # that satisfies the minJump requirement (i - j >= minJump).
            if s[i] == '0' and reachable_indices and i - reachable_indices[0] >= minJump:
                # If we reached the last index, we can return True immediately
                if i == n - 1:
                    return True
                # Otherwise, add this index to the queue as a potential starting point for future jumps
                reachable_indices.append(i)
                
        return False

# Example usage:
# sol = Solution()
# print(sol.canReach("011010", 2, 3)) # Output: True
# print(sol.canReach("01101110", 2, 3)) # Output: False
