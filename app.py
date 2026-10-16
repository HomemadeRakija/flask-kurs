from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(
        "index.html",
        navn = "yoi",
        alder = "18",
        favorittspråk="kroatisk", 
        skole="kuben",
        poeng=50
        )


@app.route("/fag")
def indez():
    fagliste = ["python", "flask", "html", "css"]
    return render_template("fag.html", fag=fagliste)

@app.route("/om")
def om():
    return render_template("om.html")

@app.route("/prosjekter")
def indev():
    return "prosjekter"

@app.route("/kontakt")
def indec():
    return "kontakter"




@app.route("/regi", methods=["GET", "POST"])
def registrering():
    if request.method == "POST":
        navn = request.form["navn"]
        return f"hei {navn}"

    return render_template("regi.html")

if __name__=="__main__":
    app.run(debug = True)