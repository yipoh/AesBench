from dotenv import load_dotenv
import google.generativeai as genai
import os
import PIL.Image
import torch
device = "cuda" if torch.cuda.is_available() else "cpu"

# Load the API Key

load_dotenv()
genai.configure(api_key=os.getenv('API_KEY'))
api_key=os.getenv('API_KEY')

# Load the sample image.
sample_image = PIL.Image.open("/Users/daniel/Repositories/aesbench-mllm/imgs/img1.png")
sample_image.show()


# Write your question.
prompt = "Write anime story about the character on the image, make it one sentence trailer about the character."

# Choose a Gemini model.
#model = genai.GenerativeModel('gemini-1.5-flash') 
model = genai.GenerativeModel('gemini-1.5-pro')

# Ask Gemini
response = model.generate_content([prompt, sample_image])

# Get answer.
result = response._result
text_content = result.candidates[0].content.parts[0].text
print("\n" + text_content)



