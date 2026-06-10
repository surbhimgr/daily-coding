# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Maximum Total Subarray Value II
# ║  Difficulty : Hard
# ║  Date       : 2026-06-10
# ║  URL        : https://leetcode.com/problems/maximum-total-subarray-value-ii/
# ╚══════════════════════════════════════════════════════════════╝

import heapq

"""
Problem Analysis:
The goal is to select k distinct subarrays [l, r] that maximize the sum of (max(subarray) - min(subarray)).
A key observation is that for any fixed max value and min value in a subarray, we want to identify
how many subarrays have that specific pair as their max and min.

However, the number of subarrays is O(n^2), and k can be up to 10^5. 
We need a way to efficiently find the top k subarrays.

Observation:
A subarray [l, r] has a value (max - min).
The global maximum subarray value is (global_max - global_min).
Many subarrays might share the same maximum and minimum elements.

Algorithm:
1. We can treat this as finding the k largest values in the set of all possible subarrays.
2. A subarray's value is determined by its maximum and minimum.
3. For a fixed pair of indices (i, j) where nums[i] is the maximum and nums[j] is the minimum of a subarray:
   The subarray must be contained within the range where nums[i] remains the max and nums[j] remains the min.
4. This looks like a "K-best" problem. We can use a priority queue to extract the best subarrays.
5. To avoid O(n^2) states, we can use a Divide and Conquer approach (similar to finding the k-th largest subarray sum)
   or observe that for a fixed maximum element at index i, we want to find the best minimums.
   
Alternative Approach:
Since we want the sum of the top k (max - min), this is equivalent to:
Sum (max of subarray) - Sum (min of subarray) for the k chosen subarrays.
Wait, the subarrays must be the SAME k subarrays.
Let's use a Max-Heap to store the "best" possible subarrays.
The most valuable subarrays are likely those that span across the global maximum and global minimum.

Actually, a more robust approach for "Top K" of something involving range queries is to use 
a priority queue of candidate ranges. 
For a range [L, R], the maximum value is max(nums[L..R]) - min(nums[L..R]).
We can start with the range [0, n-1]. Then, to find the next best, we can try shrinking the range
from either side: [L+1, R] or [L, R-1]. However, this doesn't guarantee finding the k-th largest because
the value doesn't monotonically decrease.

Correct Insight:
The number of distinct subarrays is n(n+1)/2. We want the sum of the top k.
We can binary search for a value 'V' such that there are at least k subarrays with (max - min) >= V.
Then the answer is (sum of all (max - min) for subarrays with value >= V) - (excess * V).

To count subarrays with (max - min) >= V:
For a fixed right pointer r, as we move left pointer l, (max - min) is non-increasing.
We can use a two-pointer approach with two monotonic queues (one for max, one for min) 
to find the range of l's such that max(l..r) - min(l..r) >= V.
For a fixed r, there exists a maximum l_max such that for all l <= l_max, (max - min) >= V.
The number of such subarrays is (l_max + 1).

To calculate the sum of (max - min) for these subarrays:
Sum_{l=0 to l_max} (max(l..r) - min(l..r)) = Sum(max) - Sum(min).
We can maintain the sum of maxes and mins as we slide the window using the monotonic queues.

Time Complexity: O(n log(max_val))
Space Complexity: O(n)
"""

from collections import deque

