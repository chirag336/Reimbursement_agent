import datetime
import hashlib
import json
import logging
import os
import uuid
import numpy as np
from typing import List, Dict
import re

import openai

from sklearn.metrics.pairwise import cosine_similarity

from langchain_groq import ChatGroq

# Setup logging
logger = logging.getLogger(__name__)


class ReimService:
    def __init__(self):
        self.GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")
        self.llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        # other params...
        )
        self.extract_text = "hi 2000"
        self.text = None
        self.type = None


        
    def extract_price(self):
        text = self.extract_text
        text = re.sub(r'\.(\w{2})', '.', text)
        prompt = f'''I have extracted text from an OCR model of a bill or receipt of an expense I want to reimburese,
        I want you to tell me the total amount paid.
        
        keep in mind to remove any rupees sign ₹ or any other currency sign and

        


        The extracted text is :{text}
        
        answer in the format of just digits without decimals
        '''

        response = self.llm.invoke(prompt)
        self.text =response.content
    
    def extract_type(self):
        text = self.extract_text
        prompt = f'''I have extracted text from an OCR model of a bill or receipt of an expense I want to reimburese,
        I want you to tell me what type of bill it is.

        return me just the type from the fillowing types:
        1) Fuel
        2) Travel
        3) Hotel
        4) Food
        5) others



        The extracted text is :{text}
        '''
        
        response = self.llm.invoke(prompt)
        self.type = response.content
        
if __name__ == "__main__":
    contracts_service = ReimService()
    contracts_service.extract_price()