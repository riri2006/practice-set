from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

class State(BaseModel):
    question:str
    answer:str=""

llm=ChatGroq(model="openai/gpt-oss-20b")

def ai(State):
    response= llm.invoke(f"Answer as an ai chatbot but in easy language for question: {State.question}")
    return{"answer":response.content}

graph=StateGraph(State)

graph.add_node("Node1",ai)

graph.add_edge(START,"Node1")
graph.add_edge("Node1",END)

practice=graph.compile()


result= practice.invoke({"question":"what is python"})
print("AI: ",result["answer"] )
