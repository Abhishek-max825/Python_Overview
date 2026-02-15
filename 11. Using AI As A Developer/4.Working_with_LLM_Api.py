"""
Using Open AI API to create a simple tic-tac-toe game where the user can play against an AI opponent. The AI will use the OpenAI API to determine its moves based on the current state of the board. The game will have both single-player and two-player modes, allowing users to either play against the AI or against another human player. The code will include functions for displaying the board, checking for winners, and handling user input.
"""
from openai import OpenAI

key = "SECRET_KEY"
client = OpenAI(api_key=key)
response = client.responses.create(
    model="gpt-5.2",
    input="what is 2 + 2"
)

print(response.output_text)
