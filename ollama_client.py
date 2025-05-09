import requests

OLLAMA_API_URL = "http://localhost:11434/api/generate"


def query_ollama(prompt, model="llama2"):
    """
    Sends a prompt to the local Ollama server and returns the response.
    """
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_API_URL, json=payload, timeout=60)
        response.raise_for_status()
        data = response.json()
        return data.get("response", "[No response]")
    except Exception as e:
        return f"[Error communicating with Ollama: {e}]"
