# ╔══════════════════════════════════════════════════════════════╗
# ║  Source     : LeetCode
# ║  Title      : Maximum Twin Sum of a Linked List
# ║  Difficulty : Medium
# ║  Date       : 2026-06-14
# ║  URL        : https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# ╚══════════════════════════════════════════════════════════════╝

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    """
    Problem Analysis:
    The problem asks for the maximum "twin sum" in a linked list of even length n.
    A node at index i is a twin of the node at index n-1-i.
    Effectively, we need to sum the first half of the list with the second half 
    of the list reversed.
    
    Approach:
    1. Find the middle of the linked list using the slow and fast pointer technique.
    2. Reverse the second half of the linked list.
    3. Traverse both the first half (from head) and the reversed second half 
       simultaneously, calculating the sum of their values.
    4. Keep track of the maximum sum encountered.
    
    Time Complexity: O(n)
    - Finding the middle takes O(n/2).
    - Reversing the second half takes O(n/2).
    - Iterating to find the max twin sum takes O(n/2).
    - Total: O(n), where n is the number of nodes in the list.
    
    Space Complexity: O(1)
    - We perform the reversal in-place, using only a few pointer variables.
    """
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Step 1: Find the middle of the linked list
        # 'slow' will eventually point to the start of the second half
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # Step 2: Reverse the second half of the list
        # slow is now the head of the second half
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            
        # After reversal, 'prev' is the head of the reversed second half
        # Step 3: Calculate twin sums
        max_twin_sum = 0
        first_half = head
        second_half = prev # The head of the reversed second half
        
        # We only need to iterate for n/2 elements
        while second_half:
            current_sum = first_half.val + second_half.val
            max_twin_sum = max(max_twin_sum, current_sum)
            
            first_half = first_half.next
            second_half = second_half.next
            
        return max_twin_sum