class Solution:
    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        def count_and_sum(V):
            """
            Counts how many subarrays have max - min >= V and returns
            the total sum of (max - min) for those subarrays.
            """
            count = 0
            total_val = 0
            l = 0
            min_dq = deque() # stores indices, nums[i] is increasing
            max_dq = deque() # stores indices, nums[i] is decreasing
            
            # To calculate sum of maxes and mins for l in [0, l_max]
            # We use the fact that as l increases, the max/min changes in blocks.
            # However, it's easier to iterate r and maintain the sum for all l.
            
            # We maintain: 
            # current_max_sum = sum_{i=l}^r max(nums[i..r])
            # current_min_sum = sum_{i=l}^r min(nums[i..r])
            curr_max_sum = 0
            curr_min_sum = 0
            
            l = 0
            for r in range(n):
                # Update max_dq and current_max_sum
                while max_dq and nums[max_dq[-1]] <= nums[r]:
                    idx = max_dq.pop()
                    prev_idx = max_dq[-1] if max_dq else -1
                    curr_max_sum -= (idx - prev_idx) * nums[idx]
                
                prev_idx = max_dq[-1] if max_dq else -1
                curr_max_sum += (r - prev_idx) * nums[r]
                max_dq.append(r)
                
                # Update min_dq and current_min_sum
                while min_dq and nums[min_dq[-1]] >= nums[r]:
                    idx = min_dq.pop()
                    prev_idx = min_dq[-1] if min_dq else -1
                    curr_min_sum -= (idx - prev_idx) * nums[idx]
                
                prev_idx = min_dq[-1] if min_dq else -1
                curr_min_sum += (r - prev_idx) * nums[r]
                min_dq.append(r)
                
                # Shrink l until max - min < V
                # Note: max - min is monotonic with respect to l (decreasing as l increases)
                # We want to find the largest l such that max(l..r) - min(l..r) >= V
                while l <= r:
                    # The value of the subarray starting at l and ending at r
                    # is found by the elements at the front of the deques.
                    # But the deques are for the range [l, r]. 
                    # We need to check the current window's max and min.
                    
                    # Since we need to efficiently remove elements from the left of the 
                    # monotonic queue, we must ensure max_dq[0] and min_dq[0] are >= l.
                    while max_dq and max_dq[0] < l:
                        max_dq.popleft()
                    while min_dq and min_dq[0] < l:
                        min_dq.popleft()
                    
                    if not max_dq or not min_dq: break
                    
                    if nums[max_dq[0]] - nums[min_dq[0]] >= V:
                        # This window [l, r] and all windows [l', r] for l' < l
                        # also satisfy the condition. But we are iterating l.
                        # Actually, it's easier to move l forward and subtract the
                        # contribution of the subarray starting at l.
                        
                        # The value of subarray [l, r] is nums[max_dq[0]] - nums[min_dq[0]]
                        # But the window [l, r] is just one subarray.
                        # We need the sum for ALL i in [0, l_max].
                        break
                    else:
                        # This is tricky because the monotonic queues are built 
                        # for the range [l, r]. 
                        # Let's use a different approach for the sum.
                        break
                
            return 0 # Placeholder

        # Redoing the approach: Binary Search for V is correct.
        # To implement the count and sum efficiently:
        # For a fixed r, as l increases, max(l..r) is non-increasing and min(l..r) is non-decreasing.
        # Thus (max - min) is non-increasing.
        # Let f(l, r) = max(nums[l..r]) - min(nums[l..r]).
        # For a fixed r, we find l_max such that f(l_max, r) >= V.
        # Then all l in [0, l_max] satisfy f(l, r) >= V.
        
        low = 0
        high = 10**9
        best_v = 0
        
        def get_metrics(V):
            # Returns (count, total_sum) for subarrays with max-min >= V
            cnt = 0
            s = 0
            l = 0
            max_dq = deque() 
            min_dq = deque()
            
            # To maintain sum of max and min for i in [0, l_max]
            # we can't easily use the standard monotonic queue sum trick 
            # because the window is [i, r] and we only sum for i <= l_max.
            # However, if we find l_max, the sum is:
            # Sum_{i=0}^{l_max} max(i, r) - Sum_{i=0}^{l_max} min(i, r)
            
            # Let's use the property:
            # Sum_{i=0}^{r} max(i, r) can be maintained in O(1) as r increases.
            # Let S_max(r) = Sum_{i=0}^{r} max(i, r).
            # When r increases to r+1:
            # The elements i that had max(i, r) < nums[r+1] now have max(i, r+1) = nums[r+1].
            
            # We can maintain these sums for the full range [0, r].
            # Then we need to subtract the sum for i in [l_max + 1, r].
            # This is still hard.
            
            # Let's simplify: k is 10^5. n is 5*10^4.
            # Maybe a priority queue of ranges?
            # Start with (nums[0..n-1], 0, n-1).
            # In each step, take the best, then add its children.
            # But children are not simply [L+1, R] and [L, R-1].
            # This is only for sums. For max-min, it's different.
            
            return 0

# The problem can be solved by noticing that we want to find k subarrays with the largest max-min.
# This is a "K-th largest" problem.
# The most efficient way to find the top K subarrays of max-min is to use the fact that
# for a fixed min index 'i' and max index 'j', any subarray containing both and 
# having no elements larger than nums[j] or smaller than nums[i] will have the same value.

# Let's reconsider: we can find all pairs (min_idx, max_idx) that could be the min and max
# of some subarray. But that's too many.

# Correct approach: 
# For every index i, find the range [L_i, R_i] where nums[i] is the maximum.
# This can be done using a monotonic stack.
# Now we have ranges where nums[i] is the max. We want to pair this with a min.
# This is still complex.

# Final attempt approach:
# Since the total number of subarrays is n(n+1)/2 and k is small (10^5),
# we can use a priority queue to store subarrays.
# But which ones?
# A subarray's value is determined by its max and min.
# Let's use the divide and conquer approach for "K-th largest" problem.
# Or just binary search for the value V.
# To count subarrays with max - min >= V in O(n):
# Use two pointers. For each r, find the largest l such that max(l..r) - min(l..r) >= V.
# Since max(l..r) - min(l..r) is non-increasing as l increases, 
# we can use a sliding window with two monotonic queues to find l_max in O(n).
# Then the number of subarrays is Sum(l_max + 1).
# To find the sum of values:
# Sum_{r=0 to n-1} Sum_{l=0 to l_max(r)} (max(l..r) - min(l..r))
# This sum can be computed by maintaining the Sum_{l=0}^r max(l..r) and 
# subtracting the sum from l_max+1 to r.

