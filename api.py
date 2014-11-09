from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def home():
    return "This is home!"

@app.route("/upload", methods=['POST'])
def upload():
    return "uploaded"

@app.route("/upload/<project_id>", methods=['POST'])
def update_project(project_id):
    return "uploaded"


if __name__ == "__main__":
    app.run(debug=True)
