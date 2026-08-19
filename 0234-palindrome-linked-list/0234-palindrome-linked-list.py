# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head

        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

        prev = None
        curr = slow
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first_half=head
        second_half=prev

        while second_half!=None:
            if first_half.val!=second_half.val:
                return False
            first_half=first_half.next
            second_half=second_half.next

        return True        
        # arr=[]
        # curr = head

        # while curr!=None:
        #     arr.append(curr.val)
        #     curr = curr.next

        # left=0
        # right=len(arr)-1

        # while left<right:
        #     if arr[left]!=arr[right]:
        #         return False
        #     left+=1
        #     right-=1

        # return True            

            