
from openai import OpenAI

# Create client
client = OpenAI()

prompt="Write a simple Python Flask hello world application."
# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)