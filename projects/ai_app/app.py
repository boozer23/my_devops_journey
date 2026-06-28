import anthropic
import os
from flask import Flask, request

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

@app.route("/")
def home():
    return "AI чат работает! Используй /ask?q=твой вопрос"

@app.route("/ask")
def ask():
    question = request.args.get("q", "Привет!")
    
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        messages=[
            {"role": "user", "content": question}
        ]
    )
    
    return message.content[0].text

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)