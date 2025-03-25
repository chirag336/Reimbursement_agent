from fastapi import FastAPI, File, UploadFile, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from iced_main import process_image
from PIL import Image
import io
import uvicorn

app = FastAPI( title="Reimbursement Agent",
    version="1.0.0",)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)
    
@app.get("/health")
def read_root():
    return {"Hello": "World"}


app = FastAPI( title="pricing-engine",
    description="API to get pricing band on a query",
    version="1.0.0",)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)




@app.post("/output", summary="To get prediction on any building", description="Fetch predictions of defined building")
async def office_prediction(input_parameters: str = Form(...) , file: UploadFile = File(...)):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    print(input_dictionary)
    # image = input_dictionary["image"]
    name = input_dictionary['name']
    
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    output = process_image(image, name)
    return {"output",output}