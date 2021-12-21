# Depth-first search in Python
# This exploring algorithm can be useful if we want to find if two points in a graph are connected. 
# DFS is finding strongly connected components.

# Solution1: Iterative method
## A class to represent a graph object
# Solution2: Recursive method

### Discussion
# 1. BFS1 vs BFS2
# 2. BFS1 vs DFS -> When to use one or the other
# Can we use BFS for permutation problem, why?
#

# Why use DFS over BFS, easier to prevent heap overflow (64 bit computer) for most cases
# DFS can be implemented iteratively or recurively. recursively is just easier.
## All permutation's time scomplexity must be exponential O(2^n). If you got this O(n^2) then you are wrong
"""
1. Most permutation or combination problems can be solved by DFS
2. Think of the coding problem as math problem + draw recursion tree (IMPORTANT!)
3. Basic method of DFS
    -> What does it store each level? The meaning of each level. Usually you know the number of call stacks beforehand 
    -> How many different state should we try to put on this level? (How many states or cases we to try)


"""
# 1. print all subset of a set {a,b,c}


# 2. {}{}{} find all valid permutations using the parenthesis provided (22. Generate Parentheses)
class Solution:
    """
    22. Generate Parentheses

    n: store the number of "pairs of {}" need to add
    left: stores the number of left parenthesis added so far
    right: stores the number of right parenthesis added so far
    ans: solution so far
    """
    def generateParenthesis(self, n: int):
        pass

    def valid_parenthesis(self, nums, left, right, ans):
        """
        1. Figure out the definition "valid"
        2. suppose we have a parenthesis {}{}{} -> three pairs
            -> 0 1 2 3 4 5: either you put { or } but this time has limitation
        3. back to basic (think mathematically)
            1. What does the function store on each level and knowing the approximate layer
                -> 2*n (6) layers, each level represents a position where we could place a "{" or "}"
                -> limitation:
                    -> when could we place "{": (1) if only there are still "{" remain (here is 3) (2) when beginning
                    -> when could we place "}": if only # of "{" added > # of "}" added

            2. How many different states should we try to put on this level
                -> two

                    ""
                /        \
               {          }
             /  \
            {    }
        
        """
    
        # add { on this level
        # add } on this level


# 3. 

def combination(k):
    """
    Total value k = 99 cents
    Coin value: 25, 10, 5, 1 cent

    1. What does the function store on each level and knowing the approximate layer
        -> Option1: 99 layers, each layer pick one coin out of my hand,
        -> Option2: We should say, each layer represents considering one type of coin
    2. How many different states should we try to put on this level
        -> Option1: depends on the number of distinct coins (here is 4)  -> time: O(4^99)
        -> OPtion2: 99   -> time: O(99^4)

    -> Option1
                    root (99)
               /      /    \      \
            25(74)  10(89) 5(94)  1(89)

    -> Option2
                       root (99)
               /        /       \      \
            0*25(99)  1*25     2*25    3*25(24)
         ////\\\\  /////\\\\
         0*10(99)   1*10(99)

        -> this will only have 
    ** Think why not need to recover: the value will be replaced in the fix size array
    ** Think why the loop: for k tree
    ** Dynamically change the branch
    """


# 4. Print Permutation of a string
def permutation(s, ans, level):
    """
                        abc
                    /       |       \
        level0: a(bc)       b(ac)    c(ab)   
                /   \        /\        / \  
        level1: b(c) c(b)  a(c) c(a)  
                /
        level2: c

    1. 3 level in total, each layer pick a remaining string
    2. 3, 2, 1 -> start with 3, decrase one different states until 1 -> n -> n-1 -> n-2, aka remain not use string
    Time: O(n!)
    Space: O()
    """
    # base case
    if level == len(s):
        return None
    # recursive rule
    for i in range(len(s)):
        ans += s[i]
        permutation(s, ans, level+1)
        ans = None