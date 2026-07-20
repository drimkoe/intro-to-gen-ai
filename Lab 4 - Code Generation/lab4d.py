

"""
Lab 4d - Secure Coding Requirements
This script adds explicit security requirements to our prompt.
If you don't ask for security, the LLM might take shortcuts (like leaving debug mode on).
"""
from openai import OpenAI

# Create client
client = OpenAI()

# By explicitly calling out "Security Requirements" and mentioning frameworks
# like OWASP, we trigger the LLM's knowledge base on security best practices.
# We also explicitly forbid hardcoded secrets and require input sanitization.
prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!".

        The application must:

        - Return HTTP 405 for unsupported HTTP methods.
        - Return HTTP 404 for unknown routes.
        - Include a global error handler for unhandled exceptions.
        - Avoid exposing stack traces to the client.
        - Log errors using Python's logging module.

        Security Requirements:

        - Disable Flask debug mode.
        - Do not expose internal exception details.
        - Use environment variables for configuration.
        - Follow OWASP secure coding principles where applicable.
        - Ensure no hardcoded secrets are present.
        - Validate and sanitize all external input (even if not currently used).
        """

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)