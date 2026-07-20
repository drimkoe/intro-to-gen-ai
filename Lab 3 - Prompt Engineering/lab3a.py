# Lab 3a
# Test API

from openai import OpenAI

# Create client
client = OpenAI()

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a REST API is in one paragraph."
)

print(response.output_text)