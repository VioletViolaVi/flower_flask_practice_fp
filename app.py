# "bash -c \"export FLASK_DEBUG=true && flask run\"" (in place of "flask run" for pipfile if you want)
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/flowers", methods=["GET"])
def flowers():

    flowers = [
        {'id': 1, 'name': 'rose', 'colour': 'white', 'water': True},
        {'id': 2, 'name': 'orchid', 'colour': 'purple', 'water': False},
        {'id': 3, 'name': 'tulip', 'colour': 'red', 'water': True},
        {'id': 4, 'name': 'cactus', 'colour': 'green', 'water': False},
        {'id': 5, 'name': 'bluebell', 'colour': 'blue', 'water': True},
        {'id': 6, 'name': 'sunflower', 'colour': 'yellow', 'water': True},
        {'id': 7, 'name': 'marigold', 'colour': 'gold', 'water': True}
    ]

    return render_template("flowers.html", page_title="Flower-list", flowers=flowers)


@app.route("/flower/new", methods=["GET", "POST"])
def new_flower():
    if request.method == "GET":
        return "This route only works for POST request"
    else:
        data = request.get_json()
        if data["colour"] != "there was nothing there":
            return "That's a good flower"
        else:
            return "Nah...", 400


# IMPORTANT TO KNOW!!! ;)
# the "pragma: no cover" means it will auto be 100% test coverage as you should not test this thing
if __name__ == "__main__":
    app.run(debug=True)  # pragma: no cover
