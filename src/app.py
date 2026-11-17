from flask import Flask, jsonify, request

app = Flask(__name__)

snippets = [
    {"id": 1, "lang": "bash", "title": "List hidden files", "code": "ls -la"},
    {"id": 2, "lang": "docker", "title": "Check running containers", "code": "docker ps -a"},
    {"id": 3, "lang": "git", "title": "Check repository status", "code": "git status"}
]

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "app": "DevSnippet-Vault",
        "version": "1.0",
        "routes": ["/snippets", "/snippets/<lang>", "/health"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/snippets', methods=['GET'])
def get_all_snippets():
    return jsonify({"count": len(snippets), "snippets": snippets})

@app.route('/snippets/<lang>', methods=['GET'])
def get_by_lang(lang):
    filtered = [s for s in snippets if s["lang"].lower() == lang.lower()]
    return jsonify({"lang": lang, "snippets": filtered})

@app.route('/snippets', methods=['POST'])
def create_snippet():
    data = request.get_json()
    if not data or not all(k in data for k in ("lang", "title", "code")):
        return jsonify({"error": "lang, title, and code are required"}), 400
    item = {
        "id": len(snippets) + 1,
        "lang": data["lang"],
        "title": data["title"],
        "code": data["code"]
    }
    snippets.append(item)
    return jsonify(item), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)