# 使用方法

- 开发环境

1. 安装 Python
2. 安装依赖库 requriments.txt
3. 运行 main.py

```shell
pip install -r requirements.txt
python main.py
```

然后浏览器访问 `http://127.0.0.1:5000/`

- 部署环境(loongnix) 没玩会，现只支持开发环境

1. 安装 Python, Pip, 及 uWSGI 相关依赖
2. 安装依赖库 requriments.txt
3. 运行 main.py

```shell
sudo apt-get install build-essential python3 pipx -y
# python3 -m pip install --upgrade pip # 可以使用国内源
# python3 -m pip install --upgrade pip -i https://pypi.tuna.tsinghua.edu.cn/simple
pipx install requirements.txt
uwsgi --socket 127.0.0.1:3031 --wsgi-file main.py --callable app --processes 4 --threads 2 --stats 127.0.0.1:9191
```

然后浏览器访问 `http://127.0.0.1:3031/`

# 参与开发

请先阅读本项目 [wiki](https://gitee.com/Gakusyun/iwiotss-website/wikis/Home)。
