# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        #Edge case if empty or len 1.
        if head is None or head.next is None:
            return True
    
        #Empty arr
        nums = []
        
        #Add to arr at the expense of making it O(n) in space
        while head:
            nums.append(head.val)
            head = head.next
            
        #Initialise 2 pointers. L->R and L<-R
        #L is zero. R is length of arr.
        l, r = 0, len(nums) - 1
        #While the points havenn't crossed yet
        while l <= r:
            #If ever the pointers aren't equal, then can't be palindrome
            if nums[l] != nums[r]:
                return False
            l = l + 1
            r = r - 1
        return True
