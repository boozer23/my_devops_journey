from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host="redis", port=6379)

@app.route("/")
def index():
    count = int(r.incr("hits"))
    return f"Страница открыта {count} раз(а)."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
