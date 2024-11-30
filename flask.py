from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page where the user inputs their data
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        # Pass the name and age to the template to render a greeting
        return render_template("greeting.html", name=name, age=age)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
