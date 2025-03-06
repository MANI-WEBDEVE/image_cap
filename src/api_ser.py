from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import cloudinary
import cloudinary.uploader
from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("cloud_name") and os.getenv('api_key') and os.getenv('api_secret'):
    # Cloudinary Configuration
    cloudinary.config(
        cloud_name=os.getenv('cloud_name'),
        api_key=os.getenv('api_key'),
        api_secret=os.getenv('api_secret')
    )


# FastAPI App
app = FastAPI()

# CORS Middleware (Agar frontend se requests allow karna hai)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Saare origins allow karein (production mein specific origins use karein)
    allow_methods=["*"],
    allow_headers=["*"],
)

# Image Upload Endpoint
@app.post("/upload-image/")
async def upload_image(file: UploadFile = File(...)):
    try:
        # File ko Cloudinary par upload karein
        result = cloudinary.uploader.upload(file.file, folder="user_images")
        return {"message": "Image uploaded successfully!", "url": result["secure_url"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Root Endpoint
@app.get("/")
def read_root():
    return {"message": "FastAPI server is running!"}