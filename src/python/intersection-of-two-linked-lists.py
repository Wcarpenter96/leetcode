from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # Get list lengths
        a, b = headA, headB
        len_a, len_b = 0, 0
        while a:
            len_a += 1
            a = a.next
        while b:
            len_b += 1
            b = b.next

        # Line up lists
        a, b = headA, headB
        offset = len_a - len_b
        if offset > 0:
            for _ in range(offset):
                a = a.next
        else:
            for _ in range(offset * -1):
                b = b.next

        # Compare lists for intersection
        while a:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None


test_intersect = ListNode(3, ListNode(1, None))
test_list_a = ListNode(4, ListNode(2, test_intersect))
test_list_b = ListNode(1, test_intersect)

test = Solution().getIntersectionNode(test_list_a, test_list_b)
while test:
    print(test.val)
    test = test.next
