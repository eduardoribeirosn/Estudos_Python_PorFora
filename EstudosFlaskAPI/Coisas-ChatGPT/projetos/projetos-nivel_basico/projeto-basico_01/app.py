from flask import Flask, request

app = Flask(__name__)

@app.route("/health")
def health():
    return {"message": "API está online!"}

listUsers = []

@app.route("/users", methods=["POST"])
def create_user():
    data = request.json
    text = data["text"]

    listUsers.append(text)

    return {"message": "Usuário cadastrado"}

@app.route("/users")
def get_user():
    return f"Users: {listUsers}"

if __name__ == "__main__":
    app.run(debug=True)