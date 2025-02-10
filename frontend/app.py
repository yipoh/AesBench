from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import PIL.Image
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import google.generativeai as genai

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load the API Key from the .env file located in the root directory
load_dotenv()
genai.configure(api_key=os.getenv('API_KEY'))

# Predefined prompts for each assessment method
prompts = {
    "AesA1": "How is the aesthetic quality of this image? Choose one from the following options: High, Medium, and Low.",
    "AesA2": "How is the aesthetic quality of this image? Rate them from scale 1 to 5.",
    "AesA3": "How is the aesthetic quality of this image? Rate them from scale 1 to 10."
}

# Function to read pre-prompt from a text file
def read_pre_prompt(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except Exception as e:
        print(f"Error reading pre-prompt file: {e}")
        return ""

# Generative AI model class
class GptRequest:
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def forward(self, prompt, image_path):
        img = PIL.Image.open(image_path)
        response = self.model.generate_content([prompt, img])
        response.resolve()

        # Extract and return the result
        result = response._result  
        if result.candidates:
            text_content = result.candidates[0].content.parts[0].text.rstrip()
            return text_content.strip()
        else:
            return "No response generated."

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Get the selected assessment method
            method = request.form.get('method')

            # Get the corresponding prompt
            prompt = prompts.get(method, "")

            # Check if the selected method has a specific pre-prompt and add it
            if method == "AesA1":
                pre_prompt = read_pre_prompt('pre_prompt1.txt')
                prompt = pre_prompt + "\n" + prompt
            elif method == "AesA2":
                pre_prompt = read_pre_prompt('pre_prompt2.txt') 
                prompt = pre_prompt + "\n" + prompt
            elif method == "AesA3":
                pre_prompt = read_pre_prompt('pre_prompt3.txt')  
                prompt = pre_prompt + "\n" + prompt

            # Use the GptRequest class to generate the assessment
            gpt_request = GptRequest()
            result = gpt_request.forward(prompt, filepath)

            # Split the result into answer and explanation
            answer, explanation = result.split("Explanation: ")

            # Pass the filename, answer, and explanation to the result.html template
            return render_template('result.html', filename=filename, answer=answer, explanation=explanation)
    
    return render_template('index.html')

# Updated route to serve uploaded files
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=False) 