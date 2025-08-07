import streamlit as st
import os
    
from src.langgraphagenicai.ui.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config=Config()
        self.user_controls={}
        
    def load_streamlit_ui(self):
        st.set_page_config(page_title=self.config.get_page_title(),layout="wide")
        st.header(self.config.get_page_title())
        #using session_state varibles inittialize it 
        st.session_state.timeframe=''
        st.session_state.IsFetchButtonClicked=False
        
        with st.sidebar:
        #Getting the options from config
            llm_options=self.config.get_llm_options()
            usecase_options=self.config.get_usecase_options()

            #Selecting LLM
            self.user_controls["selected_llm"]=st.selectbox("Select LLM",llm_options)
            
            if self.user_controls["selected_llm"]=="Groq":
                groq_models_options=self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"]=st.selectbox("Select Model",groq_models_options)
                self.user_controls["GROQ_API_KEY"]= st.session_state["GROQ_API_KEY"]=st.text_input("API KEY",type="password")               
                
                #validating API key
                if not self.user_controls['GROQ_API_KEY']:
                    st.warning("Please enter your Groq API Key to proceed,Don't have? refer : https://console.groq.com/home")
                
                
            #usecase selection
            self.user_controls["selected_usecase"]=st.selectbox("Select Usecase",usecase_options)

            if self.user_controls["selected_usecase"]=="Chatbot With Web":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("Tavily API Key",type="password")
                if not self.user_controls['TAVILY_API_KEY']:
                    st.warning("Please enter you Tavily Api key to proceed, Don't have? refer : https://app.tavily.com/playground ")
            
            #Ai News usecase
            if self.user_controls["selected_usecase"]=="AI News":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"]=st.session_state["TAVILY_API_KEY"]=st.text_input("Tavily API Key",type="password")
                if self.user_controls["TAVILY_API_KEY"]:
                    st.subheader("AI News Explorer")
                    time_frame=st.selectbox(label="Select Time Frame",options=["Daily","Weekly","Monthly"],index=0)
                    if st.button("Fetch latest AI News",use_container_width=True):
                        st.session_state.IsFetchButtonClicked = True
                        st.session_state.timeframe=time_frame
                else:
                    st.warning("Please enter you Tavily Api key to proceed, Don't have? refer : https://app.tavily.com/playground ")
                
        return self.user_controls