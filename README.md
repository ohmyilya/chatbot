# Naive LLAMA Chatbot (Ollama + Streamlit)

A simple local chatbot app using [Ollama](https://ollama.com/) with the LLAMA model and a Streamlit UI.

## Requirements
- Python 3.8+
- Ollama running locally (default: http://localhost:11434, with `llama2` model pulled)
- pip (for Python dependencies)

## Setup
```bash
pip install -r requirements.txt
```

## Usage
1. Make sure Ollama is running and you have pulled the `llama2` model:
   ```bash
   ollama run llama2
   ```
2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```

Then open the provided local URL in your browser.
