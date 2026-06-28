import anthropic
import os

print("Скрипт запустился")
print("Ключ есть:", bool(os.environ.get("ANTHROPIC_API_KEY")))

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

print("Отправляю запрос...")

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Привет! Кто ты?"}
    ]
)

print(message.content[0].text)

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

    import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Привет! Кто ты?"}
    ]
)

print(message.content[0].text)