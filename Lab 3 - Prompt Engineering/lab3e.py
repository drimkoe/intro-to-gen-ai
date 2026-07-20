"""
Lab 3e - Structured Output Constraints
This script demonstrates how to force the LLM to return output in a specific
format (like JSON) by explicitly detailing the required schema in the prompt.
"""
from openai import OpenAI
import json

client = OpenAI()

prompt = """

"List all Canadian provinces and their current population."
Return a JSON object with this structure:

{
  "provinces": [
    {
      "name": "string",
      "population": integer
    }
  ]
}

Constraints:
- population must be a numeric integer
- no additional fields
- only valid JSON output
- no explanations
"""

# Notice how we use the chat.completions.create endpoint here (the standard chat API)
# and we pass the prompt as a message array.
# By setting a low temperature (0.2), we ensure the model focuses strictly on following
# our JSON schema rules rather than getting creative and breaking the format.
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

print(response.choices[0].message.content)
