from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
import boto3
import os
from dotenv import load_dotenv
from typing import Optional
import shutil

# Load environment variables
load_dotenv()

app = FastAPI(title="AI Chatbot API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# AWS Configuration
service_name = 'bedrock-runtime'
region = 'us-west-2'

# Initialize AWS client
client = boto3.client(
    service_name=service_name,
    region_name=region
)

# Configure upload folder
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'doc', 'docx', 'md'}

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename: str) -> bool:
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

async def read_file_content(file_path: str) -> str:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"Error reading file: {str(e)}"

@app.post("/chat")
async def chat(
    message: Optional[str] = Form(None),
    file: Optional[UploadFile] = File(None)
):
    try:
        # Handle file upload
        if file and allowed_file(file.filename):
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            
            file_content = await read_file_content(file_path)
            
            # Prepare the payload for Claude with file content
            payload = {
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {
                        "role": "user",
                        "content": f"Here's the content of the file '{file.filename}':\n\n{file_content}\n\nUser message: {message or ''}"
                    }
                ],
                "max_tokens": 1024,
                "temperature": 0.7
            }
        else:
            # Handle text-only message
            payload = {
                "anthropic_version": "bedrock-2023-05-31",
                "messages": [
                    {
                        "role": "user",
                        "content": message or ""
                    }
                ],
                "max_tokens": 1024,
                "temperature": 0.7
            }
        
        # Call Bedrock API
        response = client.invoke_model(
            modelId="anthropic.claude-3-5-haiku-20241022-v1:0",
            body=json.dumps(payload),
            accept='application/json',
            contentType='application/json'
        )
        
        # Parse the response
        response_body = json.loads(response["body"].read().decode("utf-8"))
        
        return JSONResponse({
            "response": response_body.get("content", [{}])[0].get("text", "Sorry, I couldn't process that.")
        })
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                "error": "An error occurred while processing your request",
                "details": str(e)
            }
        )

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000) 