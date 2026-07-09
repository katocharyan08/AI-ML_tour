import os
from openai import OpenAI

client = OpenAI(
   api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": """You are a prson named Aryan, eho epeaks hindi as well as english. 
                                         You are from india. you analyze copied_text and respomd like Aryan. 
                                         Output should be the next chat response as Arayn. """},
        {"role": "user", "content": copied_text},
    ]
)
print(completion.choices[0].message.content)    