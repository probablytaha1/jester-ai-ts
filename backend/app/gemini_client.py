
import os, google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY missing in environment")
genai.configure(api_key=API_KEY)
_MODEL = genai.GenerativeModel("gemini-1.5-pro-latest", generation_config={"temperature":0.3})

def generate(text: str) -> str:
    return _MODEL.generate_content(text).text
