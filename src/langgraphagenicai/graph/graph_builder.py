from langgraph.graph import StateGraph,START,END
from langgraph.prebuilt import tools_condition

from src.langgraphagenicai.state.state import State
from src.langgraphagenicai.nodes.basic_chatbot_node import BasicChatbot
from src.langgraphagenicai.tools.search_tool import get_tools,create_tool_node 
from src.langgraphagenicai.nodes.chatbot_with_tool_node import ChatbotWithToolNode
from src.langgraphagenicai.nodes.ai_news_node import AINewsNode

class GraphBuilder:
    def __init__(self,model):
        self.llm=model
        self.graph_builder=StateGraph(State)
        
    # Basic chatbot    
    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using Langraph.
        This method intitalizes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph.The chatbot node is set as both the entry 
        and exit point of the graph.
        """
        self.basic_chatbot_node=BasicChatbot(self.llm)
        
        self.graph_builder.add_node("chatbot",self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START,"chatbot") 
        self.graph_builder.add_edge("chatbot",END )
        
    #Chatbot with tools    
    def chatbot_with_tools_build_graph(self):
        """
        Builds an advance chatbot graphs with tool integrations.
        This method creates a chatbot graph that includes both a chatbot node
        and a tool node.It defines tools and initializes the chatbot 
        with the tools capablities,sets up contditional and direct edges
        bw nodes.The Chatbot node is set as the entry point . 
        """
        tools=get_tools()
        tool_node=create_tool_node(tools=tools)
        
        #defining the chatbot node
        node=ChatbotWithToolNode(model=self.llm)
        chatbot_node=node.create_chatbot(tools=tools)
        
        #adding the nodes
        self.graph_builder.add_node("chatbot",chatbot_node)
        self.graph_builder.add_node("tools",tool_node)
        
        #adding the edges
        self.graph_builder.add_edge(START,"chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools","chatbot")
        # self.graph_builder.add_edge("chatbot",END)#tool will automatically handle this condition

    #AI News
    def ai_news_builder_graph(self):
        """
        Builds an advance chatbot graph used for getting news.
        """
        # tools=get_tools()
        # tool_node=create_tool_node(tools=tools)
        
        #definining chatbot node
        ai_news_node=AINewsNode(self.llm)
        
        #adding nodes
        self.graph_builder.add_node("fetch_news",ai_news_node.fetch_news)
        self.graph_builder.add_node("summarizer",ai_news_node.summarize)
        self.graph_builder.add_node("save_result",ai_news_node.save_result)
        
        #adding the edges
        self.graph_builder.set_entry_point("fetch_news")
        self.graph_builder.add_edge("fetch_news","summarizer")       
        self.graph_builder.add_edge("summarizer","save_result")       
        self.graph_builder.add_edge("save_result",END)       
        
                
    def setup_graph(self,usecase:str):
        """
        Sets up the graph for the selected use case.
        """
        if usecase=="Basic Chatbot":
            self.basic_chatbot_build_graph()
                    
        if usecase=="Chatbot With Web":
            self.chatbot_with_tools_build_graph()
            
        if usecase=="AI News":
            self.ai_news_builder_graph()
            
            
        return self.graph_builder.compile()
            

    