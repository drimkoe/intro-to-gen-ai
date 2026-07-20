"""
Lab 3c - Iterating Temperature and Max Tokens
This script shows how changing temperature affects the same prompt,
and introduces the 'max_output_tokens' parameter to cap the response length.
"""
from openai import OpenAI

client = OpenAI()

prompt = "Invent a completely new programming language and describe its philosophy."
# We iterate through different temperature values to see how the response changes.
for temp in [0.0, 0.5, 1.0, 1.5]:
    # max_output_tokens sets a hard limit on how many tokens the model can generate.
    # This is very useful for controlling costs and ensuring responses fit into a UI.
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=temp,
        max_output_tokens=200
    )
    print(f"\n--- Temperature: {temp} ---")
    print(response.output_text)
