import os
from openai import OpenAI
from dotenv import load_dotenv
from typing import List
from modules.prompt_templates import SYSTEM_PROMPT, USER_PROMPT

# .env에서 API 키 로드
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def generate_answer(query: str, contexts: List[str]) -> str:
    """
    검색된 문단(contexts)을 바탕으로 GPT가 자연스러운 최종 답변 생성
    """
    context_text = "\n\n".join(contexts)
    prompt = USER_PROMPT.format(context_text=context_text, query=query)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=500
    )

    return response.choices[0].message.content.strip()
