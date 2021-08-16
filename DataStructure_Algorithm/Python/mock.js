/*
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
return the k closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).


Input: points = [[1,3],[-2,2]], k = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

Input: points = [[3,3],[5,-1],[-2,4]], k = 2
Output: [[3,3],[-2,4]]
Explanation: The answer [[-2,4],[3,3]] would also be accepted.

Constraints:
1 <= k <= points.length <= 104
*/


var getDistance = (point) => {
    return (point[0] ** 2 + point[1] ** 2) ** 0.5;
}

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 var kClosest = function(points, k) {
    
    const maxHeap = new MaxHeap();

    for(let i = 0; i < points.length; i++){
        const point = points[i];

        if(maxHeap.size() < k){
            maxHeap.add(point);
        }
        else{
            const maxPoint = maxHeap.peek();

            if(getDistance(point) < getDistance(maxPoint)){
                maxHeap.removeTop();   
                maxHeap.add(point);
            }
        }
    }

    return maxHeap.heap;
};

class MaxHeap {
    constructor(){
        this.heap = [];
    }

    getParent(index){
        return index - 1 >= 0 ? Math.floor((index - 1) / 2) : 0;
    }

    add(point){
        this.heap.push(point);
        
        const heap = this.heap;

        let currentIndex = heap.length - 1;
        let parent = this.getParent(currentIndex);

        while(parent !== currentIndex && getDistance(parent) < getDistance(currentIndex)){
            [heap[currentIndex], heap[parent]] = [heap[parent], heap[currnetIndex]];

            current = parent;
            parent = this.getParent(current);
        }
    }

    peek(){
        return this.heap[0]
    }

    heapify(index){
        let smallest = index;
        let left = 2 * index + 1;
        let right = 2 * index + 2;

        if(this.heap[smallest] < this.heap[left]){
            smallest = left;
        }

        if(this.heap[smallest] < this.heap[right]){
            smallest = right;
        }

        if(smallest !== index){
            [this.heap[smallest], this.heap[index]] = [ this.heap[index], this.heap[smallest]];

            this.heapify(smallest);
        }
    }

    removeTop(){
        const heap = this.heap;
        const top = heap[0];


        [heap[0], heap[heap.length - 1]] = [heap[heap.legnth - 1], heap[0]];

        this.heapify(0);
    }
}