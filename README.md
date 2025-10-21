# Todo App

A beautiful, modern todo list application built with Flask.

## Features

- ✅ Add, edit, and delete todos
- ✅ Mark todos as completed/incomplete
- ✅ Filter todos (All, Active, Completed)
- ✅ Persistent storage (JSON file)
- ✅ REST API endpoints
- ✅ Responsive, modern UI design
- ✅ Mobile-friendly

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jitbiswas123/CI-CD.git
cd CI-CD
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to:
```
http://localhost:5000
```

## API Endpoints

### Get all todos
```bash
GET /api/todos
```

### Add a new todo
```bash
POST /api/todos
Content-Type: application/json

{
  "title": "Your todo title"
}
```

### Update a todo
```bash
PUT /api/todos/<id>
Content-Type: application/json

{
  "completed": true,
  "title": "Updated title"
}
```

### Delete a todo
```bash
DELETE /api/todos/<id>
```

## Project Structure

```
.
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main HTML template
├── static/
│   └── style.css      # CSS styles
└── todos.json         # Persistent storage (auto-generated)
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Storage**: JSON file-based persistence

## Development

The application runs in debug mode by default. Any changes to the code will automatically reload the server.

## CI/CD

This project includes a GitHub Actions workflow for continuous integration. The workflow:
- Installs Python dependencies
- Sets up the environment
- Can be extended with testing and linting

## License

MIT License
