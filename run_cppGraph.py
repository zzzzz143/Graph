import subprocess
import os
import sys
import re
import argparse

def extract_functions_with_regex(file_path):
    """
    使用正则表达式提取C++或C文件中的函数名。
    注意：这种方法可能不够准确，尤其是对于复杂的C++代码。
    """
    function_pattern = re.compile(r'\b\w+\s+\w+\s*\([^)]*\)\s*\{')
    with open(file_path, 'r') as file:
        content = file.read()
    functions = function_pattern.findall(content)
    function_names = [re.search(r'\b\w+\s+(\w+)\s*\(', func).group(1) for func in functions]
    return function_names

def generate_flowchart(file_path, function_name, output_dir):
    """
    使用cxx2flow和dot为指定函数生成SVG格式的流程图，并将其转换为PNG。
    """
    svg_output_file = os.path.join(output_dir, f"{function_name}.svg")
    png_output_file = os.path.join(output_dir, f"{function_name}.png")

    # 生成SVG文件
    svg_command = f"./cxx2flow {file_path} {function_name} | dot -Tsvg -o {svg_output_file}"
    subprocess.run(svg_command, shell=True, check=True)
    print(f"生成SVG流程图：{svg_output_file}")

    # 将SVG转换为PNG
    png_command = f"convert {svg_output_file} {png_output_file}"
    subprocess.run(png_command, shell=True, check=True)
    print(f"生成PNG流程图：{png_output_file}")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python run_cppGraph.py <source_file> [-o <output_directory>]")
        print("  <source_file>: C++或C文件的路径")
        print("  [-o <output_directory>]: 输出目录，默认为 'flowcharts'")
        sys.exit(1)

    # 获取源代码文件名
    source_file = sys.argv[1]

    # 解析可选的输出目录参数
    output_dir = "flowcharts"  # 默认输出目录
    if len(sys.argv) > 2 and sys.argv[2] == "-o" and len(sys.argv) > 3:
        output_dir = sys.argv[3]

    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 提取文件中的所有函数名
    function_names = extract_functions_with_regex(source_file)
    if not function_names:
        print("未找到任何函数。")
        sys.exit(1)

    print(f"在文件 {source_file} 中找到以下函数：{', '.join(function_names)}")

    # 为每个函数生成流程图
    for function_name in function_names:
        generate_flowchart(source_file, function_name, output_dir)