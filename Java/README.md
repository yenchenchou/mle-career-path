# Java Debug 

## Java Basics (Class 1)

   1. semantic and implementation: The code is semantic and the command code is the implementation (like JVM)
   2. Everything is **almost** an object, each object has a type 
        * states (fields)
        * behavior (methods)
        * exceptions:
            * primitives: int, boolean, byte...
            * fields (the fields themselves not the contents)
   3. class: define a states and behavior of an object
   4. object: as known as instance
   5. reference: the address where the object store
   6. dereference: the action of visiting the object according to the reference called dereference
   
## Working with objects (Class 1)

   1. Suppose we say:
   
    From a senmantic standpoint, the belowe means you create a reference called firstStudent that point to a class 
    (Student) with parameter called "Tom"
    
    ``` 
        Student firstStudent = new Student("Tom")
    ```
   -> there are three main operations in total:
        * declaration: associate a variable with an object type `Student firstStudent`
        * instantiation: The `new` keyword is a Java operator that creates the object `firstStudent = new Student(...)`
        * initialization: The `new` operator is followed by a call to a constructor, which initialize the new object
    
## Object Memory layout (Class 1)

   1. Memory space in Java: stack and heap
   2. Stack: a call stack is a stack data structure that stores information of the active subordinates (the function 
    that are under execution) of a computer program. 
   3. Heap: the place where all the object store.
   
   * **Note**: variables(reference) can be in stack or heap, for example stack variable in object and heap variable 
   (the fields). That is to say, the thing you use new to create is in Java heap
   
   
## Refrence and Object:
   * Example:
   
    Student jack = new Student("jack")
    Student rose = new Student("rose")
    jack = rose
   -> This only mean the reference value of rose is copied and assign to object jack
   
   * every Java file can only has at most one public class
   * The .java file name should be same as the name of public class <class_name> {}
   * **Please reference Google Java coding style and learn this early**
   * `public static void main` is the main entrance of any Java Program. `void` will not return anything. But how to 
   identify the method itself? Method signature is create by the name of method and the list of parameter types. 
   The order matters. Not include return value's type and not include exception list.
   *  
    
   
   
