# Notes Wed Dev

## 1. JavaScript 
### 1. `ES6`
### 2. `DOM`
A data representation of the objects that comprise the structure and content of a HTML and XML document on the web such that we can change the document structure, style, and content. [See MDN link](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction)

### 3. `this`
### 4. `Higher Order Function` vs `First-class function`
* Def Higher-order functions are functions that work on other functions, meaning that they take one or more functions as an argument and can also return a function. Higher-order functions are functions that work on other functions, meaning that they take one or more functions as an argument and can also return a function. [See link](https://stackoverflow.com/questions/10141124/any-difference-between-first-class-function-and-high-order-function)
    

### 5. `callbacks`
A function that wait until the event is finished, usually the function that get passed in the function as a parameter is a callback function.

*  First kind of callback function with events listener 

    ``` JavaScript
    document.addEventListener("click", function(){
        console.log();
    });
    ```

*  Second kind of callback function with events listener 

    ``` JavaScript
    // NOTICE: The callback function is not called by the user, but called by the object that experience the event (such as 'click' here)
    document.addEventListener("click", function(event){ // could be event or e or any word here
        console.log();
    });
    ```
*  Third kind of callback function with events listener 

    ``` JavaScript
    document.addEventListener("click", function(){
        console.log();
    });
    ```

### 6. `var`, `let`, and `const` [see link](https://www.freecodecamp.org/news/var-let-and-const-whats-the-difference/)
    . `var`: Declare a variable. Before the advent of ES6, var declarations ruled. **Can be updated and re-declared**

    ``` JavaScript
    var greeting = "Hello";
    var greeting = "Hey"; // it is acceptable, downside is you may not notice that it is used before and cause error.
    ```

    * `let`: **Can be updated but not re-declared**. It is block within same scoped and usuallt considered a new way to initilaize a new variable instead of `var`

    ``` JavaScript
    let greeting = "Hello";
    let greeting = "Hey"; // it is will cause an error
    
    let greeting = "say Hi";
    if (true) {
        let greeting = "say Hello instead";
        console.log(greeting); // "say Hello instead"
    }
    console.log(greeting); // "say Hi", this is different scope so no error 
    ```

    * `const`: similar to `let` but can't be updated and can't be re-declared. While a const object cannot be updated, the properties of this objects can be updated. Therefore, if we declare a const object as this.

    ``` JavaScript
    const greeting = {
        message: "say Hi",
        times: 4
    }
    
    let greeting = "say Hi";
    greeting = {
        words: "Hello",
        number: "five"
    } 
    greeting.message = "say Hello instead";
    ```

### 7. `hoist`
### 8. `propagate`
### 9. `arrow function`
### 10. `=`, `==`, and `===`
### 11. `querySelector` and `getElement`
