from flask import Flask, render_template, url_for, request, redirect
import json, os, random

app = Flask(__name__)
is_login = False


class User(object):
    username = ""


class Sensor(object):  # 这里写了一个类，每多一个传感器，就创建一个对象
    instances = 0

    def __init__(self):
        Sensor.instances += 1  # 计数，用于获取传感器数量
        self.get_latest_data()

    def get_latest_data(self):  # 这里写具体实现
        self.temperature = random.randint(0, 50)
        self.humidity = random.randint(0, 99)
        self.pressure = random.randint(10, 100)
        self.power = random.randint(100, 1000)
        self.power_consumption = random.randint(100, 200)

    def get_temperature(self) -> int:
        return self.temperature

    def get_humidity(self) -> int:
        return self.humidity

    def get_pressure(self) -> int:
        return self.pressure

    def get_power(self) -> int:
        return self.power

    def get_power_consumption(self) -> int:
        return self.power_consumption

    @classmethod
    def get_Sensor_count(cls):  # 计数，用于获取传感器数量
        return cls.instances


sensor1 = Sensor()  # 创建对象
sensor2 = Sensor()
sensor3 = Sensor()
sensor4 = Sensor()


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
                    User.username = username
                    return True
    except Exception as e:
        print(f"An error occurred: {e}")
    return False


@app.route("/")
def home():
    sensor1.get_latest_data()
    sensor2.get_latest_data()
    sensor3.get_latest_data()
    sensor4.get_latest_data()
    return render_template(
        "index.html",
        device_number=Sensor.get_Sensor_count(),
        sensor1=sensor1,
        sensor2=sensor2,
        sensor3=sensor3,
        sensor4=sensor4,
    )


@app.route("/about")
def about():
    developer = ["高学骏", "付典雅", "李恺烨"]
    random.shuffle(developer)
    return render_template("about.html", developer=developer)


@app.route("/login", methods=["GET", "POST"])
def login():
    global is_login
    print(is_login)
    if is_login:
        return redirect(url_for("self"))
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if check_credentials(username, password):
            is_login = True
            return redirect(url_for("home"))
        else:
            return '登录失败，请重试！<a href="login">redo</a>'
    else:
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
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
def self():
    return render_template("self.html", User=User)


@app.route("/logout")
def logout():
    global is_login
    is_login = False
    User.username = ""
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
