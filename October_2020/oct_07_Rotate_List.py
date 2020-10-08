class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k==0:
            return head
        # get the length of the linked list
        curr, length = head, 0
        while curr:
            curr = curr.next
            length += 1
        k %= length
        if k == 0:
            return head
        skip = length - k - 1
        curr = head
        while skip:
            curr = curr.next
            skip -= 1
        new_head = curr.next
        curr.next = None
        curr = new_head
        while curr.next:
            curr = curr.next
        curr.next = head
        return new_head

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next or k == 0:
            return head
        # get the length of the linked list
        curr, length = head, 0
        while curr:
            if not curr.next:
                tail = curr
            curr = curr.next
            length += 1

        k = k % length
        if k == 0:
            return head
        tail.next = head
        curr = head
        for _ in range(length - k - 1):
            curr = curr.next
        new_head = curr.next
        curr.next = None

        return new_head