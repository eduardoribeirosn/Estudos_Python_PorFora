from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "API funcionando"}

@app.route("/users")
def users():
    return {"users": ["João", "Maria"]}

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json

    text = data["text"]

    return {"result": f"Você enviou: {text}"}

if __name__ == "__main__":
    app.run(debug=True)