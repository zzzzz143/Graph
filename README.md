### 安装依赖
./install.sh

### 检查C/CPP代码   --在文件中搜索“可以返回”查找输出位置
python3 run_cppcheck.py test.c/cpp   

### 检查python代码  --在文件中搜索“可以返回”查找输出位置
python3 run_pycheck.py test.py

### 检查java代码    --在文件中搜索“可以返回”查找输出位置
python3 run_javacheck.py test.java

### 控制流图生成--python   -- 结果生成一个exampleCFG.png
python3 run_pyGraph.py   <python_file>

### 控制流图生成--c/cpp    --- 结果生成一个 test.png
python run_cppGraph.py <source_file>

### 控制流图生成--java     --- 例test.java最终生成一个test.png
python run_javaGraph.py <source_file>


### 附录--工具的安装过程
#### cppcheck --- 代码检查-- c++  ✅
```bash
apt-get install cppcheck  

cppcheck test.c
        --enable=style          # 检查代码风格问题
        --enable=performance    # 检查性能问题
        --enable=portability    # 检查可移植性问题
        --enable=all            # 启用所有检查
        --suppress=unusedFunction  # 抑制未使用函数的警告
        --suppress=uninitvar       # 抑制未初始化变量的警告
```

#### pylint        --- 代码检查 -- python ✅
```bash
pip install pylint
pylint test.py
```

#### pmd        --- 代码检查 -- java ✅
```bash
wget https://github.com/pmd/pmd/releases/download/pmd_releases%2F7.13.0/pmd-dist-7.13.0-bin.zip
unzip pmd-dist-7.13.0-bin.zip
alias pmd="/path/to/pmd-bin-7.13.0/bin/pmd"   ###这一步是起别名
pmd check -d <test.java> -R rulesets/java/quickstart.xml -f text
```

#### staticfg --- 控制流图生成--python  ✅

```bash
git clone https://github.com/coetaur0/staticfg.git

cd staticfg

python3 test.py
```

#### Soot --- 控制流图生成--java  
cd Soot

javac test.java

##### 命令1：按语句划分
java -cp soot-4.5.0-jar-with-dependencies.jar soot.tools.CFGViewer -cp . -pp test

##### 命令2：按基本块划分
java -cp soot-4.5.0-jar-with-dependencies.jar soot.tools.CFGViewer -cp . -pp --graph=BriefBlockGraph test

dot Triangle.dot -T png -o Triangle.png


#### CallGraph --- 控制流图生成--cpp  ✅

```bash
git clone https://github.com/bernardnongpoh/CallGraph.git

cd Callgraph
mkdir build
cd build
cmake ..

cd ..
./run.sh test/test_case.c
dot -Tpng .main.dot -o test.png
```

#### doxygen --- 调用图生成   -- 未使用这个

```bash
sudo apt-get install doxygen
sudo apt-get install graphviz


```


