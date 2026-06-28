from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Привет! Мой первый веб-сервер работает!"

@app.route("/about")
def about():
    return "Меня зовут Владимир. Я учусь DevOps."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)