from src.langgraphagenicai.state.state import State


class ChatbotWithToolNode:
    """
    Chatbot to handle tool call
    """
    def __init__(self,model):
        self.llm=model
        
    #without any tools we can call this function
    def process(self,state:State)->dict:
        """
        Process the input state and generates a response with tool integration.
        """
        user_input= state["messages"][-1] if state["messages"] else ""
        llm_response=self.llm.invoke({"role":"user","content":user_input})
        
        tool_response=f"Tool integration for :'{user_input}'"
        
        return {"messages":[llm_response,tool_response]}
    
    
    #with tools -we can bind with tools and process the output
    def create_chatbot(self,tools):
        """
        Returns a Chatbotnode fucntion
        """
        llm_with_tools=self.llm.bind_tools(tools)
        
        def chatbot_node(state:State):
            """
            Chatbot logic for processing the input state and returning a response
            """
            return {"messages":[llm_with_tools.invoke(state["messages"])]}
        return chatbot_node