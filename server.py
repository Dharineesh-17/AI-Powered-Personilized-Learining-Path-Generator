from flask import Flask, render_template, request, jsonify
from main import generate_path

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# This MUST be named /generate to match your JavaScript fetch call
@app.route('/generate')
def get_path():
    topic = request.args.get('topic', '')
    if not topic:
        return jsonify({"error": "Please enter a topic!"})
    
    # This calls your AI logic in main.py
    data = generate_path(topic) 
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)