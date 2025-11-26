from flask import Flask, request, jsonify
import sys
from io import StringIO

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({
        "service": "Python Executor",
        "version": "1.0",
        "endpoints": {
            "/execute": "POST - Execute Python code",
            "/info": "GET - Python environment info"
        }
    })

@app.route('/execute', methods=['POST'])
def execute():
    """Execute Python code and return output."""
    data = request.get_json()
    code = data.get('code', '')

    old_stdout = sys.stdout
    old_stderr = sys.stderr
    sys.stdout = StringIO()
    sys.stderr = StringIO()

    try:
        exec_globals = {"__builtins__": __builtins__}
        exec(code, exec_globals)

        output = sys.stdout.getvalue()
        error = sys.stderr.getvalue()

        return jsonify({
            "success": True,
            "output": output,
            "error": error if error else None
        })
    except Exception as e:
        return jsonify({
            "success": False,
            "output": sys.stdout.getvalue(),
            "error": str(e)
        })
    finally:
        sys.stdout = old_stdout
        sys.stderr = old_stderr

@app.route('/info')
def info():
    import platform
    return jsonify({
        "python_version": platform.python_version(),
        "platform": platform.platform()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
