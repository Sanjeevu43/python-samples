
#pip install torch torchvision torchaudio
# Install Hugging Face Transformers
#pip install transformers
# Install Pillow for image handling
#pip install Pillow
# Install requests (if you want to load images from URLs)
#pip install requests

import requests
from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel
import torch # Make sure torch is installed

# --- Configuration ---
# Choose the TrOCR model. Examples:
# 'microsoft/trocr-base-handwritten'
# 'microsoft/trocr-base-printed'
# 'microsoft/trocr-large-handwritten'
# 'microsoft/trocr-large-printed'
MODEL_NAME = 'microsoft/trocr-base-handwritten'

# --- Load Model and Processor ---
print(f"Loading TrOCR processor and model: {MODEL_NAME}...")
try:
    processor = TrOCRProcessor.from_pretrained(MODEL_NAME)
    model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)
    print("Model and processor loaded successfully.")
except OSError as e:
    print(f"Error loading model/processor: {e}")
    print(f"Please ensure the model name '{MODEL_NAME}' is correct and you have internet access.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred during loading: {e}")
    exit()

# --- Load Image ---
# Option 1: Load from a local file path
image_path = 'path/to/your/handwritten_image.png' # <--- CHANGE THIS TO YOUR IMAGE PATH
try:
    image = Image.open(image_path).convert("RGB")
    print(f"Image loaded successfully from: {image_path}")
except FileNotFoundError:
    print(f"Error: Image file not found at '{image_path}'")
    print("Please provide a valid path to your image file.")
    # Example of loading from URL if file not found (optional)
    print("\nTrying to load a sample image from URL instead...")
    # A sample image URL (replace with your own if needed)
    url = 'https://fki.tic.heia-fr.ch/static/img/a01-122-02.jpg' # Example IAM handwriting DB image
    try:
        image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
        print(f"Sample image loaded successfully from URL: {url}")
    except Exception as url_e:
        print(f"Error loading sample image from URL: {url_e}")
        exit()
except Exception as e:
    print(f"An error occurred loading the image: {e}")
    exit()


# --- Process Image and Perform OCR ---
print("Processing image and performing OCR...")

# 1. Preprocess the image
# The processor prepares the image for the model (resizing, normalization)
# and returns pixel values as PyTorch tensors.
try:
    pixel_values = processor(images=image, return_tensors="pt").pixel_values
except Exception as e:
    print(f"Error processing image: {e}")
    exit()

# Check if GPU is available and move tensors if desired
# device = "cuda" if torch.cuda.is_available() else "cpu"
# model.to(device)
# pixel_values = pixel_values.to(device)
# print(f"Using device: {device}") # Uncomment these lines for GPU support

# 2. Generate text IDs
# The model's generate method performs the forward pass and generates token IDs.
try:
    # Increase max_length if you expect longer text outputs
    generated_ids = model.generate(pixel_values, max_length=64)
except Exception as e:
    print(f"Error during model generation (inference): {e}")
    exit()

# 3. Decode the generated IDs to text
# The processor decodes the token IDs back into a human-readable string.
# skip_special_tokens=True removes tokens like [CLS], [SEP], [PAD] etc.
try:
    generated_text = processor.batch_decode(generated_ids, skip_special_tokens=True)[0]
except Exception as e:
    print(f"Error decoding generated IDs: {e}")
    exit()

# --- Print Result ---
print("-" * 30)
print(f"Recognized Text: {generated_text}")
print("-" * 30)