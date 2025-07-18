# 🗓️ Task Scheduler API

A RESTful API for creating, scheduling, and managing tasks with status transitions, sorting, and pagination. Built using Django and Django REST Framework.

---

## 🚀 Features

- ✅ Create, Read, Update, Delete (CRUD) tasks
- ⏰ Schedule tasks with datetime
- 🔄 Enforce valid status transitions (`pending → running → completed/failed`)
- 📊 Sort by `scheduled_time`, `created_at`, or `status`
- 📉 Limit and paginate results
- 🔐 Ready for Celery integration for async execution

---

## 🧱 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (default, can switch to PostgreSQL/MySQL)
- **Optional**: Celery + Redis for task execution

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/task-scheduler-api.git
cd task-scheduler-api
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
