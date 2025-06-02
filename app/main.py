from flask import Flask, jsonify
import os
from datetime import datetime

app = Flask(__name__)

def test(str):
    print("Changes")
    
@app.route('/')
def hello():
    return jsonify({
        "message": "Hello World",
        "version": "1.0.0",
        "environment": os.getenv("ENV", "development"),
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy",
        "service": "myapp",
        "timestamp": datetime.now().isoformat()
    })

@app.route('/info')
def info():
    return jsonify({
        "app": "MyPythonApp",
        "version": "1.0.0",
        "python_version": "3.11",
        "commit": os.getenv("GIT_COMMIT", "unknown")
    })

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=False)