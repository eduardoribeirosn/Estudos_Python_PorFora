# Todo - API
from flask import Flask, request

app = Flask(__name__)

tasks = []

@app.route("/tasks")
def get_tasks():
    textTasks = ""
    for task in tasks:
        textTasks += (f""
                      f"Task: {task['id']}\n    -    "
                      f"Title: {task['title']}\n    -    "
                      f"done: {task['done']}\n\n    -    ")
    return {"message": f"Tasks:\n\n{textTasks}"}

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.json
    titleTask = data["task"]

    newTask = {
        "id": len(tasks) + 1,
        "title": titleTask,
        "done": False
    }

    tasks.append(newTask)

    return {"message": "Task criada"}

@app.route("/tasks/<int:id>", methods=["PUT"])
def att_task(id):
    for taskAtual in tasks:
        if taskAtual["id"] == id:
            if taskAtual["done"]:
                taskAtual["done"] = False
            else:
                taskAtual["done"] = True
            return {"message": f"Task com id {id} alterada para {taskAtual['done']}"}
    return {"message": f"Task com id {id} não encontrado"}

@app.route("/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    for taskAtual in tasks:
        if(taskAtual["id"] == id):
            tasks.remove(taskAtual)
            return {"message": f"Task com id {id} deletada."}
    return {"message": f"Task com id {id} não encontrada"}

if (__name__ == "__main__"):
    app.run(debug=True)