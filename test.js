// test.js

// 未使用的变量
var unusedVar;

// 缺少空格的运算符
var sum = 1+2;

// 缺少冒号的 switch 语句
switch(a) {
    case 1:
        console.log('Case 1');
    break;
    // 缺少 break 或 fall-through 注释
    case 2:
        console.log('Case 2');
    case 3:
        console.log('Case 3');
}

// 缺少括号的 if 语句
if (a === 2)
    console.log('This should be wrapped in parens');

// 缺少逗号的数组
var list = [1,2,3];

// 缺少分号的语句
var message = 'Hello, World'
console.log(message)

// 函数声明没有使用 function 关键字
var greet = function(name) {
    return 'Hello ' + name;
}

// 函数体内的变量提升
console.log(greeting);
var greeting = 'Hello';

// 使用了未声明的变量
console.log(undeclaredVar);

// 过长的行
var veryLongStringWithoutLineBreak = "This string is much too long and should be wrapped in multiple lines for better readability.";

// 未使用的函数
function unusedFunction() {
    console.log('This function is never used.');
}

// 缺少空格的函数调用
console.log(greet('ESLint'));