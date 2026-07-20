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

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.2
)

print(response.choices[0].message.content)
