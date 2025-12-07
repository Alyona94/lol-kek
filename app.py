from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Buy milk", "done": False},
    {"id": 2, "title": "Learn Flask", "done": False}
]

@app.get("/")
def serve_frontend():
    return send_from_directory('.', 'index.html')

@app.get('/tasks')
def get_tasks():
    return jsonify(tasks), 200


if __name__ == "__main__":
    app.run(debug=True)
