# Simple Chat

---

The Simple Chat project is an API server developer using Django REST Framework. This API allows you to create your own threads, where you can chat with other users.
## Installation

---
To install and run the project on your local computer, follow these steps:

```shell
  git clone https://github.com/KristianYe/simple_chat.git
  cd simple_chat
  python -m venv venv
  source venv/bin/activate  # On Linux/Mac
  venv\Scripts\activate  # On Windows
  pip install -r requirements.txt
  python manage.py makemigrations
  python manage.py migrate
  python manage.py loaddata data.json # to load test data
  python manage.py runserver
```

After completing these steps, the API will be available at http://localhost:8000/

## Usage

---
#### The API provides the following endpoints:

- `api/chat/threads`: List of all threads of authenticated user
- `api/chat/threads/create`: Create your own Thread
- `api/chat/threads/{thread_id}`: Receive information about specific thread
- `api/chat/threads/{thread_id}/messages`: List of all messages in specified thread
- `api/chat/threads/{thread_id}/messages/read`: Mark messages as read in specified thread
- `api/chat/unread-messages-count`: Get number of unread messages
- `api/user/register`: Register new user
- `api/user/token`: Get Access Token for using chat api
- `api/user/token/refresh`: Refresh Access Token via Refresh Token


## Data for authentication

---
You can create your own profile via `/api/user/register/` or use next credentials:
```
Login: user1
Password: 12345
```
