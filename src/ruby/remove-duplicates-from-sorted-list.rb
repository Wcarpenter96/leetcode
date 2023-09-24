require 'pry'

# Definition for singly-linked list.
class ListNode
    attr_accessor :val, :next
    def initialize(val = 0, _next = nil)
        @val = val
        @next = _next
    end
end

class LinkedList
  def initialize
    @head = nil
  end

  def append(value)
    if @head
      find_tail.next = ListNode.new(value)
    else
      @head = Node.new(value)
    end
  end

  def print
    node = @head
    puts node
    while (node = node.next)
      puts node
    end
  end
end

node3 = ListNode.new(2,nil)
node2 = ListNode.new(1,node3)
node1 = ListNode.new(1,node2)
head = node1

# @param {ListNode} head
# @return {ListNode}

def delete_duplicates(head)
    dedup = []
    if head.nil?
      return dedup
    end
    while !head.next.nil?
      if head.val != head.next.val
        dedup.push(head.val)
      end
      head = head.next
    end
    dedup.push(head.val)
    dedup
end

def delete_duplicates(head)
    if head.nil?
      return head
    end
    dedup = head
    while !head.next.nil?
      binding.pry
      if head.val != head.next.val
        dedup.val = head.val
        dedup = dedup.next
      end
      head = head.next
    end
    dedup.val = head.val
    dedup.next = nil
    dedup
end

delete_duplicates(head)
