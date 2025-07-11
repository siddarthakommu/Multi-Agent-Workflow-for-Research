# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def critique_summaries(summaries):
#     model = genai.GenerativeModel('gemini-1.5-flash')
#     critiques = []
#     for summary in summaries:
#         response = model.generate_content(f"Critically evaluate this summary, highlight flaws or unsupported claims:\n\n{summary}")
#         critiques.append(response.text)
#     return critiques


import os
from openai import OpenAI

# Configure the UltraSafe-compatible client
client = OpenAI(
    api_key=os.getenv("ULTRASAFE_API_KEY"),
    base_url=os.getenv("ULTRASAFE_BASE_URL", "https://api.us.inc/usf/v1/hiring/")
)

def critique_summaries(summaries):
    critiques = []
    for summary in summaries:
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a critical reviewer helping evaluate text summaries."
                    },
                    {
                        "role": "user",
                        "content": f"Critically evaluate this summary, highlight flaws or unsupported claims:\n\n{summary}"
                    }
                ]
            )
            critiques.append(response.choices[0].message.content)
        except Exception as e:
            critiques.append(f"[Error] {str(e)}")
    return critiques
