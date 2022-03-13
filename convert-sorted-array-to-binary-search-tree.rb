# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {Integer[]} nums
# @return {TreeNode}
def sorted_array_to_bst(nums)
  add_node(nums, 0, nums.length-1)
end

def add_node(nums, s, e)
  if (s > e)
    return nil
  end
  
  m = (s + e)/2
  node = TreeNode.new(nums[m])
  node.left = add_node(nums, s, m-1)
  node.right = add_node(nums, m+1, e)
  node
end