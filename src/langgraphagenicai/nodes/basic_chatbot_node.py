from src.langgraphagenicai.state.state import State


class BasicChatbot:
    """
    Basic Chatbot logic implementation
    """
    def __init__(self,model):
        self.llm=model
        
    def process(self,state:State)->dict:
        """
        Process a input state and generates a chatbot response.
        """
        return {"messages":self.llm.invoke(state['messages'])}  