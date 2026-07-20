"""
Lab 3d - Top-p (Nucleus Sampling)
This script introduces 'top_p', another way to control response randomness.
"""
from openai import OpenAI

client = OpenAI()

prompt= "Write a surreal dream-like paragraph about a city made of glass."

# top_p (nucleus sampling) restricts the model's vocabulary choice.
# Instead of picking from all possible next words, it only picks from the most likely
# words whose combined probabilities add up to top_p (e.g., 0.3 means top 30% of probability mass).
# Note: It's generally recommended to alter EITHER temperature OR top_p, but not both heavily.
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt,
    temperature=0.8,
    top_p=0.3  # Try changing this to 1.0 to see the difference
)

print(response.output_text)