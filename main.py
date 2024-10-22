from flask import Flask
from flask.templating import render_template

# Flaskのインスタンスを作成 --- (*1)
app = Flask(__name__)


# ルーティングの指定 --- (*2)
@app.route('/')
def index():
    username = "ケイジ"
    age = 19
    email = "keiji@example.com"
    return render_template("card.html",
                           username=username,
                           age=age,
                           email=email)


# 実行する --- (*3)
if __name__ == '__main__':
    app.run(host='0.0.0.0')
