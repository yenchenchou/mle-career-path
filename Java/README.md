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
   6. dereference: the action of visiting the object according to the reference called dereference (like below 
   `rose.getnewname()`, rose is reference, this action is dereference)
   
   
## Working with objects (Class 1)

   1. Suppose we say:
   
    From a senmantic standpoint, the belowe means you create a reference called firstStudent that point to a class 
    (Student) with parameter called "Tom"
    
    ``` 
        Student firstStudent = new Student("Tom")
    ```
   -> there are three main operations in total:
        * declaration: associate a variable with an object type `Student firstStudent`. `firstStudent` is a reference
        * instantiation: The `new` keyword is a Java operator that creates the object `firstStudent = new Student(...)`
        * initialization: The `new` operator is followed by a call to a constructor, which initialize the new object
    
    
## Object Memory layout (Class 1)

   1. Memory space in Java: stack and heap
   2. Stack: a call stack is a stack data structure that stores information of the active subordinates (the function 
    that are under execution) of a computer program. 
   3. Heap: the place where all the object store.
   
   * **Note**: variables(reference) can be in stack or heap, for example stack variable in object and heap variable 
   (the fields). That is to say, the thing you use new to create is in Java heap
   
   
## Reference and Object defining (Class 1):
   * Example:
   
    Student Student
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
    
    
## Static, final, and more things to know (Class 1)
   * `final`: can use everywhere `final class` (can't be inherited), `final method` (can't be overwrite), `final field`.
   **final is not saying the content of the object can't be changed, it is saying the reference will not change
   (point to the same reference) -> class 1 2:06:00**
   * `static`:  keyword is mainly used for memory management. It can be used with variables, methods, blocks and nested 
   classes. It is a keyword which is used to share the same variable or method of a given class. Basically, 
   `static` is used for a constant variable or a method that is same for every instance of a class.
   * Example code

    ```
    public class Student {
    
        public int age;  // (member) field, of course this field is a variable
        private final String name;  // constant field
        private static String name; // static field
        private static final String Breeting="Hello"  // static constant field 
        
        public Student(String name){
            this.name = name  // constructor: a special method that is used to initialize the params of objects
        }
        
        public int getAge(){  // (member) method
            return age;
        }
        
        public void setAge(int age){  // (member) method
            this.age = age;
        }

        public String getName(){  // (member) method
            return name;
        }    
    }
    
    ```

## Primitive type and Class type (Class 1)
   * class types: store in heap, operated by reference
   * primitive types: not objects, no reference, think of as original data structure from the beginning of java appears
   
   
## Constructor, NUll, pointers (Class 1)
   * Constructor: constructor: a special method that is used to initialize a custom objects with self defined 
   parameters. The name should be the as the class name, see above code.
   * this: point to the instance (current object itself) -> the instance name in front of .methods. 調用這個method 
   的當前instance. Mandatory to write `this` when argument name same as field name. Look below:
   
   ```
   public class Student{
        String name,
        void setName(String name){
            this.name = name;
        }
   }
   ```
    
   * NULL: empty reference
   * NUllPointerException: happens when deferencing but does not get anything then it is a NUllPointerException. **Not because you find a NULL value**
   * ArrayIndexOutOfBound


## Java parameter passing
**Java is always pass by value during parameter passing:**
    * primitive type: copy of the value itself
    * object: copy of the object reference (複製名片)

    * Notice: be precise when describing, things like "reference", "dereference" actions need to be mentioned instead of inprofessional word
   