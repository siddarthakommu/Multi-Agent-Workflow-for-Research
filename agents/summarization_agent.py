# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def summarize_documents(docs):
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     summaries = []
#     for doc in docs:
#         response = model.generate_content(f"Summarize this academic document:\n\n{doc}")
#         summaries.append(response.text)
#     return summaries


import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load variables from .env

# Configure UltraSafe-compatible client
ULTRASAFE_API_KEY = os.getenv("ULTRASAFE_API_KEY")
ULTRASAFE_BASE_URL = os.getenv("ULTRASAFE_BASE_URL", "https://api.us.inc/usf/v1/hiring/")

client = OpenAI(
    api_key=ULTRASAFE_API_KEY,
    base_url=ULTRASAFE_BASE_URL,
)

def summarize_documents(docs):
    summaries = []
    for doc in docs:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful research assistant that summarizes academic texts."},
                    {"role": "user", "content": f"Summarize this academic document:\n\n{doc}"}
                ]
            )
            summaries.append(response.choices[0].message.content)
        except Exception as e:
            summaries.append(f"[Error] {str(e)}")
    return summaries
