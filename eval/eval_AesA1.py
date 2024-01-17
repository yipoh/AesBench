import torch
from PIL import Image
device = "cuda" if torch.cuda.is_available() else "cpu"
import json, time, os
import google.generativeai as genai
import PIL.Image

# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
genai.configure(api_key="XX")

class gptRequest():
    def __init__(self) -> None:
        self.model = genai.GenerativeModel('gemini-pro-vision')
    def forward(self, prompt, image_path,  server='Gemini'):
        if server == 'Gemini':
            img = PIL.Image.open(image_path)
            text = ""
            while len(text) < 3:
                try:
                    response = self.model.generate_content([prompt, img], stream=True)
                    response.resolve()
                    try:
                        text = response.text.strip()
                    except:
                        text = " "
                except Exception as error:
                    print(error)
                    print('Sleeping for 10 seconds')
                    time.sleep(10)
                    text = text+" "

        return text



if True:


    path = ".\images"
    save_name= "test_AesA1.json"
    f = open(r"AesBench_evaluation.json", encoding='utf-8')
    data=json.load(f)
    f.close()
    answers={}
    gpt_request = gptRequest()
    all_num = len(data)

    img_num = 1
    start_time = time.time()
    #####-------AesA1--------------------------
    for imgName, label in data.items():
        print()
        print(imgName)
        img_path = os.path.join(path, imgName)

        AesA1_data = label['AesA1_data']
        AesA1_prompt = AesA1_data['Question'] + " Choose one from the following options:\n" + AesA1_data['Options'] + "\nYou should output a correct option."
        print(AesA1_prompt)
        start = time.time()
        time.sleep(1)
        AesA1_message = gpt_request.forward(AesA1_prompt, img_path)
        print(AesA1_message)
        answers[imgName] = {"AesA1_response": AesA1_message}
        avg_time = (time.time() - start_time) / img_num
        need_time = (avg_time * (all_num - img_num)) / 3600
        answers_dict = json.dumps(answers, indent=4)
        with open(save_name, 'w') as outfile:
            outfile.write(answers_dict)
        print(
            "AesA1--{}/{} finished. Using time (s):{:.1f}. Average image time (s):{:.1f}. Need time (h):{:.1f}.".format(
                img_num, all_num, time.time() - start, avg_time, need_time))
        img_num = img_num + 1

