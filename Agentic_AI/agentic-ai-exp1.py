from langchain.agents import AgentType, initialize_agent
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from langchain.tools import DuckDuckGoSearchRun

#Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_0.gguf

llm = CTransformers(
    #model="TheBloke/Llama-2-7B-Chat-GGML",  # Replace with your model path or HF Hub ID
    #model="./models/TheBloke/Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_0.gguf",
    model="C:/Users/PenikalS/.cache/lm-studio/models/TheBloke/Llama-2-7B-Chat-GGUF/llama-2-7b-chat.Q4_0.gguf", 
    model_type="llama",
    config={'max_new_tokens': 256, 'temperature': 0.1}
)

# 2. Define Tools (Crucial for agent's abilities)
search = DuckDuckGoSearchRun()  # Use DuckDuckGo search (no API key required)

# 3. Initialize the Agent
tools = [search]

# Create a custom prompt
prompt_template = PromptTemplate.from_template("""
You are a helpful assistant designed to answer questions using tools.

You have access to the following tools:

{tool_names}

To answer the question, follow these steps:

1.  Think step-by-step about how to best answer the question.
2.  If you need to use a tool, you MUST use the following format:

    ```
    Thought: I need to use a tool to help me answer the question.
    Action: the name of the tool to use (one of {tool_names})
    Action Input: the input to the tool
    ```

3.  If you already know the answer, you MUST use the following format:

    ```
    Thought: I can answer the question without using any tools.
    Final Answer: the answer to the question
    ```

Begin!

Question: {input}
""")

# Format the prompt with the tool names
tool_names = ", ".join([tool.name for tool in tools])
# formatted_prompt = prompt_template.format(
#     tool_names=", ".join([tool.name for tool in tools]),
#     input="{input}"
# )
print('****************************'*3)
print('tool_names :', tool_names)
print('****************************'*3)
input = "What is the capital city of Karnataka?"
agent_kwargs = {
    'system_message': prompt_template.format(tool_names=tool_names, input="{input}"), #Format the entire string here.

}
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    agent_kwargs=agent_kwargs,
    handle_parsing_errors=True #Enable handling of parsing errors
)
# who won the cricket icc men's champions trophy 2025?
response = agent.run("What is the capital city of Karnataka?")
print(response)