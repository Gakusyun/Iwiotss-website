from flask import Flask, render_template, url_for, request, redirect
import json, os, random

app = Flask(__name__)
islogin = False


def get_temperature() -> int:
    temperature = random.randint(0, 50)  # 这里写具体实现
    return temperature


def get_humidity() -> int:
    humidity = random.randint(0, 99)  # 这里写具体实现
    return humidity


def get_pressure() -> int:
    pressure = random.randint(10, 100)  # 这里写具体实现
    return pressure


def get_device_number() -> int:
    device_number = random.randint(2, 10)  # 这里写具体实现
    return device_number


def get_power() -> int:
    power = random.randint(100, 1000)  # 这里写具体实现
    return power


def get_power_consumption() -> int:
    power_consumption = random.randint(100, 200)  # 这里写具体实现
    return power_consumption


def check_credentials(username: str, password: str) -> bool:
    print(username, password)
    users_directory = "./users"
    try:
        users_files = os.listdir(users_directory)
        if username + ".json" in users_files:
            user_file_path = os.path.join(users_directory, username + ".json")
            with open(user_file_path, "r") as f:
                data = json.load(f)
                if data.get("password") == password:
                    return True
    except Exception as e:
        print(f"An error occurred: {e}")
    return False


@app.route("/")
def home():
    return render_template(
        "index.html",
        temperature=get_temperature(),
        humidity=get_humidity(),
        pressure=get_pressure(),
        device_number=get_device_number(),
        power=get_power(),
        power_consumption=get_power_consumption(),
    )


@app.route("/about")
def about():
    developer = ["高学骏", "付典雅", "李恺烨"]
    random.shuffle(developer)
    return render_template("about.html", developer=developer)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if check_credentials(username, password):
            global islogin
            islogin = True
            return redirect(url_for("home"))
        else:
            return '登录失败，请重试！<a href="login">redo</a>'
    else:
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    global islogin
    if islogin:
        return redirect(url_for("self"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # 在users文件夹下创建一个文件，文件名是username.json
        users_directory = "./users"
        user_file_path = os.path.join(users_directory, username + ".json")
        if not os.path.exists(users_directory):
            os.makedirs(users_directory)
        # 打开（或创建）用户文件准备写入数据
        with open(user_file_path, "w") as user_file:
            # 假设我们有一些用户信息要保存，例如字典类型
            user_data = {"password": password}
            # 使用json.dump将数据写入文件
            json.dump(user_data, user_file, indent=4)
            return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/self")
def setting():
    return render_template("self.html")


if __name__ == "__main__":
    app.run(debug=True)
