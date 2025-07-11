# from langchain.chains.summarize import load_summarize_chain
# from langchain.chat_models import ChatOpenAI

# def compress_context(docs):
#     llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")
#     chain = load_summarize_chain(llm, chain_type="map_reduce")
#     return chain.run(docs)

# import os
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# def compress_context(docs):
#     """
#     Use Gemini to generate a compressed summary of a list of documents.
#     """
#     model = genai.GenerativeModel("gemini-1.5-flash-latest")
#     combined_text = "\n\n".join(docs)
#     prompt = f"""
#     Summarize the following documents into a concise, integrated summary that preserves all key findings,
#     data points, and important nuances, without losing critical information.

#     Documents:
#     {combined_text}
#     """
#     response = model.generate_content(prompt)
#     return response.text

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load env variables
load_dotenv()

ULTRASAFE_API_KEY = os.getenv("ULTRASAFE_API_KEY")
ULTRASAFE_BASE_URL = os.getenv("ULTRASAFE_BASE_URL", "https://api.us.inc/usf/v1/hiring/")

# Configure UltraSafe client
client = OpenAI(
    api_key=ULTRASAFE_API_KEY,
    base_url=ULTRASAFE_BASE_URL,
)

def compress_context(docs):
    """
    Use UltraSafe API to generate a compressed summary of a list of documents.
    """
    combined_text = "\n\n".join(docs)
    prompt = f"""
    Summarize the following documents into a concise, integrated summary that preserves all key findings,
    data points, and important nuances, without losing critical information.

    Documents:
    {combined_text}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a summarization expert."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"[Error] {str(e)}"


