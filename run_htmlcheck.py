import subprocess
import os
import sys

def run_htmlcheck(html_code_file):
    # 检查文件是否存在
    if not os.path.exists(html_code_file):
        print(f"Error: File '{html_code_file}' not found.")
        sys.exit(1)

    # 读取 html 代码
    with open(html_code_file, 'r') as file:
        html_code = file.read()

    # 获取文件扩展名
    file_extension = os.path.splitext(html_code_file)[1]

    # 创建临时文件名
    temp_file_name = f"temp{file_extension}"

    # 将代码保存到临时文件
    with open(temp_file_name, 'w') as temp_file:
        temp_file.write(html_code)

    # 构造 htmlhint 命令
    command = [
        'htmlhint',
        temp_file_name
    ]

    try:
        # 运行 htmlhint 命令，同时捕获 stdout 和 stderr
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, check=True)
        
        # 打印标准输出
        print("htmlhint output:")
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # 如果 htmlhint 命令失败，打印错误信息
        print("htmlhint encountered an error:")
        print(e.stdout)  # 打印标准输出（包含 stderr 的内容）      # 这里是找到的错误--可以返回
    finally:
        # 删除临时文件
        os.remove(temp_file_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run_htmlcheck.py <html_code_file>")
        sys.exit(1)

    # 获取 html 代码文件名
    html_code_file = sys.argv[1]

    # 调用函数运行 htmlhint
    run_htmlcheck(html_code_file)