/*
1047. Remove All Adjacent Duplicates In String

You are given a string s consisting of lowercase English letters. 
A duplicate removal consists of choosing two adjacent and equal letters and removing them.
 
We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

Example 2:

Input: s = "azxxzy" Output: "ay"

s = "azxyz" 

Hint1: 
Use a stack to process everything greedily.

*/

/**
 * @param {string} s
 * @return {string}
 */

 var removeDuplicates = function(s) {
    const stack = [];
    for(let i = 0; i < s.length; i++){
        const char = s[i];
        if(stack.length > 0 && stack[stack.length - 1] === char){
            stack.pop();
            continue;
        }
        stack.push(char);
    }
    return stack.join("");
};