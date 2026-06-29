# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Number of Strings That Appear as Substrings in Word
# ║  Difficulty : Easy
# ║  Date       : 2026-06-29
# ║  URL        : https://leetcode.com/problems/number-of-strings-that-appear-as-substrings-in-word/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Number of Strings That Appear as Substrings in Word
    
    The objective is to count how many strings from the 'patterns' list exist 
    as a contiguous substring within the given 'word'. 
    
    Approach:
    Since the constraints are very small (patterns length <= 100, word length <= 100),
    we can iterate through each pattern and use the built-in Python 'in' operator 
    to check if the pattern is a substring of the word. 
    
    Time Complexity: O(N * P * W)
    - N: Number of strings in patterns.
    - P: Average length of a pattern.
    - W: Length of the word.
    - The 'in' operator for string membership in Python typically uses a mix 
      of Boyer-Moore and Horspool algorithms, running in O(P + W) on average.
    
    Space Complexity: O(1)
    - No additional significant space is used regardless of input size.
    """

    def numOfStrings(self, patterns: list[str], word: str) -> int:
        # Initialize a counter to keep track of valid substrings
        count = 0
        
        # Iterate through every pattern in the provided patterns list
        for pattern in patterns:
            # Check if the current pattern exists anywhere within the word
            # The 'in' keyword in Python checks for substring existence
            if pattern in word:
                count += 1
        
        return count

# Example Usage:
# sol = Solution()
# print(sol.numOfStrings(["a","abc","bc","d"], "abc"))  # Output: 3
# print(sol.numOfStrings(["a","b","c"], "aaaaabbbbb")) # Output: 2
# print(sol.numOfStrings(["a","a","a"], "ab"))         # Output: 3
