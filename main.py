from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
import time

# --- 1. SETUP ---
# Initialize your FastAPI app   
app = FastAPI(title="Generative AI API (Local)")

# Load the "easy model" (distilgpt2) on startup.
# This pipeline will download the model the first time you run it.
generator = pipeline(
    "text-generation",
    model="distilgpt2",
    device="cpu" # Use "cpu" for Hugging Face free tier
)
print("Loading AI model... (This may take a moment the first time)")
generator = pipeline("text-generation", model="distilgpt2", device=cpu)
print("Model loaded successfully!")

# --- 2. DEFINE INPUT ---
# Define the data structure for your API's input
class Prompt(BaseModel):
    text: str
    max_length: int = 50

# --- 3. CREATE ENDPOINTS ---
# Create a "root" endpoint for basic checking
@app.get("/")
def read_root():
    return {"message": "Model API is running. Go to /docs for a test interface."}

# Create the "/generate" endpoint that will run the model
@app.post("/generate")
def generate_text(prompt: Prompt):
    """Generates text from a given prompt."""

    start_time = time.time()

    # Run the model!
    result = generator(prompt.text, max_length=prompt.max_length)

    end_time = time.time()
    latency = end_time - start_time

    # Return the result
    return {
        "generated_text": result[0]["generated_text"],
        "local_latency_seconds": latency
    }