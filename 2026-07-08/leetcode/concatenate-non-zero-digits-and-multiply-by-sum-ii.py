# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Concatenate Non-Zero Digits and Multiply by Sum II
# ║  Difficulty : Medium
# ║  Date       : 2026-07-08
# ║  URL        : https://leetcode.com/problems/concatenate-non-zero-digits-and-multiply-by-sum-ii/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem Analysis:
    For each query [l, r], we need to find the number x formed by concatenating
    non-zero digits in the substring s[l...r] and the sum of these digits.
    The result is (x * sum) % (10^9 + 7).

    Approach:
    1. Use Prefix Sums for digit sums:
       pre_sum[i] = sum of digits in s[0...i-1].
       Sum of digits in s[l...r] = pre_sum[r+1] - pre_sum[l].
    
    2. Use Prefix Sums for the value x:
       Let non-zero digits be d1, d2, ..., dk. 
       The value x is d1*10^{k-1} + d2*10^{k-2} + ... + dk*10^0.
       To calculate this for a range [l, r], we need:
       - The number of non-zero digits in s[0...i-1] (count[i]).
       - A prefix value array: pre_val[i] = (s[0...i-1] non-zero digits) % MOD.
       
       If s[l...r] has k non-zero digits, and we denote the number of non-zero
       digits in s[0...l-1] as c_l and in s[0...r] as c_r, then:
       x = (pre_val[r+1] - pre_val[l] * 10^(c_r - c_l)) % MOD.

    Time Complexity: O(m + q) where m is length of string and q is number of queries.
    Space Complexity: O(m) to store prefix arrays.
    """

    def concatenateNonZeroDigitsAndMultiplyBySum(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        m = len(s)
        
        # pre_sum[i]: sum of digits from index 0 to i-1
        pre_sum = [0] * (m + 1)
        # pre_count[i]: count of non-zero digits from index 0 to i-1
        pre_count = [0] * (m + 1)
        # pre_val[i]: value formed by non-zero digits from index 0 to i-1 modulo MOD
        pre_val = [0] * (m + 1)
        
        # Precompute powers of 10 to avoid repeated pow() calls inside the loop
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i-1] * 10) % MOD
            
        curr_sum = 0
        curr_count = 0
        curr_val = 0
        
        for i in range(m):
            digit = int(s[i])
            if digit != 0:
                curr_sum += digit
                curr_count += 1
                # Shift existing value left by 1 (multiply by 10) and add current digit
                curr_val = (curr_val * 10 + digit) % MOD
            
            pre_sum[i+1] = curr_sum
            pre_count[i+1] = curr_count
            pre_val[i+1] = curr_val
            
        results = []
        for l, r in queries:
            # 1. Calculate sum of digits in range [l, r]
            s_val = pre_sum[r+1] - pre_sum[l]
            
            # 2. Calculate the concatenated value x in range [l, r]
            # Formula: x = (pre_val[r+1] - pre_val[l] * 10^(count[r+1] - count[l])) % MOD
            count_in_range = pre_count[r+1] - pre_count[l]
            
            if count_in_range == 0:
                results.append(0)
                continue
                
            # Calculate x using modular arithmetic
            # We subtract the contribution of the prefix before index 'l'
            # shifted by the number of non-zero digits found within the range.
            x = (pre_val[r+1] - (pre_val[l] * pow10[count_in_range])) % MOD
            
            # Result is (x * s_val) % MOD
            results.append((x * s_val) % MOD)
            
        return results
