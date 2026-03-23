
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a Hebrew teacher.

Rules:
- No vowels unless user asks
- Detect male/female grammar
- Correct mistakes briefly
- Prefer conversational Hebrew
"""

def ask_ai(prompt):

    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)


def correct_hebrew(sentence):

    prompt = f"Correct this Hebrew sentence and explain briefly: {sentence}"

    return ask_ai(prompt)
