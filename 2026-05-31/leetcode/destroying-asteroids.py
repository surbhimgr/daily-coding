# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Destroying Asteroids
# ║  Difficulty : Medium
# ║  Date       : 2026-05-31
# ║  URL        : https://leetcode.com/problems/destroying-asteroids/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem Analysis:
    The goal is to determine if a planet of a given initial mass can destroy all 
    asteroids in an array. The planet destroys an asteroid if its current mass 
    is greater than or equal to the asteroid's mass. Upon destruction, the 
    planet absorbs the asteroid's mass.
    
    Greedy Strategy:
    To maximize the planet's ability to destroy larger asteroids, the planet 
    should always target the smallest available asteroid first. This is because 
    destroying smaller asteroids increases the planet's mass, making it 
    easier to meet the mass requirement for larger asteroids later.
    
    Algorithm:
    1. Sort the asteroids array in non-decreasing order.
    2. Iterate through the sorted asteroids.
    3. If the current mass of the planet is >= the mass of the current asteroid,
       add the asteroid's mass to the planet's mass.
    4. If at any point the planet's mass is less than the asteroid's mass, 
       it is impossible to destroy all asteroids; return False.
    5. If all asteroids are processed, return True.

    Time Complexity: O(N log N) where N is the number of asteroids, due to sorting.
    Space Complexity: O(1) or O(N) depending on the sorting implementation's 
                       space requirements (Timsort in Python uses O(N)).
    """

    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        # Sort asteroids to always take the easiest (smallest) target first
        asteroids.sort()
        
        current_mass = mass
        
        for asteroid_mass in asteroids:
            # Check if planet can destroy the current asteroid
            if current_mass >= asteroid_mass:
                # Planet absorbs the mass and continues
                current_mass += asteroid_mass
            else:
                # Planet is destroyed by the asteroid
                return False
                
        # Successfully destroyed all asteroids
        return True

# Example Usage:
# sol = Solution()
# print(sol.asteroidsDestroyed(10, [3, 9, 19, 5, 21])) # Expected: True
# print(sol.asteroidsDestroyed(5, [4, 9, 23, 4]))    # Expected: False
