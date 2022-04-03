# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} head
# @return {ListNode}
def swap_pairs(head)
  prev = nil
  current = head
  count = 0
  until current.nil?
    n = current.next
    if n.nil?
      return head
    end
    unless prev.nil?
      prev.next = n
    end
    current.next = n.next
    n.next = current
    if count == 0
        head = n
        count += 1
    end
    prev = current
    current = current.next
  end
  head
end
