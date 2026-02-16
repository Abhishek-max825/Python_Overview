"""
Using Open AI API 
"""
from openai import OpenAI

key = "SECRET_KEY"
client = OpenAI(api_key=key)
response = client.responses.create(
    model="gpt-5.2",
    input="what is 2 + 2"
)

print(response.output_text)
