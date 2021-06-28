/*
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


*/

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 var kClosest = function(points, k) {
    
    let ans = [];

    for(let i = 0; points.length; i++){
        const distance = Math.pow(points[i][0], 2) + Math.pow(points[i][1], 2);

        ans.push(Math.pow(distance, 0.5));
    }

    ans.sort((a, b) => b - a );

    return ans.slice(0, k);
};

