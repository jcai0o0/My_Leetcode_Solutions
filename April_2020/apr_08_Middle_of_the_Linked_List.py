# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head
        while fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if not fast or not fast.next:
                return slow
        return head