from langchain_community.chat_models import ChatOpenAI

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    model = "gpt-4o-mini",
    api_key  = os.getenv('OPENAI_API_KEY'),
    base_url= os.getenv('OPENAI_API_BASE_URL')
)