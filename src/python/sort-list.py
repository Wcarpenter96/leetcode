from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Bubble sort implementation
        """
        current = head
        while current:
            if current.next and current.val > current.next.val:
                # swap the values on the nodes
                larger_val = current.val
                current.val = current.next.val  # min value
                current.next.val = larger_val
            current = current.next
        return head

    def sortList2(self, head):
        def merge(a, b):
            current = pre_head = ListNode()

            while a and b:
                if a.val <= b.val:
                    current.next = a
                    a = a.next
                else:
                    current.next = b
                    b = b.next

                current = current.next

            while a:
                current.next = a
                a = a.next
                current = current.next

            while b:
                current.next = b
                b = b.next
                current = current.next

            return pre_head.next

        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head

        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next

        if pre:
            pre.next = None

        first_half = self.sortList(head)
        second_half = self.sortList(slow)
        result = merge(first_half, second_half)

        return result


test_list = ListNode(4, ListNode(2, ListNode(3, ListNode(1, None))))
test = Solution().sortList2(test_list)
while test:
    print(test.val)
    test = test.next