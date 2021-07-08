/*
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order, and each of their nodes contains a single digit. 
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Input: l1 = [0], l2 = [0]
Output: [0]


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

https://assets.leetcode.com/uploads/2020/10/02/addtwonumber1.jpg

[9, 9]
[9]

*/


/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
 var addTwoNumbers = function(l1, l2) {
    
    let arr1 = []; // [9, 9]
    let arr2 = []; // [9]
    let ans = 0;

    while(l1){
        arr1.push(l1.val);
        l1 = l1.next;
    }

    while(l2){
        arr2.push(l2.val);
        l2 = l2.next;
    }

    // i = 0 -> 9 * 10^(2-1-0)
    // i = 1 -> 9 * 10^(2-1-1)


    for(let i = 0; i < arr1.length; i++){
        ans += arr1[arr1.length - 1 - i] * Math.pow(10, arr1.length - 1 - i);
    }

    // for(let i = arr1.length - 1; i >= 0 ; i--){
    //     ans += arr1[i] * Math.pow(10, i);
    // }

    for(let i = 0; i < arr2.length; i++){
        ans += arr2[arr2.length - 1 - i] * Math.pow(10, arr2.length - 1 - i);
    }

    let finalList = new ListNode();
    let current = finalList;

    // ans = String(ans); // 108
                  
    // 8 -> 0 -> 1
    // for(let i = ans.length - 1; i >= 0 ; i--){
    while(ans > 0){
        current.val = ans % 10;
        current.next = new ListNode();
        current = current.next;

        ans = Math.floor(ans / 10);
    }

    return finalList;

};

// ListNode(0)