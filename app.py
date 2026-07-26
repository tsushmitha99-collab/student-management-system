from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/save", methods=["POST"])
def save():
    name = request.form["name"]
    roll = request.form["roll"]
    marks = int(request.form["marks"])
    email = request.form["email"]
    phone = request.form["phone"]

    with open("students.txt", "a") as file:
        file.write(f"{name},{roll},{marks},{email},{phone}\n")

    return "Student Added Successfully! <br><br><a href='/'>Home</a>"


@app.route("/search")
def search_page():
    return render_template("search.html")


@app.route("/search", methods=["POST"])
def search_student():
    name = request.form["name"]

    with open("students.txt", "r") as file:
        for line in file:
            s = line.strip().split(",")

            if s[0].lower() == name.lower():

                if int(s[2]) >= 40:
                    result = "PASS"
                else:
                    result = "FAIL"

                return render_template(
                    "result.html",
                    student=s,
                    result=result
                )

    return "Student Not Found! <br><br><a href='/'>Home</a>"


if __name__ == "__main__":
    app.run(debug=True)
