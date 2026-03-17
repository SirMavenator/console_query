# cq.py
'''
cq is a "console query": Query an LLM on the command line.
Gemini model and Gemini API key are specified in .env file.

This should be run in the c1 Conda environment as:

    cq.py --prompt "Explain briefly how an LLM works"

'''
import os
from google import genai
from dotenv import load_dotenv
import logging
import argparse

if __name__ == '__main__':

    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser()
    parser.add_argument('--prompt', type=str, help='Prompt string to send to model')
    args = parser.parse_args()

    load_dotenv()
    

    MODEL_NAME = os.getenv("GEMINI_MODEL_NAME", "")
    API_KEY = os.getenv("GEMINI_API_KEY", "")
    query = args.prompt

    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(model=MODEL_NAME, contents=query)

    logger.info(f'Prompt: {query}')
    logger.info(f'Response: {response.text}')

    

