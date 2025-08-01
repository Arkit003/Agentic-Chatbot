from pydantic import BaseModel,Field
from typing_extensions import TypedDict
from langgraph.graph.message import add_messages
from typing import Annotated

class State(TypedDict):
    """
    Represent the state used in the graph.
    """
    messages:Annotated[list,add_messages]