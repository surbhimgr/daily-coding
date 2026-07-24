# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Number of Unique XOR Triplets II
# ║  Difficulty : Medium
# ║  Date       : 2026-07-24
# ║  URL        : https://leetcode.com/problems/number-of-unique-xor-triplets-ii/
# ╚══════════════════════════════════════════════════════════════╝

"""
Problem Analysis:
We need to find the number of unique values resulting from nums[i] XOR nums[j] XOR nums[k]
where i <= j <= k.
Let the elements be a, b, c.
Since i <= j <= k, we can pick the same index multiple times.
- If i = j = k, we get: a XOR a XOR a = a
- If i = j < k, we get: a XOR a XOR c = c
- If i < j = k, we get: a XOR c XOR c = a
- If i < j < k, we get: a XOR b XOR c

Essentially, we are looking for all unique values that can be formed by:
1. Single elements from the array: x
2. XOR of three distinct elements from the array: x ^ y ^ z

Notice that x XOR x XOR y = y, and x XOR y XOR y = x. 
So the case where two indices are the same simplifies to a single element.
The case where all three are the same also simplifies to a single element.

Thus, the problem reduces to finding the size of the set:
{nums[i]} UNION {nums[i] XOR nums[j] XOR nums[k] | i < j < k}

Constraints:
nums.length <= 1500, nums[i] <= 1500.
The maximum value of any element is 1500. The XOR sum of three such numbers 
will be less than 2048 (since 2^11 = 2048).

Complexity:
Time: O(N^2 * (max_val / 64)) or O(N^3) naive.
However, with N=1500, N^3 is too slow. 
We can optimize using bitsets. For every pair (i, j), we XOR their values 
and check which elements in the array XORed with this value create a new triplet.
Actually, a better approach:
The set of values is {nums[i]} UNION { (nums[i] ^ nums[j]) ^ nums[k] }.
Let S be the set of unique numbers in nums.
Let P be the set of all unique XOR sums of two distinct elements from S: {s1 ^ s2}.
Then the answer is the size of the set {p ^ s | p in P, s in S} UNION S.

Since S is small (max 1500 elements, max value 1500), we can iterate through all 
pairs in S and then all elements in S. But that's still O(|S|^3).
Given |S| <= 1500, O(|S|^3) is ~3.3 * 10^9, which is too slow for Python.
However, we can use Python's large integers as bitsets.
"""

from typing import List

class Solution:
    def solve(self, nums: List[int]) -> int:
        # Only unique numbers matter for the combinations
        # because x ^ x ^ y = y and x ^ y ^ y = x
        unique_nums = sorted(list(set(nums)))
        n = len(unique_nums)
        
        # The set of all possible results
        results_bitset = 0
        
        # Case 1: Single elements (covers i=j=k and i=j<k and i<j=k)
        for x in unique_nums:
            results_bitset |= (1 << x)
            
        # Case 2: Three distinct elements i < j < k
        # We want to find all unique values of (unique_nums[i] ^ unique_nums[j]) ^ unique_nums[k]
        # To optimize, we iterate through all pairs (i, j) and use a bitset 
        # representing all unique_nums to find all possible k.
        
        # Pre-calculate a bitset of all unique numbers available
        nums_bitset = 0
        for x in unique_nums:
            nums_bitset |= (1 << x)
            
        # We iterate through pairs i < j
        for i in range(n):
            val_i = unique_nums[i]
            for j in range(i + 1, n):
                val_ij = val_i ^ unique_nums[j]
                
                # We need k > j. Instead of checking k > j, we can just XOR 
                # val_ij with all available numbers.
                # If we XOR val_ij with unique_nums[k] where k < j, we get
                # unique_nums[i] ^ unique_nums[j] ^ unique_nums[k], which 
                # is just a permutation of the three distinct indices.
                # The only issue is if the result is already covered by Case 1.
                # But since we are using a bitset, it doesn't matter.
                
                # XORing a bitset by a value 'v' is not a simple shift.
                # However, we can iterate through the unique_nums again.
                # To optimize O(N^3) in Python, we need to avoid deep loops.
                pass

        # Correction: The O(N^3) is indeed too slow.
        # But wait, the max value is only 1500. 
        # The result of any XOR triplet is < 2048.
        # Let's use the property that there are only 2048 possible values.
        
        # Let's use a boolean array (or bitset) for the pairs.
        # pairs[x] = true if there exist i < j such that nums[i] ^ nums[j] = x
        pairs = [False] * 2048
        for i in range(n):
            for j in range(i + 1, n):
                pairs[unique_nums[i] ^ unique_nums[j]] = True
        
        # Now we check all pairs combined with all single elements
        final_results = [False] * 2048
        # Single elements
        for x in unique_nums:
            final_results[x] = True
            
        # Triplets (distinct)
        # If a value 'p' is a XOR of two distinct elements (i, j), 
        # then p ^ unique_nums[k] is a triplet.
        # To ensure i, j, k are distinct, we must be careful.
        # But the problem says i <= j <= k.
        # If we pick any two indices (i, j) and any index k:
        # 1. i < j < k -> Valid distinct triplet.
        # 2. i < j and k = i -> unique_nums[i] ^ unique_nums[j] ^ unique_nums[i] = unique_nums[j] (Case 1)
        # 3. i < j and k = j -> unique_nums[i] ^ unique_nums[j] ^ unique_nums[j] = unique_nums[i] (Case 1)
        # 4. i < j and k < i -> valid distinct triplet (just a permutation of indices).
        
        # Therefore, any p ^ unique_nums[k] where p is a XOR of two distinct elements
        # and k is any index will result in either a single element or a 3-distinct-element XOR.
        
        # To handle "distinct" correctly: 
        # If p = unique_nums[i] ^ unique_nums[j] and we XOR it with unique_nums[k],
        # if k == i or k == j, we get a single element.
        # if k != i and k != j, we get a distinct triplet.
        # So we just need to check all p in pairs and all s in unique_nums.
        
        for p in range(2048):
            if pairs[p]:
                for s in unique_nums:
                    final_results[p ^ s] = True
                    
        return sum(final_results)

# Time Complexity: O(N^2 + 2048 * N)
# Space Complexity: O(2048)
