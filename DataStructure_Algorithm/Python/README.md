# Python Need To Know

## Python Objects

### Public, Protected, Private Members

1. Public: accessible from outside the class, aka any part of the program
2. Protected: only accessible to a class derived from it.
3. Private: accessible within the class only

### Methods

1. Class method
    - Instead of accepting a self parameter, **class methods take a cls parameter that points to the class and not the object instance** when the method is called.
    - Because the class method only has access to this cls argument, it can’t modify object instance state. That would require access to self. However, class methods can still modify class state that applies across all instances of the class.

2. Instance method:
    - Most used
    - You can see the method may takes more than one parameter. The most important one, **self, which points to an instance of MyClass when the method is called**.
    - Through the self parameter, instance methods can freely access attributes and other methods on the same object. This gives them a lot of power when it comes to modifying an object’s state. Not only can they modify object state, instance methods can also access the class itself through the self.__class__ attribute.
    - This means instance methods can also modify class state.

3. Static method
    - This type of method takes neither a self nor a cls parameter (but of course it’s free to accept an arbitrary number of other parameters).
    - Therefore a static method can neither modify object state nor class state

### [Python Data Structures](https://www.educative.io/blog/8-python-data-structures#linked-list)

1. List: A sequencial data structure. Python does not have a built in array type. Each value in the array is called an “element” and indexing that represents its position.
    - Pros
        - Simple to create and use data sequences
        - Automatically scale to meet changing size requirements
    - Cons
        - Not optimized for scientific data (unlike NumPy’s array)
    - Applications
        - Shared storage of related values or objects, i.e. myDogs
        - Data collections you’ll loop through

2. Queue: Linear data structure that store data in a “first in, first out” (FIFO) order. Think of waiting to but BTS meal in McDonald's.
    - Pros
        - Automatically orders data chronologically
        - Scales to meet size requirements
        - Time efficient with deque class
    - Cons
        - Can only access data on the ends

3. Stack: Sequential data structure that act as the Last-in, First-out (LIFO) version of queues
    - Pros
        - Offers LIFO data management that’s impossible with arrays
    - Cons
        - Stack memory is limited

4. Heap:
    - Pros
    - Cons

5. Linked list: Eequential collection of data that uses relational pointers on each data node.
    - Pros
        - Efficient insertion and deletion of new elements
        - Useful as a starting point for advanced data structures like graphs or trees
        - Simpler to reorganize than arrays
    - Cons
        - Storage of pointers with each data point increases memory usage
        - Must always traverse the linked list from Head node to find a specific element
    - Applications
        - Solutions that call for frequent addition and removal of data

6. Tree: Relation-based data structure, which specialize in representing hierarchical structures
    - Pros
        - Good for representing hierarchical relationships
        - Dynamic size, great at scale
        - Efficient at search if the tree is not skewed
    - Cons
7. Graph:  data structure used to represent a visual of relationships between data vertices
    - Pros
        - Quickly convey visual information through code
        - Usable for modeling a wide range of real world problems
    - Cons
        - Vertex links are difficult to understand in large graphs
        - Time expensive to parse data from a graph
    - Applications
        - Excellent for modeling networks or web-like structures
        - Used to model social network sites like Facebook
8. Hash Table: Complex data structure capable of storing large amounts of information and retrieving specific elements efficiently.
    - Pros
        - Extremely effective for large data sets
        - Can covert keys in any form to integer indices
    - Cons
        - Collision errors require full overhaul of hash function

## Common questions

1. [Top 100 Python Interview Questions You Must Prepare In 2021](https://www.edureka.co/blog/interview-questions/python-interview-questions/#WhatisthedifferencebetweenlistandtuplesinPython?)
