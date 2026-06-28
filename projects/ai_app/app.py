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