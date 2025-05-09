import subprocess
import os
import sys

def generate_call_graph(source_file, output_file):
    # 定义 CallGraph 脚本路径
    callgraph_script = "CallGraph/run.sh"
    
    # 定义 dot 文件路径
    dot_file = "temp.bc.callgraph.dot"
    
    try:
        # 运行 CallGraph 脚本生成 .dot 文件
        subprocess.run([callgraph_script, source_file], check=True)
        
        # 检查 .dot 文件是否生成
        if not os.path.exists(dot_file):
            raise FileNotFoundError(f"Failed to generate {dot_file}")
        
        # 使用 dot 工具将 .dot 文件转换为 PNG 文件
        subprocess.run(["dot", "-Tpng", dot_file, "-o", output_file], check=True)
        
        print(f"Call Graph saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while generating the call graph: {e}")
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python run_cppGraph.py <source_file>")
        sys.exit(1)
    
    # 获取源代码文件名
    source_file = sys.argv[1]
    
    # 输出文件固定为 test.png
    output_file = "test.png"
    
    # 调用函数生成调用图
    generate_call_graph(source_file, output_file)