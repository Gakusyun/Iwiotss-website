# 使用方法

这是一个依托于 Flask 的项目，所以需要安装 Python 和 Flask 库。

安装 Python:
https://www.python.org/downloads/

安装完 Python 后，请安装 pip:
在命令行中输入命令：

```shell
    python -m pip install --upgrade pip
```
或者，可以使用国内镜像源安装 pip:
```shell
    python -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
```
安装 依赖库:
```shell
    pip install -r requirements.txt
```
如果不行，可以试试：
```shell
    pip install --break-system-packages -r requirements.txt
```
现在，就可以运行这个项目了:
```shell
    python main.py
```
当命令行中出现：
> * Running on http://127.0.0.1:5000
> 
> Press CTRL+C to quit
说明项目已经运行成功。

这时，就可以在浏览器中输入：`http://127.0.0.1:5000/`就能进入主页了。

