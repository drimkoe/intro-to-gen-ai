from openai import OpenAI

# Create client
client = OpenAI()

prompt= "Write a surreal dream-like paragraph about a city made of glass."

response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    temperature=0
)

print(response.output_text)