pip install Flask
# app.py
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve the homepage
@app.route("/")
def home():
    return render_template("index.html")

# API endpoint that receives data from frontend
@app.route("/api/message", methods=["POST"])
def message_api():
    data = request.get_json()
    user_msg = data.get("message", "")
    response_msg = f"Hello from server! You said: {user_msg}"
    return jsonify({"reply": response_msg})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
