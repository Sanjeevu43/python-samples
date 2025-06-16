
import requests
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch # Explicitly importing PyTorch

# --- Configuration ---
MODEL_NAME = 'microsoft/trocr-base-handwritten' # Or 'microsoft/trocr-base-printed', etc.
# A sample image URL (replace with your own local path or URL if needed)
# Example IAM handwriting DB image:
IMAGE_PATH_OR_URL = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg'
# IMAGE_PATH_OR_URL = 'path/to/your/local_image.png' # Example for local file

# --- Device Selection (Using torch) ---
# Check if CUDA (GPU support) is available, otherwise use CPU
# This is a direct use of the torch library
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

# --- Load Model and Processor ---
print(f"Loading TrOCR processor and model: {MODEL_NAME}...")
try:
    processor = TrOCRProcessor.from_pretrained(MODEL_NAME)
    # Load the model and immediately move it to the selected device
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME).to(device)
    print("Model and processor loaded successfully.")
except OSError as e:
    print(f"Error loading model/processor: {e}")
    print(f"Please ensure the model name '{MODEL_NAME}' is correct and you have internet access.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred during loading: {e}")
    exit()

# --- Load Image ---
print(f"Loading image from: {IMAGE_PATH_OR_URL}...")
try:
    if IMAGE_PATH_OR_URL.startswith("http"):
        image = Image.open(requests.get(IMAGE_PATH_OR_URL, stream=True).raw).convert("RGB")
    else:
        image = Image.open(IMAGE_PATH_OR_URL).convert("RGB")
    print("Image loaded successfully.")
except FileNotFoundError:
     print(f"Error: Local image file not found at '{IMAGE_PATH_OR_URL}'")
     exit()
except Exception as e:
    print(f"An error occurred loading the image: {e}")
    exit()


# --- Process Image and Perform OCR ---
print("Processing image...")

# 1. Preprocess the image using the processor
# return_tensors="pt" tells the processor to output PyTorch tensors
try:
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
    print(f"Image processed into a tensor of shape: {pixel_values.shape} and type: {pixel_values.dtype}") # Show tensor info
except Exception as e:
    print(f"Error processing image: {e}")
    exit()

# 2. Move the input tensor to the same device as the model (GPU or CPU)
# This is another direct use of the torch library's tensor methods
pixel_values = pixel_values.to(device)
print(f"Pixel values tensor moved to device: {pixel_values.device}")

# 3. Generate text IDs using the model (Inference)
print("Running model inference (generating token IDs)...")
try:
    # The model's generate method expects PyTorch tensors on the correct device
    # Increase max_length if you expect longer text outputs
    with torch.no_grad(): # Deactivate gradient calculations for inference - uses less memory
        generated_ids = model.generate(pixel_values, max_length=64)
    print("Token IDs generated.")
except Exception as e:
    print(f"Error during model generation (inference): {e}")
    exit()

# 4. Decode the generated IDs to text
print("Decoding token IDs to text...")
try:
    # generated_ids is also a PyTorch tensor, likely on the same device
    print(f"Generated IDs tensor shape: {generated_ids.shape}, device: {generated_ids.device}")
    # The processor decodes the token IDs back into a human-readable string.
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
except Exception as e:
    print(f"Error decoding generated IDs: {e}")
    exit()

# --- Print Result ---
print("-" * 30)
print(f"Recognized Text: {generated_text}")
print("-" * 30)