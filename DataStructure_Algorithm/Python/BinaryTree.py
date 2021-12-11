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

4. The number of nodes in binary tree relies on the leaf layer because all sum of upper nodes will be 1 less than the leaf layer

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
    if abs(left - right) > 1:
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

# Time: O(n) -> O(1) split + O(2) split + O(4) split ... + O(n/2) split
# Space: O(n) -> total longest length of the call stack in worst case

# Determine whether is identical, child rotation is allow
def identicalTree(root):
    if not root: return True
    return isIdentical(root.left, root.right)


def isIdentical(left, right):
    if not left and not right:
        return True
    elif not left or not right or left.val != right.val:
        return False
    return (isIdentical(left.left, right.left) and isIdentical(left.right, right.right)) or \
            (isIdentical(left.right, right.left) and isIdentical(left.left, right.right))
            # a quadral tree

"""
      root1             root1
     /    /             \        \
  LL, RL  LR RR        LL RR     LR RL
"""
# Time: the original binary tree has log2N (assume balanced) layer, so quadral tree still has log2N (assume balanced)
# because the original tree isIdentical(left, right) is log2N layer. There are O(4^log2N) = O(N^2) levels in this tree

# Space: O(logn) -> (assume balanced) depends on the number of call stack


# 5. Determine a binary tree is BST
"""
      root(n)
      /       \

brute force: O(n^2)


        10 [-inf, inf]
       /   \
      5    15
[-inf, 10) (10, inf]
    /  \   / \ 
   2    7 12 20
[-inf,5)(5, 10)
"""
def bst(root):
    return helper(root, float("-inf"), float("inf"))
    # if root.left.val < root.val:
    # if root.right.val > root.val:

def helper(root, minVal, maxVal):
    if not root: 
        return True
    if root.val <= minVal or root.val >= maxVal:
        return False
    return helper(root.left, minVal, root.val) and \
        helper(root.right, root.val, maxVal)

# Time: O(n) -> visit every node
# Space: O(n) -> perfect skewed

# 6. print out the value in the range k1 to k2 in a BST in a ascending order
"""
analysis: if we print out in order then we get a print value in ascending order
-> the process in is the middle
k1 = 3
k2 = 9
            10 [3,9]
          /   \
[3,9]    5     15 [3,9]
        /  \   / \ 
       2    7 12 20
"""
def printTree(root, k1, k2):
    if not root:
        return root
    if root.val > k1:  # root.val == k1 will go too small
        printTree(root.left, k1, k2)
    if k1 <= root.val <= k2:
        print(root.val)
    if root.val < k2:
        printTree(root.right, k1, k2)

# Time: O(n) -> possible visit every node
# Space: O(n) -> perfect skewed