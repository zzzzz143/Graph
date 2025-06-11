import subprocess
import os
import sys
import re

def convert_dot_to_png(output_dir):
    # 将生成的 .dot 文件转换为 .png 图片
    for dot_file in os.listdir(output_dir):
        if dot_file.endswith(".dot"):
            dot_path = os.path.join(output_dir, dot_file)
            # 提取最后一个空格后的部分作为函数名
            parts = dot_file.split()
            func_name = parts[-1].replace('.dot', '')
            png_file = os.path.join(output_dir, func_name + ".png")
            subprocess.run(["dot", "-Tpng", dot_path, "-o", png_file], check=True)
            print(f"Converted {dot_file} to {png_file}")

def cleanup(output_dir):
    # 删除除了 .png 文件之外的所有文件
    for file in os.listdir(output_dir):
        file_path = os.path.join(output_dir, file)
        if not file.endswith(".png"):
            os.remove(file_path)
            print(f"Deleted {file_path}")

def generate_cfg(source_file, output_dir):
    # 检查源文件是否存在
    if not os.path.exists(source_file):
        print(f"Error: Source file '{source_file}' not found.")
        sys.exit(1)
    
    # 获取源文件的路径和名称
    source_dir = os.path.dirname(source_file)
    source_name = os.path.splitext(os.path.basename(source_file))[0]
    class_file = os.path.join(source_dir, f"{source_name}.class")
    
    # 编译 Java 文件
    compile_command = ["javac", source_file]
    
    # 定义 Soot 的 CFGViewer 命令
    soot_command = [
        "java",
        "-cp", "Soot/soot-4.5.0-jar-with-dependencies.jar",
        "soot.tools.CFGViewer",
        "-cp", ".",
        "-pp",
        "--graph=BriefBlockGraph",
        "--output-dir", output_dir,  
        source_name
    ]
    
    try:
        # 运行 javac 命令编译 Java 文件
        subprocess.run(compile_command, check=True)
        
        # 检查编译后的 .class 文件是否存在
        if not os.path.exists(class_file):
            raise FileNotFoundError(f"Failed to compile {source_file} to {class_file}")
        
        # 运行 Soot 的 CFGViewer 命令生成控制流图
        subprocess.run(soot_command, check=True)
        
        print(f"Control Flow Graph generated for {source_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the control flow graph: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python run_javaGraph.py <source_file> <output_dir>")
        sys.exit(1)
    
    # 获取源代码文件名
    source_file = sys.argv[1]
    output_dir = sys.argv[2]
    
    # 调用函数生成控制流图
    generate_cfg(source_file,output_dir)

    # 转换 .dot 文件为 .png 图片
    convert_dot_to_png(output_dir)

    # 清理输出目录，只保留 .png 文件
    cleanup(output_dir)