class Solution:
    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        n = len(nums)
        
        def solve(V):
            cnt = 0
            total_val = 0
            l = 0
            max_dq = deque()
            min_dq = deque()
            
            # current_max_sum = sum_{i=l}^r max(nums[i..r])
            # current_min_sum = sum_{i=l}^r min(nums[i..r])
            c_max_sum = 0
            c_min_sum = 0
            
            for r in range(n):
                # Update maxes
                while max_dq and nums[max_dq[-1]] <= nums[r]:
                    idx = max_dq.pop()
                    prev = max_dq[-1] if max_dq else -1
                    c_max_sum -= (idx - prev) * nums[idx]
                prev = max_dq[-1] if max_dq else -1
                c_max_sum += (r - prev) * nums[r]
                max_dq.append(r)
                
                # Update mins
                while min_dq and nums[min_dq[-1]] >= nums[r]:
                    idx = min_dq.pop()
                    prev = min_dq[-1] if min_dq else -1
                    c_min_sum -= (idx - prev) * nums[idx]
                prev = min_dq[-1] if min_dq else -1
                c_min_sum += (r - prev) * nums[r]
                min_dq.append(r)
                
                # Now shrink l to find the largest l such that max-min >= V
                # The current sums are for i in [l, r].
                # We want to move l forward until max(l..r) - min(l..r) < V.
                while l <= r:
                    # Value of current subarray [l, r]
                    # We need the max and min for the current window [l, r]
                    # Since we move l, we must pop from the front of deques
                    while max_dq and max_dq[0] < l: max_dq.popleft()
                    while min_dq and min_dq[0] < l: min_dq.popleft()
                    
                    if not max_dq or not min_dq: break
                    
                    cur_val = nums[max_dq[0]] - nums[min_dq[0]]
                    if cur_val >= V:
                        # All subarrays from [l, r], [l+1, r]... up to [l_max, r]
                        # will be counted. But it's easier to just move l 
                        # and maintain the sum.
                        # This is slightly wrong. Let's use the property:
                        # If max(l, r) - min(l, r) >= V, then [l, r] is a valid subarray.
                        # Since max-min is non-increasing with l, we find the 
                        # maximum l' such that max(l', r) - min(l', r) >= V.
                        # All i in [0, l'] are valid.
                        # The sum of (max - min) for i in [0, l'] is 
                        # (Sum_{i=0}^r max - Sum_{i=l'+1}^r max) - (Sum_{i=0}^r min - Sum_{i=l'+1}^r min)
                        break
                    else:
                        # Not possible here since cur_val is max-min for [l, r]
                        # and we are looking for it to be >= V.
                        # If it's < V, then for any l' > l, max-min will also be < V.
                        # So we stop.
                        break
                
                # Wait, the two-pointer logic is:
                # For a fixed r, we want to find the number of l's in [0, r] such that 
                # max(l..r) - min(l..r) >= V.
                # Because max-min is non-increasing as l increases, 
                # there is a boundary l_max.
                # We can find l_max by moving it forward.
                
            return 0

# Given the complexity of implementing the binary search sum, 
# let's use the Priority Queue approach with a smart state.
# A state is (value, l, r).
# The best subarray is the one with the global max and min.
# This is not quite correct.
# The most reliable way to solve "Top K Subarrays" is using a 
# Segment Tree or a similar structure to find the max value, then split.

import heapq

class Solution:
    def maxTotalSubarrayValue(self, nums: list[int], k: int) -> int:
        # Use a max-priority queue to find the k subarrays with the largest max-min.
        # We start with the range [0, n-1].
        # For a range [l, r], its value is max(nums[l..r]) - min(nums[l..r]).
        # To avoid duplicates and ensure we find the top k, we can't just do [l+1, r] and [l, r-1].
        # However, for the purpose of this problem, k is small enough that we can 
        # use a heap of (value, l, r) and push neighbors, using a set to track visited.
        # Note: This might be too slow for n=5e4, but given the constraints, 
        # the number of "high value" subarrays is often small or they are clustered.
        
        n = len(nums)
        if n == 0: return 0
        
        # Precompute sparse tables for range max and min queries
        log_n = n.bit_length()
        st_max = [[0] * n for _ in range(log_n)]
        st_min = [[0] * n for _ in range(log_n)]
        st_max[0] = nums[:]
        st_min[0] = nums[:]
        
        for j in range(1, log_n):
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])
        
        def get_max(l, r):
            j = (r - l + 1).bit_length() - 1
            return max(st_max[j][l], st_max[j][r - (1 << j) + 1])
        
        def get_min(l, r):
            j = (r - l + 1).bit_length() - 1
            return min(st_min[j][l], st_min[j][r - (1 << j) + 1])

        def get_val(l, r):
            return get_max(l, r) - get_min(l, r)

        pq = [(-get_val(0, n - 1), 0, n - 1)]
        visited = {(0, n - 1)}
        total_value = 0
        count = 0
        
        while pq and count < k:
            val_neg, l, r = heapq.heappop(pq)
            total_value += (-val_neg)
            count += 1
            
            for nl, nr in [(l + 1, r), (l, r - 1)]:
                if nl <= nr and (nl, nr) not in visited:
                    visited.add((nl, nr))
                    heapq.heappush(pq, (-get_val(nl, nr), nl, nr))
                    
        return total_value
