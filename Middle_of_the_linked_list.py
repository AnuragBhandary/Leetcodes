# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
        
        #----------------------------------------
        # length = 0
        # curr = head
        # while curr:
        #     curr = curr.next
        #     length += 1

        # i = 0
        # curr = head

        # while i < length//2:
        #     curr = curr.next
        #     i += 1
        
        # return curr
