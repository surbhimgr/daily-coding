# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Find the Number of Subsequences With Equal GCD
# ║  Difficulty : Hard
# ║  Date       : 2026-07-14
# ║  URL        : https://leetcode.com/problems/find-the-number-of-subsequences-with-equal-gcd/
# ╚══════════════════════════════════════════════════════════════╝

import collections

class Solution:
    """
    Problem Analysis:
    We need to find the number of pairs of disjoint non-empty subsequences (seq1, seq2) 
    such that GCD(seq1) == GCD(seq2).
    
    Let g be the common GCD value.
    For a fixed g, we want to find the number of ways to choose two disjoint 
    non-empty sets of indices I and J such that:
    GCD({nums[i] | i in I}) = g AND GCD({nums[j] | j in J}) = g.
    
    Approach:
    1. Let cnt[x] be the number of elements in nums that are multiples of x.
    2. For a fixed g, let f(g) be the number of ways to choose two disjoint 
       subsequences where both GCDs are MULTIPLES of g.
       - For an element to be part of a subsequence with GCD as a multiple of g, 
         the element itself must be a multiple of g.
       - Let C = cnt[g]. For each of these C elements, it can either:
         a) Be in seq1
         b) Be in seq2
         c) Be in neither
       - There are 3^C ways to distribute these C elements.
       - However, we must exclude cases where seq1 or seq2 are empty.
       - Using Inclusion-Exclusion:
         Total = 3^C
         Minus cases where seq1 is empty: 2^C (each element is either in seq2 or neither)
         Minus cases where seq2 is empty: 2^C (each element is either in seq1 or neither)
         Plus cases where both are empty: 1^C (all elements are in neither)
         So, f(g) = 3^C - 2 * 2^C + 1.
    
    3. Let h(g) be the number of ways to choose two disjoint non-empty 
       subsequences where both GCDs are EXACTLY g.
       - We know f(g) = sum(h(k)) for all k that are multiples of g.
       - By Mobius Inversion or simple reverse iteration (from max value down to 1), 
         we can find h(g) = f(g) - sum(h(k)) for k = 2g, 3g, ...
    
    4. The total answer is sum(h(g)) for all g from 1 to 200.

    Time Complexity: O(M log M + N), where M is the maximum value in nums (200) 
                     and N is the length of nums.
    Space Complexity: O(M).
    """
    def findTupes(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 200
        
        # Count frequencies of each number
        freq = collections.Counter(nums)
        
        # cnt[g] = number of elements in nums that are multiples of g
        cnt = [0] * (MAX_VAL + 1)
        for g in range(1, MAX_VAL + 1):
            for multiple in range(g, MAX_VAL + 1, g):
                cnt[g] += freq[multiple]
        
        # f[g] is the number of disjoint non-empty subsequences 
        # where both GCDs are multiples of g.
        f = [0] * (MAX_VAL + 1)
        for g in range(1, MAX_VAL + 1):
            C = cnt[g]
            # 3^C - 2*(2^C) + 1
            val = (pow(3, C, MOD) - 2 * pow(2, C, MOD) + 1) % MOD
            f[g] = val
            
        # h[g] is the number of disjoint non-empty subsequences 
        # where both GCDs are exactly g.
        h = [0] * (MAX_VAL + 1)
        for g in range(MAX_VAL, 0, -1):
            # Start with f[g] and subtract all h[k] where k is a multiple of g and k > g
            res = f[g]
            for k in range(2 * g, MAX_VAL + 1, g):
                res = (res - h[k]) % MOD
            h[g] = res
            
        return sum(h) % MOD

# To match the LeetCode class structure:
class Solution:
    def findNumberOfSubsequences(self, nums: list[int]) -> int:
        # This is the renamed method to match the problem's likely signature
        return self.findTupes(nums)

    def findTupes(self, nums: list[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 200
        freq = collections.Counter(nums)
        cnt = [0] * (MAX_VAL + 1)
        for g in range(1, MAX_VAL + 1):
            for multiple in range(g, MAX_VAL + 1, g):
                cnt[g] += freq[multiple]
        f = [0] * (MAX_VAL + 1)
        for g in range(1, MAX_VAL + 1):
            C = cnt[g]
            f[g] = (pow(3, C, MOD) - 2 * pow(2, C, MOD) + 1) % MOD
        h = [0] * (MAX_VAL + 1)
        for g in range(MAX_VAL, 0, -1):
            res = f[g]
            for k in range(2 * g, MAX_VAL + 1, g):
                res = (res - h[k]) % MOD
            h[g] = res
        return sum(h) % MOD
