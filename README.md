# 使用方法

这是一个依托于 Flask 的项目，所以需要安装 Python 和 Flask 库。

安装 Python:
https://www.python.org/downloads/

安装完 Python 后，请安装 pip:
在命令行中输入命令：
```shell
sudo apt install python3-pip #使用 apt 安装 pip
```
创建虚拟环境：
```shell
    python3 -m venv env #创建虚拟环境
```
激活虚拟环境：
```shell
    source env/bin/activate #激活虚拟环境
```
安装依赖：
```shell
    pip install -r requirements.txt #安装依赖
```
现在，就可以运行这个项目了:
```shell
    python3 app.py
```
当命令行中出现：
> * Running on http://127.0.0.1:5000
> 
> Press CTRL+C to quit
说明项目已经运行成功。

这时，就可以在浏览器中输入：`http://127.0.0.1:5000/`就能进入主页了。

退出虚拟环境：
```shell
    deactivate #退出虚拟环境
```