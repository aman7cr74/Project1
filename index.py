from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is my first Python web app tjhid aman from world war 2!"

@app.route("/health")
def health():
    return {"status": "UP"}

if __name__ == "__main__":
    app.run(debug=True)
