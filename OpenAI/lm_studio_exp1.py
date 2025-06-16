
import requests
import json

# --- Configuration ---

#GET http://localhost:1234/v1/models
#POST http://localhost:1234/v1/chat/completions
#POST http://localhost:1234/v1/completions
#POST http://localhost:1234/v1/embeddings

'''
POST http://localhost:1234/v1/chat/completions
Purpose: Designed specifically for conversational or chat-based interactions. It's the modern and 
preferred endpoint for models fine-tuned for instruction following and dialogue (like Llama-2-Chat, 
Mistral-Instruct, GPT-3.5-Turbo, GPT-4, etc.).

Input Format: Expects a structured messages array. Each item in the array is an object with a 
role (system, user, or assistant) and content (the text). This allows you to provide context, 
history, and system-level instructions.

Use Case: Building chatbots, multi-turn dialogues, question-answering with history, role-playing, 
following complex instructions given via a system prompt.
'''

'''
http://localhost:1234/v1/completions

Purpose: Designed for more general-purpose text completion. It takes a single prompt and tries to continue 
it. This was the primary endpoint for older OpenAI models (like text-davinci-003).

Input Format: Expects a simple prompt string (or an array of strings for batch processing, though less 
common for chat).

{
  "model": "local-model",
  "prompt": "The capital of France is",
  "max_tokens": 10,
  "temperature": 0.7
}

Use Case: Simple text generation, continuing a story or sentence, code completion 
(though chat often works better now), summarization (by prompting "Summarize this: ..."), 
translation (by prompting "Translate to French: ..."). It doesn't inherently understand 
conversational turns or roles.
'''


LMSTUDIO_API_BASE_URL = "http://localhost:1234/v1"  # Default URL for LM Studio
ENDPOINT = "/chat/completions"
API_URL = f"{LMSTUDIO_API_BASE_URL}{ENDPOINT}"

# --- Your Prompt ---
user_prompt = "Explain the concept of Large Language Models (LLMs) in simple terms."

# --- Request Payload (OpenAI compatible format) ---
payload = {
    "model": "local-model",  # Model name doesn't matter much for LM Studio local server if only one model is loaded
    "messages": [
        {"role": "system", "content": "You are a helpful AI assistant."},
        {"role": "user", "content": user_prompt}
    ],
    "temperature": 0.7,     # Controls randomness (optional, default is often 0.7)
    "max_tokens": 500,      # Max words/tokens in the response (optional)
    "stream": False         # Set to False for a single complete response (True for streaming)
}

# --- Headers ---
headers = {
    "Content-Type": "application/json"
}

# --- Send the Request ---
try:
    print(f"Sending request to: {API_URL}")
    print(f"Payload:\n{json.dumps(payload, indent=2)}") # Print payload for debugging

    response = requests.post(API_URL, headers=headers, json=payload)

    # Raise an exception for bad status codes (4xx or 5xx)
    response.raise_for_status()

    # --- Process the Response ---
    response_data = response.json()
    # print(f"\nFull Response:\n{json.dumps(response_data, indent=2)}") # Uncomment to see the full structure

    # Extract the content from the response
    if "choices" in response_data and len(response_data["choices"]) > 0:
        assistant_message = response_data["choices"][0]["message"]["content"]
        print("\n--- LLM Response ---")
        print(assistant_message.strip()) # .strip() removes leading/trailing whitespace
    else:
        print("\nError: Could not find 'choices' in the response or it was empty.")
        print(f"Full Response:\n{json.dumps(response_data, indent=2)}")

except requests.exceptions.RequestException as e:
    print(f"\nAn error occurred sending the request: {e}")
    print("Please ensure:")
    print("1. LM Studio is running.")
    print(f"2. The local server is started (usually on port 1234).")
    print(f"3. The URL '{API_URL}' is correct.")
    print("4. No firewall is blocking the connection on localhost.")

except json.JSONDecodeError:
    print("\nError: Could not decode the JSON response from the server.")
    print(f"Raw Response Text: {response.text}")

except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")