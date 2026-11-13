from pydantic import BaseModel
from langgraph.graph import StateGraph, START, END

class Statee(BaseModel):
    name : str

def Hie(Statee):
    print("Hello , ", Statee.name)

def Bie(Statee):
    print("Byee , ", Statee.name)

graph = StateGraph(Statee)

graph.add_node("Node1",Hie)
graph.add_node("Node2",Bie)

graph.add_edge(START,"Node1")
graph.add_edge("Node1","Node2")
graph.add_edge("Node2",END)


demo = graph.compile()
demo.invoke({"name":"Riddhi"})
