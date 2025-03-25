
from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import pytesseract
import io
from PIL import Image
import uuid


def run_tesseract(image:bytes):



    img_byte_arr=image
    
    img = Image.open(io.BytesIO(img_byte_arr))
    text = pytesseract.image_to_string(img)
    # new_uuid =uuid.uuid4()
    return text