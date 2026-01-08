# Agentic-Chatbot

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![LangGraph](https://img.shields.io/badge/LangGraph-Agentic-green)
![Last Commit](https://img.shields.io/github/last-commit/Arkit003/Agentic-Chatbot)

A simple **agentic chatbot** built with **Streamlit** and **LangGraph** that lets you interact with and compare responses from different AI models/providers.  
This project provides an end-to-end chatbot interface where you can experiment with agent-like behavior and multiple LLMs.

---

## Features

- **Conversational chatbot UI** using Streamlit  
- **Multi-model support** — try different AI models/providers in one place  
- **Agentic behavior** — integrates reasoning logic and flexible prompts  
- Lightweight and customizable Python project

---

## Technologies Used

| Component | Purpose |
|---------|---------|
| **Python** | Core language |
| **Streamlit** | Web interface for the chatbot |
| **LangGraph** | Manages language model integrations and workflows |
| **OpenAI / Other LLMs** | Chatbot backend models |

---

## Project Structure

```text
Agentic-Chatbot/
├── AINews/             # Markdowns of Monthly and Weekly AI News
├── src/                # Source code containing agent logic and graph definitions
├── app.py              # Main Streamlit application entry point
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project configuration and dependencies
├── .gitignore          # Git ignore file
├── .python-version     # Specified Python version
└── README.md           # Project documentation
```


##  Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/Arkit003/Agentic-Chatbot.git
   cd Agentic-Chatbot
   ```

2.**Create and activate a virtual environment**
   ```bash 
      python3 -m venv venv
      source venv/bin/activate   # macOS / Linux
      .\venv\Scripts\activate    # Windows 
   ```

3.**Install dependencies** 
 ```bash
   pip install -r requirements.txt
   ```

## Running the app
```bash
   streamlit run app.py
```




