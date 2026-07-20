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
