import os
from flask import Flask

app = Flask(__name__)

MY_NAME = os.environ.get("MY_NAME", "Незнакомец")

@app.route("/")
def home():
    return f"Привет! Меня зовут {MY_NAME}"

@app.route("/about")
def about():
    return "Меня зовут Владимир. Я учусь DevOps."

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)