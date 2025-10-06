
# MyOwnAPI

## Overview
This project is a simple Flask-based API with a minimal frontend. It allows you to create, update, delete, list, and search posts by title and content.

## Structure
- `backend/` — Flask backend (`backend_app.py`)
- `frontend/` — Frontend app and static files

## Setup
1. Install Python 3.10+ and create a virtual environment:
	```sh
	python -m venv .venv
	source .venv/bin/activate
	pip install flask flask-cors
	```
2. Start the backend:
	```sh
	python backend/backend_app.py
	```
3. (Optional) Start the frontend if available.

## API Endpoints

### List Posts
`GET /api/posts`

### Add Post
`POST /api/posts`
Body (JSON): `{ "title": "...", "content": "..." }`

### Update Post
`PUT /api/posts/<id>`
Body (JSON): `{ "title": "...", "content": "..." }`

### Delete Post
`DELETE /api/posts/<id>`

### Search Posts
`GET /api/posts/search?title=foo&content=bar`
Searches for posts where the title contains `foo` and the content contains `bar` (case-insensitive). You can use only one parameter as well.

## Example
```sh
curl 'http://localhost:5002/api/posts/search?title=first'
```

## License
MIT
