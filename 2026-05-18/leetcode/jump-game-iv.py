# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Jump Game IV
# ║  Difficulty : Hard
# ║  Date       : 2026-05-18
# ║  URL        : https://leetcode.com/problems/jump-game-iv/
# ╚══════════════════════════════════════════════════════════════╝

"""
Jump Game IV Solution

This problem can be solved using BFS (Breadth-First Search) since we want to find the minimum number of steps to reach the last index.

Approach:
1. Create a graph where each index is a node
2. Edges exist between:
   - Adjacent indices (i-1, i+1)
   - Indices with same value
3. Use BFS to find shortest path from index 0 to last index

Key optimizations:
- Use a hash map to group indices by value for efficient same-value jumps
- Clear the list of same-value indices after visiting any node with that value to avoid redundant exploration

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) for the graph representation and BFS queue
"""

from collections import deque, defaultdict
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        
        # Edge case: already at the last index
        if n <= 1:
            return 0
        
        # Create a map of value -> list of indices with that value
        value_to_indices = defaultdict(list)
        for i, value in enumerate(arr):
            value_to_indices[value].append(i)
        
        # BFS setup
        queue = deque([0])  # Queue stores indices
        visited = set([0])  # Set of visited indices
        steps = 0
        
        while queue:
            # Process all nodes at current level
            for _ in range(len(queue)):
                current_index = queue.popleft()
                
                # If we reached the last index, return steps
                if current_index == n - 1:
                    return steps
                
                # Generate all possible next moves
                next_indices = []
                
                # Move to i+1
                if current_index + 1 < n:
                    next_indices.append(current_index + 1)
                
                # Move to i-1
                if current_index - 1 >= 0:
                    next_indices.append(current_index - 1)
                
                # Jump to same value indices
                current_value = arr[current_index]
                if current_value in value_to_indices:
                    next_indices.extend(value_to_indices[current_value])
                    # Clear the list to avoid revisiting same value indices
                    del value_to_indices[current_value]
                
                # Add unvisited indices to queue
                for next_index in next_indices:
                    if next_index not in visited:
                        visited.add(next_index)
                        queue.append(next_index)
            
            steps += 1
        
        return -1  # Should never reach here for valid input

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [100,-23,-23,404,100,23,23,23,3,404]
    print(f"Example 1: {solution.minJumps(arr1)}")  # Expected: 3
    
    # Example 2
    arr2 = [7]
    print(f"Example 2: {solution.minJumps(arr2)}")  # Expected: 0
    
    # Example 3
    arr3 = [7,6,9,6,9,6,9,7]
    print(f"Example 3: {solution.minJumps(arr3)}")  # Expected: 1
