
import os
from openai import OpenAI
from dotenv import load_dotenv,find_dotenv,dotenv_values

env = find_dotenv()
env_details = load_dotenv()

api_key = os.getenv('API_KEY')

# The OpenAI client automatically looks for the OPENAI_API_KEY environment variable.
# If you haven't set it, you can uncomment and use the line below,
# but it's less secure.
client = OpenAI(api_key=api_key)
try:
    #client = OpenAI() # Attempts to read OPENAI_API_KEY from environment

    print("Sending request to OpenAI...")

    # Make the API call to the Chat Completions endpoint
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",  # Or use "gpt-4" if you have access
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me a short, fun fact about the ocean."}
        ]
        top_p=0.9,
        temperature=0.8,      # Make it a bit more creative
        max_tokens=60,        # Limit the response length
        n=2,                  # Get two different options
        stop=["\n"]           # Stop generation at the first 
        frequency_penalty=0.0, # Default
        presence_penalty=0.0   # Default
    )
    # In short: n=2 asks the AI to give you two different answers/variations for the same request in one go.
    
    '''
    Cost Implication: Be aware that using n=2 (or any n > 1) means you will be billed for the prompt 
    tokens plus the tokens generated for all n completions. So, n=2 approximately doubles the generation 
    cost compared to n=1.
    '''
    
    # Extract and print the response content
    response_message = completion.choices[0].message.content
    print("\nOpenAI Response:")
    print(response_message)

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please ensure your OPENAI_API_KEY environment variable is set correctly.")
    print("You can get a key from https://platform.openai.com/api-keys")