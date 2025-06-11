// 文件名：example.cpp
#include <iostream>

// 函数声明
void functionA();
void functionB();
void functionC();

// 主函数
int main() {
    std::cout << "Program starts." << std::endl;
    functionA();
    functionB();
    std::cout << "Program ends." << std::endl;
    return 0;
}

// 函数A
void functionA() {
    std::cout << "Function A is called." << std::endl;
    functionC();
}

// 函数B
void functionB() {
    std::cout << "Function B is called." << std::endl;
}

// 函数C
void functionC() {
    std::cout << "Function C is called." << std::endl;
}