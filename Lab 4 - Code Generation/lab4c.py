

"""
Lab 4c - Error Handling Requirements
This script demonstrates how to ensure the generated code is robust by
explicitly instructing the LLM to include error handling.
"""
from openai import OpenAI

# Create client
client = OpenAI()

# Here we add an explicit bulleted list of error handling requirements.
# LLMs respond very well to bulleted lists for requirements. 
# This ensures that edge cases like 404s and 405s are properly managed.
prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!".

        The application must:

        - Return HTTP 405 for unsupported HTTP methods.
        - Return HTTP 404 for unknown routes.
        - Include a global error handler for unhandled exceptions.
        - Avoid exposing stack traces to the client.
        - Log errors using Python's logging module.

        """

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)