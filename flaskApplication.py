from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
  {
    "ranking": 1,
    "country": "Spain",
    "stadium": "Various (often La Cartuja)",
    "won": 460,
    "draw": 180,
    "lost": 138
  },
  {
    "ranking": 2,
    "country": "Argentina",
    "stadium": "Estadio Monumental",
    "won": 585,
    "draw": 263,
    "lost": 221
  },
  {
    "ranking": 3,
    "country": "France",
    "stadium": "Stade de France",
    "won": 471,
    "draw": 195,
    "lost": 265
  },
  {
    "ranking": 4,
    "country": "England",
    "stadium": "Wembley Stadium",
    "won": 621,
    "draw": 255,
    "lost": 200
  },
  {
    "ranking": 5,
    "country": "Brazil",
    "stadium": "Maracanã",
    "won": 664,
    "draw": 209,
    "lost": 161
  }
]

@app.route("/")
def index():
    return """
    <h1>Top 5 Ranked International Football Teams</h1>
    <p> Try these endpoints:</p>
    <ul>
        <li><a href="/hello">/hello</a></li>
        <li><a href="/data">/data</a></li>
        <li><a href="/data/1">/data/1</a></li>
        <li><a href="/data/2">/data/2</a></li>
        <li><a href="/data/3">/data/3</a></li>
        <li><a href="/data/4">/data/4</a></li>
        <li><a href="/data/5">/data/5</a></li>
    </ul>
    """


@app.route("/hello")
def hello():
    return jsonify({"hello":"world"})

@app.route("/data")
def data():
    return jsonify(DATA), 200

@app.route("/data/<int:ranking>")
def item(ranking):
    for i in DATA:
        if i["ranking"] == ranking:
            return jsonify(i), 200
    return jsonify({"error": "team not found"}), 404

if __name__=="__main__":
    app.run(debug=True)
