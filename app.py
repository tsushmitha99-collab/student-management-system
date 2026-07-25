from flask import Flask, render_template, request
from students import students

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    name = request.form["name"]

    if name in students:
        student = students[name]
        return render_template("result.html", name=name, student=student)
    else:
        return "Student Not Found"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)