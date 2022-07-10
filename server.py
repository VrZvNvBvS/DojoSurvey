from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "Victorias's Secret"


@app.route("/", methods=['GET', 'POST'])
def survey():
    if request.method == 'POST':
        session['form'] = request.form
        return redirect("/results")
    else:
        return render_template("index.html")


@app.route("/results", methods=['GET'])
def results():
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)
