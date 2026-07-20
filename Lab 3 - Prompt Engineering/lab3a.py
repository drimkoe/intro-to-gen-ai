"""
Lab 3a - Basic API Interaction
This script demonstrates the simplest way to interact with the OpenAI API.
"""
from openai import OpenAI

# The OpenAI() client automatically looks for the OPENAI_API_KEY environment variable.
# It acts as our main gateway to interact with the models.
client = OpenAI()

# We send our prompt to the model and wait for a response.
# Here we use 'gpt-4.1-mini' (or another available model) and provide a simple instruction.
response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a REST API is in one paragraph."
)

print(response.output_text)