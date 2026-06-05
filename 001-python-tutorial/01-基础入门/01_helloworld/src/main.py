"""
@author lingwh
@desc python helloworld 案例
@date 2026/6/5 16:20

搭建 python 环境

1. 下载 python https://www.python.org/ftp/python/ 或 https://www.python.org/downloads/
2. 安装 python 解释器
3. 配置 python 环境变量、Scripts环境变量(pip等命令在Scripts目录下)
4. 验证 python 安装和环境变量配置是否成功
    python --version
    pip --version
5. 设置 pip 使用国内镜像源
    pip config set global.index-url http://mirrors.aliyun.com/pypi/simple/
    pip config set install.trusted-host mirrors.aliyun.com
6. 查看 pip 镜像配置
    pip config list #
7. python2和python3区别?
    python2默认不支持中文，python3默认支持中文
8. python 经典教程
    https://liaoxuefeng.com/books/python/introduction/index.html
"""

print("hello world!")