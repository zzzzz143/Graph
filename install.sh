#!/bin/bash
# install.sh

# 确保脚本以 root 权限运行
if [ "$(id -u)" -ne 0 ]; then
    echo "该脚本必须以 root 权限运行" >&2
    exit 1
fi

# 更新包列表
apt-get update

# 安装编译工具和 pip
apt-get install -y build-essential python3-pip

# 安装 cppcheck 和 graphviz
apt-get install -y cppcheck graphviz

# 安装 pylint
pip3 install pylint

echo "所有依赖项已安装完毕。"