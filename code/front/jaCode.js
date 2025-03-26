// alert("Hello World");

// 基础语法

// 1. 变量
let name = "John";
let age = 30;
let isMarried = true;
let message = "Hello " + name + ", you are " + age + " years old.";
console.log(message);

// 反引号可以不用加+，直接可以用${}来表示变量
let message2 = `Hello ${name}, you are ${age} years old.`;
console.log(message2);

    //  函数
    /**
     * 该函数用于向指定的人打招呼
     * @param {string} name - 要打招呼的人的名字
     */
    function greet(name) {
      // 打印问候语
      console.log("Hello " + name + "!");
  }
  // 调用 greet 函数，向 "John" 打招呼，并将结果赋值给 result 变量
  greet("John");
  //函数表达式和箭头函数
  // 函数表达式
  let myFunc = function() {
    console.log("This is a function expression.");
  };
  myFunc();
  // 箭头函数
  let myArrowFunc = () => {
    console.log("This is an arrow function.");
  };
  myArrowFunc();

  // 自定义一个属性，并调用里面的属性和方法
  let person = {
    name: "John",
    age: 30,
    greet: function() {
      console.log("Hello " + this.name + "!");
    }   
  };
  // 调用属性名和方法
  console.log(person.name);
  person.greet();

  // json -js对象标记法
  // 定义一个json对象
  let jsonTest = {
    "name": "John",
    "age": 30,
    "isMarried": true
  };

JSON.stringify(jsonTest); // 将json对象转换为json字符串

// 定义一个json字符串
let jsonString = '{"name":"John","age":30,"isMarried":true}';

let jsonObj = JSON.parse(jsonString);   // 将json字符串转换为json对象

console.log(jsonObj.name); // 输出 "John"
console.log(jsonObj.age); // 输出 30
console.log(jsonObj.isMarried); // 输出 true










// // 2. 条件语句
// if (age >= 18) {
//   console.log("You are old enough to vote.");
// } else {
//   console.log("You are not old enough to vote.");
// }
// // 3. 循环语句
// for (let i = 0; i < 5; i++) {
//   console.log(i);
// }
// // 4. 函数
// function greet(name) {
//   console.log("Hello " + name + "!");
// }
// greet("John");
// // 5. 数组
// let fruits = ["apple", "banana", "orange"];
// console.log(fruits[1]);
// // 6. 对象
// let person = {
//   name: "John",
//   age: 30,
//   greet: function() {
//     console.log("Hello " + this.name + "!");
//   }
// };
// person.greet();
// // 7. 事件
// let button = document.getElementById("myButton");
// button.addEventListener("click", function() {
//   console.log("Button clicked!");
// }); 

// // 高级语法   

// // 1. 类
// class Person {
//   constructor(name, age) {
//     this.name = name;
//     this.age = age;
//   }
//   greet() {
//     console.log("Hello " + this.name + "!");
//   }
// }
// let john = new Person("John", 30);









// 2. 模块化
// 3. 异步编程
// 4. 正则表达式
// 5. 事件循环
// 6. 原型链
// 7. 作用域
// 8. 闭包
// 9. 迭代器与生成器
// 10. 装饰器
// 11. 反射
// 12. 元编程
// 13. 类型系统
// 14. 泛型
// 15. 异步编程
// 16. 并发编程
// 17. 并行编程
// 18. 函数式编程
// 19. 面向对象编程
// 20. 面向切面编程
// 21. 面向服务编程
// 22. 面向数据编程
// 23. 面向过程编程
// 24. 面向事件编程
// 25. 面向组件编程
// 26. 面向模式编程
// 27. 面向主题编程
// 28. 面向体系编程
// 29. 面向范式编程
// 30. 面向产品编程
// 31. 面向用户编程
// 32. 面向场景编程
// 33. 面向工具编程
// 34. 面向框架编程
// 35. 面向语言编程
// 36. 面向数据库编程
// 37. 面向云计算编程
// 38. 面向大数据编程
// 39. 面向物联网编程
// 40. 面向人工智能编程
// 41. 面向机器学习编程
// 42. 面向深度学习编程
// 43. 面向增强现实编程
// 44. 面向区块链编程
// 45. 面向智能合约编程
// 46. 面向智能网格编程
// 47. 面向智能城市编程