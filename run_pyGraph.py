import os
import sys
from staticfg import CFGBuilder

def generate_cfg_for_all_functions(python_file, output_folder):
    # 确保输出文件夹存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 构建控制流图
    cfg = CFGBuilder().build_from_file('example', python_file)

    # 遍历所有函数并生成控制流图
    for func_name, function_cfg in cfg.functioncfgs.items():
        # 生成控制流图文件名
        output_file = os.path.join(output_folder, f"{func_name}_CFG")

        # 可视化指定函数的控制流图，生成 PNG 文件，但不自动打开
        function_cfg.build_visual(output_file, 'png', show=False)
        print(f"Control flow graph for function '{func_name}' generated as '{output_file}'.")

def delete_cfg_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith("_CFG") and not filename.endswith("_CFG.png"):
            os.remove(os.path.join(folder_path, filename))
            print(f"Deleted {filename}")

if __name__ == "__main__":
    # 检查命令行参数
    if len(sys.argv) < 3:
        print("Usage: python run_pyGraph.py <python_file> <output_folder>")
        sys.exit(1)

    # 从命令行参数获取 Python 文件名和输出文件夹路径
    python_file = sys.argv[1]
    output_folder = sys.argv[2]

    # 生成所有函数的控制流图
    generate_cfg_for_all_functions(python_file, output_folder)
    delete_cfg_files(output_folder)