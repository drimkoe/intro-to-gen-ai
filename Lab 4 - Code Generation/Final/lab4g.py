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
