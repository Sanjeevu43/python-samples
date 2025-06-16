from openai import OpenAI
from dotenv import find_dotenv,load_dotenv
import os

env = find_dotenv()
env_details = load_dotenv()
api_key= os.getenv("API_KEY")

client = OpenAI(api_key=api_key)

completion = client.chat.completion.create(
    model="gpt-turbo4",
    messages = [
        {"role":"System","content":"You are a helpfull assistant"},
        {"role":"User","content":"Tell me a short, fun fact about the ocean."}
    ],
    temparature=0.1,
    max_tokens=100,
    stop=[],

)

res = completion.choices[0].message.content