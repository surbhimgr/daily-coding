# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Partition Array According to Given Pivot
# ║  Difficulty : Medium
# ║  Date       : 2026-06-08
# ║  URL        : https://leetcode.com/problems/partition-array-according-to-given-pivot/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem: Partition Array According to Given Pivot
    
    The goal is to rearrange the array such that:
    1. Elements < pivot come first.
    2. Elements == pivot come second.
    3. Elements > pivot come last.
    
    Crucially, the relative order of elements within each category must be preserved.
    This implies a stable partition.
    
    Approach:
    Since we need to maintain relative order, the simplest and most effective 
    way is to iterate through the array and categorize elements into three 
    separate lists (less, equal, greater), then concatenate them.
    
    Time Complexity: O(n) - We traverse the input array once and the 
                     result lists once.
    Space Complexity: O(n) - We use auxiliary space to store the partitioned elements.
    """
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # Initialize three lists to hold elements based on their relation to the pivot
        less = []
        equal = []
        greater = []
        
        # Single pass through the array to categorize each element
        # This maintains the relative order as we process indices from 0 to n-1
        for x in nums:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            else:
                greater.append(x)
        
        # Concatenate the lists in the required order: less < equal < greater
        # In Python, list concatenation (+) creates a new list containing all elements
        return less + equal + greater

# Example usage:
# sol = Solution()
# print(sol.pivotArray([9,12,5,10,14,3,10], 10)) # Expected: [9,5,3,10,10,12,14]
# print(sol.pivotArray([-3,4,3,2], 2))          # Expected: [-3,2,4,3]
