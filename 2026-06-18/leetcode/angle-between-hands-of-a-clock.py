# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Angle Between Hands of a Clock
# ║  Difficulty : Medium
# ║  Date       : 2026-06-18
# ║  URL        : https://leetcode.com/problems/angle-between-hands-of-a-clock/
# ╚══════════════════════════════════════════════════════════════╝

class Solution:
    """
    Problem: Angle Between Hands of a Clock
    
    Logic:
    1. The clock is a circle of 360 degrees.
    2. Minute Hand: 
       - Completes 360 degrees in 60 minutes.
       - Speed = 360 / 60 = 6 degrees per minute.
       - Position = minutes * 6.
    3. Hour Hand:
       - Completes 360 degrees in 12 hours.
       - Speed per hour = 360 / 12 = 30 degrees per hour.
       - Additionally, it moves as minutes pass. It moves 30 degrees in 60 minutes, 
         which is 30 / 60 = 0.5 degrees per minute.
       - Position = (hour % 12) * 30 + (minutes * 0.5).
    4. The angle is the absolute difference between these two positions.
    5. Since we need the smaller angle, if the difference is greater than 180, 
       we subtract it from 360.

    Time Complexity: O(1) - Basic arithmetic operations.
    Space Complexity: O(1) - Constant space used.
    """
    
    def getAngle(self, hour: int, minutes: int) -> float:
        # Calculate the position of the minute hand in degrees from 12 o'clock
        # 360 degrees / 60 minutes = 6 degrees per minute
        minute_angle = minutes * 6
        
        # Calculate the position of the hour hand in degrees from 12 o'clock
        # 360 degrees / 12 hours = 30 degrees per hour
        # Additionally, the hour hand moves as minutes pass: 30 degrees / 60 minutes = 0.5 degrees per minute
        # Use hour % 12 to handle the 12 o'clock position as 0 degrees
        hour_angle = (hour % 12) * 30 + (minutes * 0.5)
        
        # Find the absolute difference between the two angles
        angle = abs(hour_angle - minute_angle)
        
        # The problem asks for the smaller angle between the two hands
        # If the angle is greater than 180, the smaller angle is the exterior one (360 - angle)
        if angle > 180:
            angle = 360 - angle
            
        return float(angle)

# Example usage:
# sol = Solution()
# print(sol.getAngle(12, 30)) # Expected: 165
# print(sol.getAngle(3, 30))  # Expected: 75
# print(sol.getAngle(3, 15))  # Expected: 7.5
