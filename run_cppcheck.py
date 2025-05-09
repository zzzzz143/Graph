import subprocess
import os
import sys

def run_cppcheck(cpp_code_file):
    # 检查文件是否存在
    if not os.path.exists(cpp_code_file):
        print(f"Error: File '{cpp_code_file}' not found.")
        sys.exit(1)

    # 读取C/C++代码
    with open(cpp_code_file, 'r') as file:
        cpp_code = file.read()

    # 获取文件扩展名
    file_extension = os.path.splitext(cpp_code_file)[1]

    # 创建临时文件名
    temp_file_name = f"temp{file_extension}"

    # 将代码保存到临时文件
    with open(temp_file_name, 'w') as temp_file:
        temp_file.write(cpp_code)

    # 构造 cppcheck 命令
    command = [
        'cppcheck',
        temp_file_name,
        '--enable=style',
        '--enable=performance',
        '--enable=portability',
        '--enable=all'
    ]

    try:
        # 运行 cppcheck 命令，同时捕获 stdout 和 stderr
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        
        # # 打印标准输出
        # print("Cppcheck output:")
        # print(result.stdout)
        
        # 检查是否有标准错误输出
        if result.stderr:
            print("Cppcheck error output:")
            print(result.stderr)                 # 这里是找到的错误--可以返回
    except subprocess.CalledProcessError as e:
        # 如果 cppcheck 命令失败，打印错误信息
        print("Cppcheck encountered an error:")
        print(e.stderr)
    finally:
        # 删除临时文件
        os.remove(temp_file_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_cppcheck.py <cpp_code_file>")
        sys.exit(1)

    # 获取C/C++代码文件名
    cpp_code_file = sys.argv[1]

    # 调用函数运行 cppcheck
    run_cppcheck(cpp_code_file)