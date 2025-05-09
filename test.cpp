#include <iostream>

// 未使用的函数
int unusedFunction() {
    return 42;
}

// 未初始化的变量
int main() {
    int uninitialized;
    std::cout << "The uninitialized variable is: " << uninitialized << std::endl;

    // 逻辑问题：除以零
    int zero = 0;
    int result = 10 / zero;

    // 内存泄漏
    int* ptr = new int;
    // delete ptr;

    return 0;
}