# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Count the Number of Special Characters I
# ║  Difficulty : Easy
# ║  Date       : 2026-05-26
# ║  URL        : https://leetcode.com/problems/count-the-number-of-special-characters-i/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Count the Number of Special Characters I
    A character is 'special' if both its lowercase and uppercase versions 
    exist within the given string.
    
    Approach:
    1. Use two sets to keep track of all lowercase letters and uppercase letters 
       encountered in the string.
    2. The intersection of these two sets represents the letters that appear 
       in both cases.
    3. The size of this intersection is the number of special characters.
    
    Time Complexity: O(N), where N is the length of the word. We traverse the string once.
    Space Complexity: O(1), because the sets will contain at most 26 characters 
    regardless of the input size.
    """

    def specialCharacters(self, word: str) -> int:
        # Set to store lowercase letters found in the word
        lower_set = set()
        # Set to store uppercase letters found in the word
        upper_set = set()
        
        for char in word:
            if char.islower():
                lower_set.add(char)
            elif char.isupper():
                upper_set.add(char)
        
        # To find the intersection, we need the uppercase letters converted to lowercase
        # or vice-versa. Here we convert all uppercase letters in upper_set to lowercase.
        normalized_upper = {char.lower() for char in upper_set}
        
        # The number of special characters is the size of the intersection 
        # between lowercase characters and normalized uppercase characters.
        special_chars = lower_set.intersection(normalized_upper)
        
        return len(special_chars)

# Example usage:
# sol = Solution()
# print(sol.specialCharacters("aaAbcBC")) # Output: 3
# print(sol.specialCharacters("abc"))     # Output: 0
# print(sol.specialCharacters("abBCab"))  # Output: 1
