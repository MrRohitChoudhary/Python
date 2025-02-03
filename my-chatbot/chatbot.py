import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

print("Chatbot activated! Type 'quit' to exit")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    response = chat.send_message(user_input)
    print("Bot:", response.text)