/*
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, 
and return an array of the non-overlapping intervals that cover all the intervals in the input.


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Input: intervals = [[1,4], [4,5], [0, 1]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

*/

/**
 * @param {number[][]} intervals
 * @return {number[][]}
 */
 var merge = function(intervals) {
    
    let sortedIntervals = intervals.sort((a,b) => a[0] - b[0]);
    let ans = [];

    for(let i = 0; i < sortedIntervals.length; i++){
        
        if(i === 0){
            ans.push(sortedIntervals[i]);
            continue;
        }

        const first = ans[ans.length - 1];
        const second = sortedIntervals[i];
        const secondIntervalStart = second[0];
        const secondIntervalEnd = second[1];
        const firstIntervalStart = first[0];
        const firstIntervalEnd = first[1];

        if(secondIntervalStart <= firstIntervalEnd){
            // ans.push([firstIntervalStart, secondIntervalEnd])
            first[0] = firstIntervalStart;
            first[1] = Math.max(firstIntervalEnd, secondIntervalEnd);
        }
        else{
            // ans.push(first);
            // ans.push(second);
            // [1,4], [2,3]
            ans.push(second);
        }
    }

    return ans;
};