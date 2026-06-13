# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Weighted Word Mapping
# ║  Difficulty : Easy
# ║  Date       : 2026-06-13
# ║  URL        : https://leetcode.com/problems/weighted-word-mapping/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Weighted Word Mapping
    
    The goal is to calculate the total weight of each word based on a provided weight array
    for the 26 lowercase English letters. Then, take the weight modulo 26 and map it to a 
    character using a reverse alphabetical order (0 -> 'z', 1 -> 'y', ..., 25 -> 'a').
    Finally, concatenate these characters into a single result string.

    Algorithm:
    1. Initialize an empty list to store the resulting characters.
    2. For each word in the input array:
       a. Calculate the sum of weights for each character in the word.
       b. Compute the weight modulo 26.
       c. Map the result 'r' to a character. Since 0 maps to 'z' and 25 maps to 'a', 
          the mapping is: character = chr(ord('z') - r).
       d. Append this character to the list.
    3. Join the list into a string and return.

    Time Complexity: O(N * L), where N is the number of words and L is the average length of a word.
    Space Complexity: O(N), to store the resulting characters before joining.
    """

    def weightedWordMapping(self, words: list[str], weights: list[int]) -> str:
        result = []
        
        for word in words:
            word_weight = 0
            for char in word:
                # Convert character to 0-25 index (a=0, b=1, ...)
                idx = ord(char) - ord('a')
                word_weight += weights[idx]
            
            # Calculate weight modulo 26
            rem = word_weight % 26
            
            # Map the remainder to reverse alphabet order
            # 0 -> 'z' (ord('z') - 0)
            # 1 -> 'y' (ord('z') - 1)
            # 25 -> 'a' (ord('z') - 25)
            mapped_char = chr(ord('z') - rem)
            result.append(mapped_char)
            
        return "".join(result)

# Example usage and testing
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    print(sol.weightedWordMapping(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2])) 
    # Expected: "rij"
    
    # Example 2
    print(sol.weightedWordMapping(["a","b","c"], [1]*26)) 
    # Expected: "yyy"
    
    # Example 3
    print(sol.weightedWordMapping(["abcd"], [7,5,3,4,3,5,4,9,4,2,2,7,10,2,5,10,6,1,2,2,4,1,3,4,4,5])) 
    # Expected: "g"
