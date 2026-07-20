

"""
Lab 4b - Clear Statement of the Programming Problem
This script improves upon the previous prompt by adding a clear, specific
statement of what we want the application to do.
"""
from openai import OpenAI

# Create client
client = OpenAI()

# By explicitly stating the Python version (3.11), the exact framework (Flask),
# and the precise endpoint routing ("/" and "Hello, World!"), we leave less
# room for the LLM to make incorrect assumptions.
prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!"."""

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)