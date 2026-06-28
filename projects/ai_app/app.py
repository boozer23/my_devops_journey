import anthropic
import os
import psutil
from flask import Flask, jsonify

app = Flask(__name__)
client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

def get_system_stats():
    return {
        "cpu": psutil.cpu_percent(interval=1),
        "memory": psutil.virtual_memory().percent,
        "disk": psutil.disk_usage("/").percent
    }

@app.route("/")
def home():
    return "DevOps Dashboard работает! Используй /stats или /analyze"

@app.route("/stats")
def stats():
    return jsonify(get_system_stats())

@app.route("/analyze")
def analyze():
    system_stats = get_system_stats()
    
    prompt = f"""
    Проанализируй состояние сервера:
    CPU: {system_stats['cpu']}%
    Память: {system_stats['memory']}%
    Диск: {system_stats['disk']}%
    
    Всё ли в порядке? Есть ли проблемы?
    Ответь коротко — 2-3 предложения.
    """
    
    message = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=256,
        messages=[{"role": "user", "content": prompt}]
    )
    
    return app.response_class(
    response=__import__('json').dumps({
        "stats": system_stats,
        "ai_analysis": message.content[0].text
    }, ensure_ascii=False),
    mimetype='application/json'
)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)