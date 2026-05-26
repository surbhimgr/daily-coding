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
    
    A character is considered 'special' if both its lowercase and uppercase 
    versions appear at least once in the given string 'word'.
    
    Approach:
    1. Use two sets to track the characters encountered: one for lowercase and one for uppercase.
    2. Iterate through the string, adding each character to the corresponding set.
    3. The intersection of these two sets contains all characters that appear in both cases.
    4. The length of this intersection is the total count of special characters.
    
    Time Complexity: O(n), where n is the length of the string. We traverse the string once.
    Space Complexity: O(1), as the sets can contain at most 26 English letters regardless of input size.
    """

    def numberOfSpecialChars(self, word: str) -> int:
        # Sets to store characters seen in lowercase and uppercase
        lowers = set()
        uppers = set()
        
        for char in word:
            if char.islower():
                lowers.add(char)
            elif char.isupper():
                uppers.add(char.lower()) # Normalize to lowercase for easy intersection
                
        # The special characters are those present in both sets
        # Intersection find elements common to both
        special_chars = lowers.intersection(uppers)
        
        return len(special_chars)

# Example usage and test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    assert sol.numberOfSpecialChars("aaAbcBC") == 3 # 'a', 'b', 'c'
    
    # Test Case 2
    assert sol.numberOfSpecialChars("abc") == 0    # No uppercase
    
    # Test Case 3
    assert sol.numberOfSpecialChars("abBCab") == 1 # Only 'b'
    
    print("All test cases passed!")
