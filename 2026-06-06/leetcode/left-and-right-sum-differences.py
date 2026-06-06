# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Left and Right Sum Differences
# ║  Difficulty : Easy
# ║  Date       : 2026-06-06
# ║  URL        : https://leetcode.com/problems/left-and-right-sum-differences/
# ╚══════════════════════════════════════════════════════════════╝

from typing import List

class Solution:
    """
    Problem: Left and Right Sum Differences
    
    The goal is to calculate the absolute difference between the sum of elements 
    to the left and the sum of elements to the right for every index in the array.
    
    Approach:
    1. Calculate the total sum of the array.
    2. Maintain a running variable `left_sum` starting at 0.
    3. For each element at index `i`:
       - The `right_sum` can be derived as: (Total Sum) - (left_sum) - (current element).
       - The answer for index `i` is abs(left_sum - right_sum).
       - Update `left_sum` by adding the current element for the next iteration.
    
    Complexity Analysis:
    - Time Complexity: O(n), where n is the length of the array. We iterate through 
      the array twice (once for sum(), once for the loop).
    - Space Complexity: O(1) additional space if we don't count the output array,
      or O(n) to store the resulting differences.
    """
    
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        # Calculate the total sum of the array initially
        total_sum = sum(nums)
        
        # Initialize running sum for elements to the left
        left_sum = 0
        
        # Result list to store |leftSum[i] - rightSum[i]|
        answer = []
        
        for x in nums:
            # The sum of elements to the right is the total sum minus 
            # the elements to the left and the element itself.
            right_sum = total_sum - left_sum - x
            
            # Calculate absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum for the next index
            left_sum += x
            
        return answer

# Example Usage:
# sol = Solution()
# print(sol.leftRightDifference([10, 4, 8, 3])) # Output: [15, 1, 11, 22]
# print(sol.leftRightDifference([1]))           # Output: [0]
