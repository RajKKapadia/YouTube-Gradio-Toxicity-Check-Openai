import os

import openai
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

openai.api_key = os.getenv('OPENAI_API_KEY')

def check_toxicity(text: str) -> dict:
    response = openai.Moderation.create(
        input=text
    )
    scores = response['results'][0]['category_scores']
    scores = {k: float(v) for k, v in sorted(scores.items(), key=lambda item: item[1], reverse=True)}
    return scores

