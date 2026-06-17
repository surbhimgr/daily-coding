# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Process String with Special Operations II
# ║  Difficulty : Hard
# ║  Date       : 2026-06-17
# ║  URL        : https://leetcode.com/problems/process-string-with-special-operations-ii/
# ╚══════════════════════════════════════════════════════════════╝

import sys

class Solution:
    """
    Problem: Process String with Special Operations II
    
    The problem asks for the k-th character of a string formed by specific operations:
    - Lowercase letter: Append to result.
    - '*': Remove last character.
    - '#': Duplicate current string.
    - '%': Reverse current string.
    
    Constraints: k and total length can be up to 10^15. A direct simulation is impossible.
    
    Approach:
    1. We first simulate the process to track the length of the string and the state 
       at each operation. We store these "snapshots" in a list.
    2. Once we have the total length, we check if k is within bounds.
    3. We work backwards from the final state to find which character at the 
       original string indices would end up at position k.
    
    Reverse Logic:
    - If operation was 'letter': if k == length - 1, the character is that letter.
    - If operation was '*': the string was longer before. k remains k.
    - If operation was '#': the string was duplicated. If k >= half_length, 
      then k = k - half_length.
    - If operation was '%': the string was reversed. k = (length - 1) - k.
    
    Complexity:
    - Time: O(N), where N is the length of string s. We iterate through s twice.
    - Space: O(N) to store the history of lengths and operations.
    """

    def kthCharacter(self, s: str, k: int) -> str:
        # We use 0-indexed k as per problem description if k=0 is the first char, 
        # however, the examples show k is 0-indexed ("a#b%*", k=1 is 'a', "ba" -> index 1 is 'a').
        
        history = []
        current_length = 0
        
        # Phase 1: Forward pass to calculate lengths and store history
        for char in s:
            if char.islower():
                current_length += 1
                history.append(('char', current_length, char))
            elif char == '*':
                if current_length > 0:
                    current_length -= 1
                history.append(('*', current_length, ''))
            elif char == '#':
                current_length *= 2
                history.append(('#', current_length, ''))
            elif char == '%':
                history.append(('%', current_length, ''))
            
            # Safety break: though constraints say final length <= 10^15, 
            # we only care about lengths up to k + 1.
            # However, since k can be 10^15, we just track exactly.
        
        # If k is out of bounds of the final string
        if k < 0 or k >= current_length:
            return "."
        
        # Phase 2: Backward pass to trace index k
        curr_k = k
        for i in range(len(history) - 1, -1, -1):
            op, length, val = history[i]
            
            if op == 'char':
                # If the current character was the one appended and it's at the target index
                if curr_k == length - 1:
                    return val
                # Otherwise, this char was appended after the k-th char, so it doesn't affect curr_k
            
            elif op == '*':
                # The '*' operation removed a character. In reverse, that character 
                # is simply ignored because it's not part of the final string 
                # that we are searching through.
                pass
            
            elif op == '#':
                # String was duplicated: S = S + S
                # If curr_k is in the second half, map it back to the first half
                half_len = length // 2
                if curr_k >= half_len:
                    curr_k -= half_len
            
            elif op == '%':
                # String was reversed.
                # New index = (Length - 1) - Old index
                # Note: the length here is the length of the string at that operation step
                curr_k = (length - 1) - curr_k
                
        return "."
