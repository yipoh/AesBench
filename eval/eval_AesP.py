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
    save_name= "test_AesP.json"
    f = open(r"AesBench_evaluation.json", encoding='utf-8')
    data=json.load(f)
    f.close()
    answers={}
    gpt_request = gptRequest()
    all_num = len(data)

    img_num = 1
    start_time = time.time()
    #####-------AesP--------------------------
    for imgName, label in data.items():
        print()
        print(imgName)
        img_path = os.path.join(path, imgName)

        AesP_data = label['AesP_data']
        AesP_prompt = AesP_data['Question'] + " Choose one from the following options:\n" + AesP_data['Options'] + "\nYou should output a correct option without explanation."
        # print(AesP_prompt)
        start = time.time()
        time.sleep(1)
        AesP_message = gpt_request.forward(AesP_prompt, img_path)
        print(AesP_message)
        answers[imgName] = {"AesP_response": AesP_message}

        avg_time = (time.time() - start_time) / img_num
        need_time = (avg_time * (all_num - img_num)) / 3600

        answers_dict = json.dumps(answers, indent=4)
        with open(save_name, 'w') as outfile:
            outfile.write(answers_dict)
        print(
            "AesP--{}/{} finished. Using time (s):{:.1f}. Average image time (s):{:.1f}. Need time (h):{:.1f}.".format(
                img_num, all_num, time.time() - start, avg_time, need_time))
        img_num = img_num + 1

