from langchain_groq import ChatGroq
from langgraph.graph import StateGraph,START,END
from pydantic import BaseModel
from dotenv import load_dotenv
load_dotenv()

class State(BaseModel):
    query:str
    route:str=""
    answer:str=""


llm=ChatGroq(model="openai/gpt-oss-20b")

def Router(State):
    route=llm.invoke(f"READ Question {State.query} and classify in these two classes only and answer only in single word coding or general: If question is related to coding then- Coding otherwise General" )
    return{"route":route.content}

def Llm(State):
    response=llm.invoke(f"Answer as coding expert and give only theoretical answers but in easily understandable way for question:{State.query} ")
    return{"answer":response.content}


def General(State):
    re=llm.invoke(f"Answer as general purpose ai and give answers accordingly for question:{State.query}")
    return{"answer":re.content }

def Decide(State):
    return State.route

graph=StateGraph(State)

graph.add_node("Router",Router)
graph.add_node("LLM",Llm)
graph.add_node("General",General)

graph.add_edge(START,"Router")
graph.add_conditional_edges(
    "Router",
    Decide,
    {
        "Coding":"LLM",
        "General":"General"
    }
)

graph.add_edge("LLM", END)
graph.add_edge("General",END)

app = graph.compile()

User_question = input("Ask: ")
response = app.invoke({"query":User_question})
print("Assistant: ", response["answer"])