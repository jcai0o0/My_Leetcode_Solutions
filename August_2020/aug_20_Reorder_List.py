# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        # find the middle node of linked list
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        while prev:
            nxt_1 = head.next
            nxt_2 = prev.next
            print(head.val, prev.val)
            head.next = prev
            prev.next = nxt_1
            head = nxt_1
            prev = nxt_2