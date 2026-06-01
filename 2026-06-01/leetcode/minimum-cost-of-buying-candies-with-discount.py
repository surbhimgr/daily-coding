# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Minimum Cost of Buying Candies With Discount
# ║  Difficulty : Easy
# ║  Date       : 2026-06-01
# ║  URL        : https://leetcode.com/problems/minimum-cost-of-buying-candies-with-discount/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem Explanation:
    The goal is to minimize the cost of buying all candies. 
    We can get one candy for free for every two candies we buy, provided the free 
    candy's cost is less than or equal to the minimum cost of the two bought candies.
    
    Greedy Strategy:
    To maximize the value of the free candies, we should aim to get the most expensive 
    possible candies for free. To do this, we should buy the two most expensive 
    candies available. These two will then allow us to take the third most 
    expensive candy for free (since the third most expensive is guaranteed to be 
    <= the minimum of the top two).
    
    Algorithm:
    1. Sort the costs in descending order.
    2. Iterate through the sorted array in chunks of 3.
    3. For every chunk of 3, we pay for the first two (most expensive) and skip the third.
    4. If fewer than 3 candies remain in a chunk, we pay for all of them.
    
    Time Complexity: O(N log N) due to sorting, where N is the length of the cost array.
    Space Complexity: O(1) or O(N) depending on the sorting implementation in Python (Timsort).
    """

    def minCost(self, cost: list[int]) -> int:
        # Sort the candies in descending order to pick the most expensive ones first
        cost.sort(reverse=True)
        
        total_cost = 0
        i = 0
        n = len(cost)
        
        # Process candies in groups of 3
        while i < n:
            # We always pay for the first two candies in the current group of three
            # if they exist.
            if i < n:
                total_cost += cost[i]
                i += 1
            if i < n:
                total_cost += cost[i]
                i += 1
                
            # The third candy is free (if it exists), so we skip it.
            # The condition for the free candy is that its cost <= min(bought_1, bought_2).
            # Since the array is sorted descending, cost[i] is always <= cost[i-1] and cost[i-2].
            i += 1
            
        return total_cost

# Example usage and testing:
# sol = Solution()
# print(sol.minCost([1,2,3]))        # Output: 5
# print(sol.minCost([6,5,7,9,2,2]))  # Output: 23
# print(sol.minCost([5,5]))          # Output: 10
