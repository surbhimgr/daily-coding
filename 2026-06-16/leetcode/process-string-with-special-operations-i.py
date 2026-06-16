# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Process String with Special Operations I
# ║  Difficulty : Medium
# ║  Date       : 2026-06-16
# ║  URL        : https://leetcode.com/problems/process-string-with-special-operations-i/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Process String with Special Operations I
    
    The problem asks us to simulate a process of building a string based on a set of 
    special character rules:
    - Lowercase letter: Append to the result.
    - '*': Remove the last character from the result (backspace).
    - '#': Duplicate the current result (result = result + result).
    - '%': Reverse the current result.

    Given the constraints (s.length <= 20), a direct simulation is highly efficient 
    as the string length grows exponentially with '#', but with a maximum of 20 
    operations, the growth is manageable within memory limits.
    """

    def processString(self, s: str) -> str:
        # Initialize an empty list to act as a dynamic string/buffer
        # Using a list is generally more efficient for appending and popping in Python
        result = []
        
        for char in s:
            if char == '*':
                # Remove the last character if the result is not empty
                if result:
                    result.pop()
            elif char == '#':
                # Duplicate the current result. 
                # result[:] creates a copy of the current list to append
                result += result[:]
            elif char == '%':
                # Reverse the current result in-place
                result.reverse()
            else:
                # If it's a lowercase English letter, append it
                result.append(char)
        
        # Join the list into a final string
        return "".join(result)

# Time and Space Complexity Analysis:
# -----------------------------------
# Time Complexity: O(2^N) in the worst case.
#   - The '#' operation doubles the length of the string. If we have 20 '#' characters,
#     the length could potentially reach 2^20. 
#   - Reversing ('%') and duplicating ('#') both take linear time relative to the 
#     current length of the result string.
#   - Given N <= 20, 2^20 is roughly 1 million, which fits within the time limit.
#
# Space Complexity: O(2^N).
#   - The resulting string can grow exponentially due to the '#' operation.
#   - The space required to store the result is proportional to the final string length.
