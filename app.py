from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
boostrap = Bootstrap5(app)

@app.route('/')
def index():
    classmates = [
        ("Alex", "LOL", "Laughing Out Loud"),
        ("Sam", "BRB", "Be Right Back"),
        ("Jordan", "FYI", "For Your Information"),
    ]

    paragraphs = "".join(
        f"<p>{name}: {acronym} ({meaning})</p>"
        for name, acronym, meaning in classmates
    )
    return f"<h1>Classmate Acronyms</h1>{paragraphs}"

@app.route('/von')
def my_page():
    return render_template("template.html", first_name="Von", acronym="IMO (In My Opinion)")

@app.route('/bootstrap')
def bootstrap_page():
    return render_template("image.html")