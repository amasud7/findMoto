# pass data to gemini model and rank 10 choices --> give explanations?
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash",
                              system_instruction="You are a marketplace helper trying to help  the customer get the best deal on a bike. You look at the price of the bike and model and search the web to determine which motorcycle is the best deal."
                              )
response = model.generate_content("Rank the bikes from the following data")
print(response.text)
