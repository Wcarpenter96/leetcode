from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        current_a, current_b = headA, headB
        len_a, len_b = 0, 0

        while current_a:
            len_a += 1
            current_a = current_a.next

        while current_b:
            len_b += 1
            current_b = current_b.next

        print(len_a, len_b)


test_list_a = ListNode(4, ListNode(2, ListNode(3, ListNode(1, None))))
test_list_b = ListNode(5, ListNode(1, ListNode(3, ListNode(1, None))))

test = Solution().getIntersectionNode(test_list_a, test_list_b)
while test:
    print(test.val)
    test = test.next

