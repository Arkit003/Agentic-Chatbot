import streamlit as st 
import traceback

from src.langgraphagenicai.ui.streamlitui.loadui import LoadStreamlitUI
from src.langgraphagenicai.LLMS.groq_llm import GroqLLM
from src.langgraphagenicai.graph.graph_builder import GraphBuilder
from src.langgraphagenicai.ui.streamlitui.display_result import DisplayResult

def load_langgraph_agenticai_app():
    """
    Loads and runs the LangGraph AgenticAI application with Streamlit UI.
    This Function intiliazes the UI, handles user input,configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness.
    
    """
    ##Load UI
    ui=LoadStreamlitUI()
    user_input=ui.load_streamlit_ui()
    
    #catching the user input error
    
    if not user_input:
        st.error("ERROR: Failed to load user input from the UI.")
        return 
    
    # user_message = st.chat_input("Enter your message:")
    if st.session_state.IsFetchButtonClicked:
        user_message=st.session_state.timeframe
    else:
        user_message=st.chat_input("Enter Your message:")
    
    if user_message:
        try:
            #configuring the llm
            obj_llm_config=GroqLLM(user_input)
            model=obj_llm_config.get_llm_model()
            
            if not model:
                st.error("Error:LLM model could not be initialized")
                return 
            
            #initiliazing the usecase based on the selection
            usecase=user_input["selected_usecase"]
            if not usecase:
                st.error("Error:Usecase could be initialized")
                return
            
            graph_builder=GraphBuilder(model=model)
            try:
                graph=graph_builder.setup_graph(usecase=usecase)
                DisplayResult(usecase=usecase,graph=graph,user_message=user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error:Graph setup failed - {traceback.format_exc()}")
                return
            
            
            
        except Exception as e:
            st.error(f"Error:Graph setup failed - {traceback.format_exc()}")
            return 