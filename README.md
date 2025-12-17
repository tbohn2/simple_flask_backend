# simple_flask_backend
Simple backend to explore Flask

## Project Structure

```
app/
├── __init__.py        # Flask app factory, register blueprints
├── routes/            # Endpoints / controllers
│   ├── __init__.py
│   └── user_routes.py
├── services/          # Business logic / services
│   ├── __init__.py
│   └── user_service.py
├── models/            # Database models
│   ├── __init__.py
│   └── user.py
├── utils/             # Helpers, utilities
│   └── helpers.py
├── templates/         # HTML templates
└── static/            # CSS, JS, images
config.py              # Configuration settings
requirements.txt
run.py                 # Application entry point
```

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

The server will start on `http://localhost:5000`

## API Endpoints

### Users
- `GET /api/users/` - Get all users
- `GET /api/users/<id>` - Get user by ID
- `POST /api/users/` - Create a new user
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com"
  }
  ```
