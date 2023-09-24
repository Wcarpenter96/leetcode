# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val = 0, _next = nil)
#         @val = val
#         @next = _next
#     end
# end
# @param {ListNode} list1
# @param {ListNode} list2
# @return {ListNode}
def merge_two_lists(l1, l2)
    merged = [] # head = nil
    h1 = l1
    h2 = l2
    
    while !h1.nil? && !h2.nil? do  
        if h1.val < h2.val
            merged << h1.val
            h1 = h1.next
        else
            merged << h2.val
            h2 = h2.next
        end
    end
    
    if h1.nil?
        while !h2.nil? do 
            merged << h2.val
            h2 = h2.next
        end
    elsif h2.nil? 
        while !h1.nil? do 
            merged << h1.val
            h1 = h1.next
        end
    end 
    
    merged
end