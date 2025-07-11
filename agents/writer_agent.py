# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def compile_final_report(summaries, critiques):
#     text = ""
#     for s, c in zip(summaries, critiques):
#         text += f"SUMMARY:\n{s}\n\nCRITIQUE:\n{c}\n\n"
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     response = model.generate_content(f"Generate a detailed research report from the following:\n\n{text}")
#     return response.text


import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Configure UltraSafe client
ULTRASAFE_API_KEY = os.getenv("ULTRASAFE_API_KEY")
ULTRASAFE_BASE_URL = os.getenv("ULTRASAFE_BASE_URL", "https://api.us.inc/usf/v1/hiring/")

client = OpenAI(
    api_key=ULTRASAFE_API_KEY,
    base_url=ULTRASAFE_BASE_URL,
)

def compile_final_report(summaries, critiques):
    text = ""
    for s, c in zip(summaries, critiques):
        text += f"SUMMARY:\n{s}\n\nCRITIQUE:\n{c}\n\n"

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert research analyst. Generate a well-structured research report based on summaries and critiques."},
                {"role": "user", "content": f"Generate a detailed research report from the following:\n\n{text}"}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"
