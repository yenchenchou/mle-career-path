"""
1. The real base case for tree is the two null pointers (99% of time holds true). For thre below example, you reach to null and get the 2 then go the right null.

            1
          /   \
        null  null
2. When talking about tree types or ay properties, it means the property applies to all single not just the global tree
3. Common types of tree
    (1) Complete Binary Free
    (2) Full Binary Free
    (3) Binary Search Tree
    (4) Balanced Binary Tree

"""
# 1. pre, in ,post order traversal
# 2. get height of tree
def heightRree(root):
    # base case
    if not root:
        return 0
    left = heightRree(root.left)
    right = heightRree(root.right)
    return max(left, right) + 1
# 3. How to determine whether the tree is balanced binary tree?
# balanced: the height difference of the left subtree and the right subtree is less than or equal to 1
# the below os not the optimal solution
def isBalancedTree(root):
    # how to analyze complexity of two recursion
    if not root: return True

    left = heightRree(root.left) # get height
    right = heightRree(root.right) # get height
    if abs(elft - right) > 1:
        return False
    return isBalancedTree(root.left) and isBalancedTree(root.right)

'''
            isBalancedTree(root) -> time for get height O(n/2) + O(n/2)
           /                    \
isBalancedTree(root.left) isBalancedTree(root.right)
O(n/4) + O(n/4)          +      O(n/4) + O(n/4)

total time complexity: n * logn (layers is balanced)
'''
    
def isBalancedTree(root):
    pass

# 4. Determine whether a binary is symmetric
def symmetricTree(root):
    if not root: return True
    return isSymmetric(root.left, root.right)


def isSymmetric(left, right):
    if not left and not right:
        return True
    elif not left or not right or left.val != right.val:
        return False
    
    return isSymmetric(left.left, right.right) and isSymmetric(left.right, right.left)



