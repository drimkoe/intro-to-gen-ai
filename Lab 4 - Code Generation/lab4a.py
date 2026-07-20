"""
Lab 4a - Unstructured Prompts
This script demonstrates that a vague prompt often produces weak code.
Without specific instructions, the LLM will guess your intent and use defaults,
which may lack error handling, security, or standard styling.
"""
from openai import OpenAI

# Create client
client = OpenAI()

# Notice how this prompt is very brief. We didn't specify a framework version,
# routing details, or error handling.
prompt="Write a simple Python Flask hello world application."
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)