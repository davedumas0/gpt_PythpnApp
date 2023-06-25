import os
from openai.error import RateLimitError
import backoff
import openai

@backoff.on_exception(backoff.expo, RateLimitError)

def read_api_key(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

api_key_file_path = "C:/MY GAME/java games/gptAPP/gpt/api_key.txt"
api_key = read_api_key(api_key_file_path)
openai.api_key = api_key
