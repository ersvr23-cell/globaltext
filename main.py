from flask import Flask, request, jsonify

app = Flask(__name__)
latest_message = "Waiting for message..."

@app.route("/api/setMessage", methods=["POST"])
def set_message():
    global latest_message
    data = request.get_json()
    latest_message = data.get("message", latest_message)
    return jsonify({"ok": True})

@app.route("/api/getMessage", methods=["GET"])
def get_message():
    return jsonify({"message": latest_message})

if __name__ == "__main__":
    app.run()
