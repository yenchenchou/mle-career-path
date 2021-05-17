const _ = require('lodash');

function sayHello() {
  console.log('Hello, World');
}

_.times(5, sayHello);


/* 
Your previous Python 3 content is preserved below:

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()


# 
# Your previous JavaScript content is preserved below:
# 
# const _ = require('lodash');
# 
# function sayHello() {
#   console.log('Hello, World');
# }
# 
# _.times(5, sayHello);
# 
# 
# /* 
# Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
# 
# 
# Input: root = []
# Output: []
#  */
# 
# 
# /**
#  * Definition for a binary tree node.
#  * function TreeNode(val, left, right) {
#  *     this.val = (val===undefined ? 0 : val)
#  *     this.left = (left===undefined ? null : left)
#  *     this.right = (right===undefined ? null : right)
#  * }
#  */
# /**
#  * @param {TreeNode} root
#  * @return {number[][]}
#  */
# 
# 
# var zigzagLevelOrder = function(root) {
#     
#   levels = [root];
#   ans = [];
#   isReverse = false;
#   
#   while(levels){
#     let level = levels.shift();
#     let size = level.length;
#     let tmp = [];
#     
#     for (let i = 0; i < size - 1; i++){
#       let node = level[i];    
#       
#       if(node.left){
#         tmp.push(node.left);
#       }
#       
#       if(node.right){
#         tmp.push(node.right);
#       }
#     };
#     
#     if(isReverse){
#       ans.push(level.reduce((_result, node) => {
#           return [node.val, ..._result];
#       }, []));
#     }
#     else{
#       ans.push(level.map(node => node.val));    
#     }
#     
#     levels = tmp;
#     isReverse = !isReverse;
#   }
#   
#   return ans;
# };

 */