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
# @return {Integer[]}
def inorder_traversal(root)
    current = root
    stack = []
    inorder = []
    
    while true do
        if !current.nil?
            stack.push(current)
            current = current.left
        else
            if stack.empty?
                break
            else
                current = stack.pop
                inorder.push(current.val)
                current = current.right
            end
        end
    end
    inorder
end

def inorder_traversal(root)
    @inorder = []
    
    def traverse(current)
        return if current.nil?
        traverse(current.left)
        @inorder.push(current.val)
        traverse(current.right)
    end
    
    traverse(root)
    @inorder
end