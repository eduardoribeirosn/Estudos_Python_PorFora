from langgraph.graph import StateGraph, END
from typing import TypedDict

class State(TypedDict):
    message: str
    response: str
    resultSoma: int

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
        return {"response": "soma"}
    elif "subtrair" in message:
        return {"response": "sub"}
    return {"response": "fim"}

def soma(state):
    content = state["message"]
    itens = content.split()

    a = int(itens[1])
    b = int(itens[2])

    resultado = a + b
    print(resultado)
    return {"resultSoma": resultado}

def subtrair(state):
    content = state["message"]
    itens = content.split()

    a = int(itens[1])
    b = int(itens[2])

    resultado = a - b
    print(resultado)
    return {"resultSub": resultado}

graph = StateGraph(State)

graph.add_node("chatbot", chatbot)
graph.add_node("soma", soma)
graph.add_node("sub", subtrair)

# graph.add_node("condSoma", condSoma)

graph.set_entry_point("chatbot")

graph.add_conditional_edges(
    "chatbot",
    lambda state: state["response"],
    {
        "soma": "soma",
        "sub": "sub",
        "fim": END
    }
)

graph.add_edge("soma", END)

app = graph.compile()

result = app.invoke({
    "message": "subtrair 10 3"
})

print(result)