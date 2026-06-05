# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Total Waviness of Numbers in Range II
# ║  Difficulty : Hard
# ║  Date       : 2026-06-05
# ║  URL        : https://leetcode.com/problems/total-waviness-of-numbers-in-range-ii/
# ╚══════════════════════════════════════════════════════════════╝

import functools

class Solution:
    """
    Problem Analysis:
    The goal is to find the total waviness of all numbers in the range [num1, num2].
    Waviness is defined by the number of peaks (digit > both neighbors) and valleys (digit < both neighbors).
    Since we need the sum over a range, we can calculate the total waviness for [1, num2] 
    and subtract the total waviness for [1, num1 - 1].

    Approach: Digit DP
    State variables:
    - index: current digit position being processed.
    - prev_digit: the digit placed at index - 1.
    - pprev_digit: the digit placed at index - 2.
    - is_less: boolean, true if we have already placed a digit smaller than the corresponding digit in the upper bound.
    - is_started: boolean, true if we have started placing non-zero digits (handles leading zeros).
    - trend: represents the relation between prev_digit and pprev_digit.
        0: No trend yet (either fewer than 2 digits placed or digits were equal).
        1: prev_digit > pprev_digit (increasing).
        -1: prev_digit < pprev_digit (decreasing).

    A peak/valley occurs at index-1 if:
    - The trend was increasing (1) and the current digit is smaller than prev_digit (Valley).
    - The trend was decreasing (-1) and the current digit is larger than prev_digit (Peak).
    - Actually, a simpler way: if (pprev < prev > curr) it's a peak, if (pprev > prev < curr) it's a valley.
    """

    def solve(self, n_str: str) -> int:
        # Memoization cache for (index, prev_digit, pprev_digit, is_less, is_started)
        # We store (count_of_numbers, total_waviness)
        @functools.lru_cache(None)
        def dp(idx, prev, pprev, is_less, is_started):
            if idx == len(n_str):
                return 0, 1 if is_started else 0
            
            total_waviness = 0
            total_count = 0
            
            limit = int(n_str[idx]) if not is_less else 9
            
            for d in range(limit + 1):
                new_is_less = is_less or (d < limit)
                new_is_started = is_started or (d > 0)
                
                # If we haven't started, we treat the current digit as a leading zero
                if not new_is_started:
                    w, c = dp(idx + 1, -1, -1, new_is_less, False)
                    total_waviness += w
                    total_count += c
                else:
                    # If we just started (first non-zero digit)
                    if not is_started:
                        w, c = dp(idx + 1, d, -1, new_is_less, True)
                        total_waviness += w
                        total_count += c
                    else:
                        # We have at least one digit already (prev)
                        # Check if prev is a peak or valley
                        # Peak: pprev < prev > d
                        # Valley: pprev > prev < d
                        waviness_increment = 0
                        if pprev != -1:
                            if (pprev < prev > d) or (pprev > prev < d):
                                waviness_increment = 1
                        
                        w, c = dp(idx + 1, d, prev, new_is_less, True)
                        # total_waviness = sum of waviness of suffixes + (this point's waviness * count of suffixes)
                        total_waviness += w + waviness_increment * c
                        total_count += c
                        
            return total_waviness, total_count

        # We need the total waviness of all numbers from 1 to n_str
        res_w, _ = dp(0, -1, -1, False, False)
        return res_w

    def totalWaviness(self, num1: int, num2: int) -> int:
        # Total waviness in [num1, num2] is solve(num2) - solve(num1 - 1)
        # Using strings for the digit DP range
        ans2 = self.solve(str(num2))
        ans1 = self.solve(str(num1 - 1))
        return ans2 - ans1

# Time Complexity: O(L * 10 * 10 * 2 * 2) where L is the number of digits (max 15).
# Space Complexity: O(L * 10 * 10) for the memoization table.
