from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/greet", methods=["GET", "POST"])
def index():
    name = ""
    message = ""

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            message = f"Hello, {name}! Welcome to your Flask app."
        else:
            message = "Please enter your name."

    return render_template("index.html", name=name, message=message)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)