"""
Lab 3b - Exploring Temperature
This script introduces the 'temperature' parameter.
"""
from openai import OpenAI

client = OpenAI()

prompt= "Write a surreal dream-like paragraph about a city made of glass."

# The 'temperature' parameter controls the randomness of the model's output.
# - A temperature of 0.0 makes the output highly deterministic and focused (good for code or facts).
# - Higher values (e.g., 0.8 to 1.5) make the output more creative, random, and diverse.
# - Warning: Very high temperatures (close to 2.0) can produce gibberish!
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    temperature=0
)

print(response.output_text)