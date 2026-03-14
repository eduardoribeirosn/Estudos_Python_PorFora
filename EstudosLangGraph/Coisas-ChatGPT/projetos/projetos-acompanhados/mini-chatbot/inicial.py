from langgraph.graph import StateGraph

def chatbot(state):
    message = state["message"]
    return {"response": f"Você disse: {message}"}

graph = StateGraph(dict)

graph.add_node("chatbot", chatbot)

graph.set_entry_point("chatbot")

app = graph.compile()

result = app.invoke({
    "message": "Olá"
})

print(result)