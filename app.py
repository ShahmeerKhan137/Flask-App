from flask import Flask

# This is the Flask application object
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! First Flaskk app, first change, MANZOOR BHAI"

# Only run when executed directly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)