# Simple API

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
uvicorn main:app --host 0.0.0.0 --port $PORT
```

## Routes

- `/` - Hello World
- `/users` - List of users
- `/users/{user_id}` - User detail
