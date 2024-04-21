from flask import Flask

app = Flask(__name__)

@app.route("/patients")
def patients():
    return {"patients": ["patient1", "patient2", "patient3"]}

if __name__ == "__main__":
    app.run(debug=True)