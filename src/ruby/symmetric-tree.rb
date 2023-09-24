# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val = 0, left = nil, right = nil)
#         @val = val
#         @left = left
#         @right = right
#     end
# end
# @param {TreeNode} root
# @return {Boolean}
# A tree is symmetric when the left subtree is the same as the 
# inverted right subtree
def is_symmetric(root)
  return true unless root
  is_same_tree(root.left, invert_tree(root.right))
end

# The trees are the same if the root.val of one is 
# the same as the root.val of the other and the left 
# and right subtrees of each are the same
def is_same_tree(root1, root2)
  return true if root1.nil? && root2.nil?
  return false if root1.nil? || root2.nil? || root1.val != root2.val
  is_same_tree(root1.left, root2.left) && is_same_tree(root1.right, root2.right)
end

def invert_tree(root)
  return unless root
  root.left, root.right = invert_tree(root.right),invert_tree(root.left)
  return root
end
