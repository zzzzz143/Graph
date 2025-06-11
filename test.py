# 文件名：example.py
def factorial(n):
    """计算阶乘"""
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def main():
    """主函数"""
    number = 5
    print(f"计算 {number} 的阶乘：")
    result = factorial(number)
    print(f"结果：{result}")

    # 循环结构
    for i in range(3):
        print(f"循环迭代：{i}")

    # 条件结构
    if number > 10:
        print("数字大于10")
    elif number > 5:
        print("数字大于5但小于等于10")
    else:
        print("数字小于等于5")

    # 调用另一个函数
    greet("Alice")

def greet(name):
    """打印问候语"""
    print(f"Hello, {name}!")

if __name__ == "__main__":
    main()