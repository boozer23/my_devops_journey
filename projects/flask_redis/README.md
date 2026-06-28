# Flask + Redis Visit Counter 🐳

A multi-container web application built with Docker Compose.
Tracks page visits using Redis as a persistent data store.

## 🏗️ Architecture
Browser → Flask (port 5001) → Redis (port 6379)

## 🛠️ Tech Stack

- **Python / Flask** — web server
- **Redis** — in-memory data store
- **Docker Compose** — container orchestration
- **Docker Volumes** — persistent data storage

## 🚀 Quick Start

```bash
git clone https://github.com/boozer23/my_devops_journey.git
cd my_devops_journey/projects/flask_redis
docker compose up --build
```

Open http://localhost:5001

## 📁 Project Structure
flask_redis/

├── app.py              # Flask application

├── requirements.txt    # Python dependencies

├── Dockerfile          # Container build instructions

└── docker-compose.yml  # Multi-container orchestration

## 💡 What I learned

- Docker Compose for multi-container apps
- Container networking (services communicate by name)
- Persistent storage with Docker Volumes
- Environment separation between services