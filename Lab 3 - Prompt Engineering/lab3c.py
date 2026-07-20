from openai import OpenAI

# Create client
client = OpenAI()

prompt = "Invent a completely new programming language and describe its philosophy."
for temp in [0.0, 0.5, 1.0, 1.5]:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        temperature=temp,
        max_output_tokens=200
    )
    print(f"\n--- Temperature: {temp} ---")
    print(response.output_text)
