# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        h = head
        length = 0
        intv = 1
        while h:
            h = h.next
            length += 1
        fake_head = ListNode(None)
        fake_head.next = head
        while intv < length:
            prev, h = fake_head, fake_head.next
            while h:
                # get the two merge head h1 and h2
                h1, i = h, intv
                while i and h:
                    h = h.next
                    i -= 1
                if i:
                    break
                h2, i = h, intv
                while i and h:
                    h = h.next
                    i -= 1
                c1, c2 = intv, intv-i
                while c1 and c2:
                    if h1.val < h2.val:
                        prev.next = h1
                        h1 = h1.next
                        c1 -= 1
                    else:
                        prev.next = h2
                        h2 = h2.next
                        c2 -= 1
                if c1:
                    prev.next = h1
                if c2:
                    prev.next = h2
                while c1 > 0 or c2 > 0:
                    prev = prev.next
                    c1 -= 1
                    c2 -= 1
                prev.next = h
            intv *= 2
        return fake_head.next