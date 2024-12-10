import io
import pickle
import numpy as np
import PIL
from PIL import Image, ImageOps
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

# Load the pre-trained model
with open('mnist_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Create FastAPI app
app = FastAPI()


# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Digit Classifier API"}


@app.get("/favicon.ico")
def favicon():
    return {"message": "No favicon available"}

@app.post("/predict-image/")
async def predict_image(file: UploadFile = File(...)):
    try:
        # Read the uploaded image
        contents = await file.read()
        pil_image = Image.open(io.BytesIO(contents)).convert('L')  # Convert to grayscale
        
        # Invert colors and resize to 28x28
        pil_image = ImageOps.invert(pil_image)
        pil_image = pil_image.resize((28, 28), Image.Resampling.LANCZOS)
        
        # Convert the image to a numpy array and reshape it for the model
        img_array = np.array(pil_image).reshape(1, -1)
        
        # Make a prediction
        prediction = model.predict(img_array)
        return {"prediction": int(prediction[0])}
    
    except Exception as e:
        # Log the error and return a user-friendly message
        print(f"Error processing image: {e}")
        return {"error": "Failed to process the image"}, 400
