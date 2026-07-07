import os

from openai import OpenAI
client = OpenAI(
   api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello! How can I use the OpenAI API in my Python project?"},
    ]
)
print(completion.choices[0].message.content)    