from langgraph.graph import StateGraph

def chatbot(state):
    message = state["message"]
    print(state)
    if "bom dia" in message:
        return {"response": "bom dia"}
    elif "boa tarde" in message:
        return {"response": "boa tarde"}
    elif "boa noite" in message:
        return {"response": "boa noite"}
    elif "soma" in message:
        return {"response": message}
    return {"response": f"Você disse: {message}"}

def soma(state):
    content = state["response"]
    itens = content.split()
    print(itens[1] + itens[2])
    return itens[1] + itens[2]

# def condSoma(state):
#     content = state["response"]
#     if content in "soma":
#         return "soma"
#     else:
#         return "fim"

graph = StateGraph(dict)

graph.add_node("chatbot", chatbot)

graph.add_node("soma", soma)

# graph.add_node("condSoma", condSoma)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
    "chatbot",
    lambda state: state["response"],
    {
        "soma", "soma",
        "fim", "END"
    }

)

app = graph.compile()

result = app.invoke({
    "message": "soma 25 20"
})

print(result)