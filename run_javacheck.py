import subprocess
import os
import sys

def run_javacheck(java_code_file,output_path):
    # 检查文件是否存在
    if not os.path.exists(java_code_file):
        print(f"Error: File '{java_code_file}' not found.")
        sys.exit(1)

    if not os.path.exists(output_path):
        open(output_path, 'w').close()  # 创建一个空文件
        print(f"File '{output_path}' not found but created.")

    # 读取 java 代码
    with open(java_code_file, 'r') as file:
        py_code = file.read()

    # 获取文件扩展名
    file_extension = os.path.splitext(java_code_file)[1]

    # 创建临时文件名
    temp_file_name = f"temp{file_extension}"

    # 将代码保存到临时文件
    with open(temp_file_name, 'w') as temp_file:
        temp_file.write(py_code)

    # 构造 pmd 命令
    command = [    # "/path/to/pmd-bin-7.13.0/bin/pmd"
        './pmd-bin-7.13.0/bin/pmd', 'check', '-d', temp_file_name, '-R', 'rulesets/java/quickstart.xml', '-f', 'text', '-r', output_path ,'--no-cache'
    ]

    try:
        # 运行 pmd 命令，同时捕获 stdout 和 stderr
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
        
        # 打印标准输出
        print("pmd output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # 如果 pmd 命令失败，打印错误信息
        print("pmd encountered an error:")
        print(e.stdout)  # 打印标准输出（包含 stderr 的内容）    # 这里是找到的错误--可以返回
    finally:
        # 删除临时文件
        os.remove(temp_file_name)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python run_javacheck.py <java_code_file> <output_path>")
        sys.exit(1)

    # 获取 java 代码文件名
    java_code_file = sys.argv[1]
    output_path = sys.argv[2]

    # 调用函数运行 pmd
    run_javacheck(java_code_file, output_path)