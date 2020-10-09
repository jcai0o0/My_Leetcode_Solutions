class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        if head.next == head:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        if fast and fast.next:
            temp = head
            while temp != slow:
                temp, slow = temp.next, slow.next
            return temp
        return None