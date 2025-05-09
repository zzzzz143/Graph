import sys
from staticfg import CFGBuilder

def generate_cfg_from_args():
    # 检查命令行参数
    if len(sys.argv) < 2:
        print("Usage: python run_pyGraph.py <python_file>")
        sys.exit(1)

    # 从命令行参数获取 Python 文件名
    python_file = sys.argv[1]

    # 构建控制流图
    cfg = CFGBuilder().build_from_file('example', python_file)

    # 可视化控制流图，生成 PNG 文件，但不自动打开
    cfg.build_visual('exampleCFG', 'png', show=False)

if __name__ == "__main__":
    generate_cfg_from_args()