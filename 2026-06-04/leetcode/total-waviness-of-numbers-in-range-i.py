# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Total Waviness of Numbers in Range I
# ║  Difficulty : Medium
# ║  Date       : 2026-06-04
# ║  URL        : https://leetcode.com/problems/total-waviness-of-numbers-in-range-i/
# ╚══════════════════════════════════════════════════════════════╝

"""
Problem Analysis:
The "waviness" of a number is the count of its peaks and valleys.
A peak is a digit strictly greater than both neighbors; a valley is strictly less.
First and last digits are never peaks or valleys. 
Numbers with < 3 digits have 0 waviness.

Given the constraints (num1, num2 <= 10^5), a simple iteration over the range 
is efficient enough. For each number, we convert it to a string of digits 
and check the conditions for each digit from index 1 to n-2.

Time Complexity: O(N * L), where N is the number of elements in the range 
               and L is the average number of digits (max 6).
Space Complexity: O(L) to store the digits of the current number.
"""

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        total_waviness = 0
        
        # Iterate through every number in the inclusive range [num1, num2]
        for num in range(num1, num2 + 1):
            # Convert number to a string to easily access digits
            s = str(num)
            n = len(s)
            
            # A number with fewer than 3 digits has a waviness of 0
            if n < 3:
                continue
            
            # Check digits from the second to the second-to-last
            for i in range(1, n - 1):
                prev_digit = s[i-1]
                curr_digit = s[i]
                next_digit = s[i+1]
                
                # A peak is strictly greater than both neighbors
                if curr_digit > prev_digit and curr_digit > next_digit:
                    total_waviness += 1
                # A valley is strictly less than both neighbors
                elif curr_digit < prev_digit and curr_digit < next_digit:
                    total_waviness += 1
                    
        return total_waviness

# Example Usage and Testing
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(f"Example 1: {sol.totalWaviness(120, 130)}") # Expected: 3
    
    # Example 2
    print(f"Example 2: {sol.totalWaviness(198, 202)}") # Expected: 3
    
    # Example 3
    print(f"Example 3: {sol.totalWaviness(4848, 4848)}") # Expected: 2
