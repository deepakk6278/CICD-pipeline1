import os
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.get("/health")
def health():
    return jsonify(status="ok", service="frontend-cicd-project"), 200

@app.get("/api/student")
def student():
    return jsonify(
        name="Student",
        course="Cloud Computing and DevOps",
        project="CI/CD Pipeline Demonstration"
    ), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", "5000")))
