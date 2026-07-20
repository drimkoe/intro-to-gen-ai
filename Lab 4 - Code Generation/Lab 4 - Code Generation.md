# Lab 4 - Code Generation

The focus of this lab is to investigate prompting as technical specification writing.

In this lab, you will
- Understand how vague prompts produce weak code
- Learn to write a structured engineering specification
- Include error handling requirements
- Include secure coding standards
- Reference PEP and Python standards
- Generate a high-quality Flask "Hello World" app

You can continue to use the same conda environment you used in lab 3/

## Part 1: Unstructured

Just like in the previous lab, run the following scrip `lab4a.py` in the conda console

```python

from openai import OpenAI

# Create client
client = OpenAI()

prompt="Write a simple Python Flask hello world application."
# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)

```
The model cannot implement requirements you did not specify

Look at the output and determine
- Does it specify Python version?
- Does it include error handling?
- Does it mention security?
- Does it follow PEP standards?
- Does it pin dependencies?
- Does it include input validation?


## Part 2: Clear Statement of the Programming Problem

Add a clear statement of the programming problem

```Python
from openai import OpenAI

# Create client
client = OpenAI()

prompt="""Create a minimal but production-quality Python 3.11 Flask web application
        that exposes a single HTTP GET endpoint at the root path ("/")
        and returns the text "Hello, World!"."""

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)

```

## Part 3: Error Handling Requirements

Now we add in the explicit error handling requirements

```Python

from openai import OpenAI

# Create client
client = OpenAI()

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
```

## Part 4: Secure Coding Requirements

Now we add into the specification the secure coding requirements.

```Python


from openai import OpenAI

# Create client
client = OpenAI()

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
```

## Part 5: Coding standards

Now we specify coding standards

```python
from openai import OpenAI

# Create client
client = OpenAI()

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

        Coding Standards:

        - Follow PEP 8 style guidelines.
        - Follow PEP 257 for docstrings.
        - Include type hints (PEP 484).
        - Organize code using functions and main guard:
            if __name__ == "__main__":
        - Include a requirements.txt file.
        - Include comments explaining key sections.
        """

# Simple prompt
response = client.responses.create(
    model="gpt-4.1-mini",
    input=prompt
)

print(response.output_text)
```

The final output is now in the `Final` folder in the file
 
## Part 6: Generating tests.

Now we switch the role of the LLM from being a developer to being a QA engineer. We can now ask it to generate a series of tests based on the code.

This is in the script `lab4f.py` Note that we are now supplying the code as input for the prompt to work on.


```python
from openai import OpenAI

client = OpenAI()

with open("Hello.py", "r", encoding="utf-8") as f:
    flask_code = f.read()

prompt = f"""
You are a senior QA automation engineer.

Analyze the following Python Flask application and generate a comprehensive
set of test cases.

Requirements:

1. Provide functional test cases.
2. Provide negative test cases.
3. Provide security-related test cases.
4. Provide edge case scenarios.
5. Identify any potential failure points.
6. Provide pytest-based automated test examples.
7. Explain the reasoning behind each test.

Follow best practices for testing Flask applications.
Assume Python 3.11 and pytest.

Here is the application code:

{flask_code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "user", "content": prompt}
    ],
    temperature=0.3
)

print(response.choices[0].message.content)

```

Run this and see the tests and explanations that have been generated. If you are having problems, the file `testcases.txt` shows the output of this script.


## Part 7: Dockerizing the application

Now we can create a dockerized version of our flask application by having the LLM act as a CI/CD engineer and create a high quality Dockerfile.

```python
from openai import OpenAI

client = OpenAI()

# Read Flask code from file
with open("Hello.py", "r", encoding="utf-8") as f:
    flask_code = f.read()

prompt = f"""
You are a senior DevOps engineer specializing in containerization.

Analyze the following Flask application and generate a production-ready Dockerfile.

Requirements:

1. Use Python 3.11.
2. Use a minimal base image (prefer slim or alpine).
3. Do not run the container as root.
4. Use best practices for Docker layering.
5. Install dependencies from requirements.txt.
6. Disable debug mode.
7. Expose the correct port.
8. Use a production-ready WSGI server (e.g., gunicorn).
9. Minimize image size.
10. Follow Docker security best practices.

Provide:
- The complete Dockerfile
- Explanation of each section
- Any recommended improvements to the Flask app for containerization

Here is the Flask application:

```python
{flask_code}

"""

response = client.chat.completions.create(
model="gpt-4o-mini",
messages=[{"role": "user", "content": prompt}],
temperature=0.3
)

print(response.choices[0].message.content)

```

The result is also shown in docker.txt.


## End Lab
