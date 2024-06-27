
  <h1>AesBench </h1>    

_Can your MLLM understand the highly abstract image aesthetics like humans? Come and test on AesBench !_
    
 <div>
    <a href="https://github.com/yipoh/AesBench"><img src="https://img.shields.io/github/stars/yipoh/AesBench"/></a>
    <a href="https://arxiv.org/abs/2401.08276"><img src="https://img.shields.io/badge/Arxiv-2401:08276-red"/></a>
    <a href="https://huggingface.co/datasets/qyuan/EAPD_release"><img src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Dataset-green"></a>
    <a href="https://github.com/yipoh/AesBench/tree/main/data_release"><img src="https://img.shields.io/badge/Data-Release-orange"></a>
</div>


<h5> If you like this work, please give us a star ⭐ on GitHub.  </h2>
    

<h1>Introduction</h1> 
</div>

 <br>

</h5>
</p> 
<p align="center">
    <img src="imgs/overview.png"/>
<p>

<p align="justify">Multimodal Large Language Models (MLLMs) are undergoing flourishing development, promoting human-machine interaction and collaboration in daily life. However, their capacities for understanding image aesthetics largely remain unexplored. This may impede the applications of advanced MLLMs in real-world scenarios, such as art design and image generation. To address this dilemma, we introduce  <strong>AesBench</strong>, <strong>an expert benchmark to systematically evaluate the aesthetic understanding capacities of MLLMs</strong>. In this benchmark, high-quality annotations are first collected from aesthetic experts, based on which an aesthetics understanding benchmark dataset is built. In addition, we design a set of integrative criteria to evaluate MLLMs from four shallow-to-deep perspectives, including perception (AesP), empathy (AesE), assessment (AesA), and interpretation (AesI). We hope this work can encourage the community to delve into more profound investigations of the yet untapped potential of MLLMs in image aesthetics understanding.</p>


## Update
- 🎉 We have supported [VLMEvalKit](https://github.com/open-compass/VLMEvalKit) to facilitate quick testing of your MLLMs. 🔥🔥🔥
- 🎉 Congrats to [SPHINX-MoE](https://github.com/Alpha-VLLM/LLaMA2-Accessory) for achieving new SOTAs on AesP and AesE!!
- 🤗 Database of AesBench now support [Huggingface](https://huggingface.co/datasets/qyuan/EAPD_release)!
- 🚩 We have released the Evaluation Database and Codes of AesBench! Check [Here](https://github.com/yipoh/AesBench/tree/main/data_release) for more details. 




## Leaderboard

Here is the comparison of [GPT-4V](https://chat.openai.com), [Gemini Pro Vision](https://ai.google.dev/), and other OA MLLMs on AesP

| Rank |MLLM       | Tec. Qua.| Col. Lig.|Comp.|Content|NIs  | AIs  | AGIs  | Yes-No | What | How | Why  |Overall|
|:----:|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| 🥇 | SPHINX-MoE        | 66.67%    | 76.31%       | 72.68% | 66.31% | 75.84%  | 72.19% | 68.88% | 69.12% | 62.18% | 80.38% | 88.05% | 72.93% |
| 🥈 | Q-Instruct        | 66.03%    | 74.48%       | 73.68% | 68.09% | 76.48%  | 69.70% | 69.28% | 64.68% | 63.31% | 85.28% | 86.34% | 72.61% |
| 🥉 | GPT-4V            | 69.02%    | 74.66%       | 71.72% | 65.57% | 75.67%  | 72.58% | 65.82% | 68.93% | 64.67% | 76.70% | 84.46% | 72.08% |
| 4 | Gemini Pro Vision | 65.08%    | 74.57%       | 72.24% | 67.97% | 74.63%  | 69.62% | 70.03% | 64.70% | 64.95% | 78.71% | 90.24% | 71.99% |
| 5  | ShareGPT4V        | 62.18%    | 71.90%       | 69.29% | 64.89% | 70.79%  | 71.57% | 63.96% | 69.32% | 61.33% | 72.01% | 77.56% | 69.18% |
| 6  | mPLUG-Owl2        | 60.90%    | 70.57%       | 68.30% | 62.77% | 72.23%  | 64.71% | 64.10% | 65.59% | 58.64% | 73.02% | 80.73% | 67.89% |
| 7  | LLaVA-1.5         | 53.85%    | 70.16%       | 67.40% | 59.93% | 69.10%  | 65.71% | 62.37% | 62.36% | 58.92% | 70.71% | 81.22% | 66.32% |
| 8  | Qwen-VL           | 54.81%    | 66.25%       | 62.91% | 60.64% | 68.30%  | 58.85% | 59.44% | 61.25% | 55.38% | 67.53% | 74.15% | 63.21% |
| 9  | LLaVA             | 46.79%    | 63.59%       | 65.30% | 64.54% | 64.29%  | 61.10% | 60.77% | 65.39% | 52.27% | 61.18% | 74.88% | 62.43% |
| 10  | InstructBLIP      | 37.82%    | 55.36%       | 55.43% | 57.09% | 57.06%  | 55.86% | 47.21% | 59.84% | 45.01% | 54.98% | 56.34% | 54.29% |
| 11 | MiniGPT-v2       | 56.73%  | 56.44%  | 51.74%  | 50.00%  | 56.74%  | 53.24%  | 50.93%  | 53.99%  | 43.06%  | 58.73%   | 66.10%   | 54.18%   |
| 12 | GLM              | 55.77%  | 54.61%  | 51.25%  | 48.94%  | 54.90%  | 55.24%  | 47.34%  | 60.95%  | 44.62%  | 48.48%   | 55.61%   | 52.96%   |
| 13 | Otter            | 35.90%  | 54.28%  | 51.65%  | 51.06%  | 51.04%  | 50.62%  | 51.20%  | 56.10%  | 44.48%  | 51.37%   | 49.02%   | 50.96%   |
| 14 | IDEFICS-Instruct | 37.50%  | 52.87%  | 52.84%  | 51.06%  | 52.97%  | 50.12%  | 48.40%  | 50.96%  | 44.62%  | 51.09%   | 60.73%   | 50.82%   |
| 15 | MiniGPT-4        | 39.42%  | 41.31%  | 42.67%  | 44.33%  | 41.57%  | 42.89%  | 41.36%  | 47.23%  | 32.01%  | 41.99%   | 46.10%   | 41.93%   |
| 16 | TinyGPT-V        | 21.79%  | 24.52%  | 22.13%  | 28.01%  | 22.71%  | 24.69%  | 24.34%  | 32.39%  | 17.99%  | 19.77%   | 19.27%   | 23.71%   |


Here is the comparison of [GPT-4V](https://chat.openai.com), [Gemini Pro Vision](https://ai.google.dev/), and other OA MLLMs on AesE 

| Rank | MLLM            | Emotion | Interest | Uniqueness | Vibe | NIs | AIs | AGIs | Yes-No | What | How | Why | Overall |
|:----:|:---------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
|🥇| SPHINX-MoE       | 68.59%  | 80.65%  | 75.86%  | 82.14%  | 74.72%  | 75.19%  | 69.02%  | 74.95%  | 62.89%  | 72.71%   | 88.48%   | 73.32%   |
|🥈| Q-Instruct       | 68.64%  | 83.86%  | 75.86%  | 80.00%  | 76.65%  | 72.19%  | 66.62%  | 64.30%  | 67.42%  | 81.57%   | 86.76%   | 72.68%   |
|🥉| Gemini Pro Vision| 66.87%  | 87.50%  | 70.00%  | 79.09%  | 70.60%  | 72.35%  | 71.53%  | 67.50%  | 64.52%  | 72.25%   | 90.37%   | 71.37%   |
|4| ShareGPT4V       | 66.48%  | 80.65%  | 68.97%  | 78.72%  | 70.95%  | 73.69%  | 67.29%  | 67.75%  | 65.58%  | 72.71%   | 83.58%   | 70.75%   | 
|5|GPT-4V           | 65.06%  | 72.41%  | 62.07%  | 80.15%  | 73.87%  | 72.08%  | 62.27%  | 68.67%  | 64.02%  | 70.07%   | 84.20%   | 70.16%   |
|6| mPLUG-Owl2       | 65.60%  | 77.42%  | 65.52%  | 78.07%  | 71.03%  | 71.57%  | 66.22%  | 68.05%  | 64.16%  | 70.14%   | 83.82%   | 69.89%   |
|7| LLaVA-1.5        | 62.49%  | 80.65%  | 75.85%  | 78.93%  | 69.26%  | 69.58%  | 65.43%  | 62.37%  | 64.16%  | 71.71%   | 84.07%   | 68.32%   |
|8| LLaVA            | 58.61%  | 80.63%  | 65.52%  | 75.83%  | 67.01%  | 66.96%  | 58.38%  | 67.95%  | 55.95%  | 60.14%   | 79.66%   | 64.68%   |
|9| Qwen-VL          | 58.67%  | 83.87%  | 72.41%  | 73.90%  | 63.88%  | 67.08%  | 61.57%  | 60.65%  | 58.07%  | 66.14%   | 79.90%   | 64.18%   |
|10| MiniGPT-v2        | 52.52%  | 58.06%  | 44.83%  | 58.07%  | 55.86%  | 55.85%  | 50.27%  | 57.81%  | 43.48%  | 53.43%   | 66.42%   | 54.36%   |
|11| GLM               | 53.13%  | 70.97%  | 44.83%  | 55.29%  | 56.58%  | 54.86%  | 48.67%  | 60.65%  | 41.78%  | 50.43%   | 64.95%   | 53.96%   |
|12| InstructBLIP      | 49.64%  | 58.06%  | 51.72%  | 61.50%  | 55.06%  | 55.24%  | 48.94%  | 55.88%  | 50.99%  | 51.43%   | 58.33%   | 53.89%   |
|13| Otter             | 48.42%  | 70.97%  | 51.72%  | 63.21%  | 53.05%  | 55.74%  | 52.39%  | 54.77%  | 51.84%  | 53.43%   | 54.41%   | 53.64%   |
|14| IDEFICS-Instruct  | 43.93%  | 64.52%  | 62.07%  | 64.06%  | 50.72%  | 53.12%  | 49.07%  | 50.20%  | 41.08%  | 52.43%   | 66.42%   | 50.82%   |
|15| MiniGPT-4         | 39.78%  | 38.71%  | 24.14%  | 39.04%  | 42.70%  | 37.78%  | 35.51%  | 50.61%  | 31.59%  | 31.86%   | 38.48%   | 39.35%   |
|16| TinyGPT-V         | 30.36%  | 29.03%  | 31.03%  | 35.40%  | 32.50%  | 36.03%  | 26.99%  | 36.00%  | 29.89%  | 28.86%   | 31.62%   | 32.04%   |


Here is the comparison of [GPT-4V](https://chat.openai.com), [Gemini Pro Vision](https://ai.google.dev/), and other OA MLLMs on AesA

| Rank | MLLM               | NIs| AIs | AGIs | Overall |
|:----:|:---------:|:-----:|:-----:|:-----:|:-----:|
|🥇| Q-Instruct          | 62.20%  | 49.75%  | 40.69%  | 52.86%  |
|🥈| GPT-4V              | 59.98%  | 46.92%  | 40.59%  | 50.86%  |
|🥉| mPLUG-Owl2          | 57.78%  | 49.50%  | 40.83%  | 50.57%  |
|4| SPHINX-MoE           | 57.62%  | 48.50%  | 38.70%  | 49.93%  |
|5| Gemini Pro Vision   | 54.17%  | 48.39%  | 42.20%  | 49.38%  |
|6| ShareGPT4V          | 54.65%  | 48.38%  | 35.90%  | 47.82%  |
|7| InstructBLIP        | 52.73%  | 47.88%  | 34.84%  | 46.54%  |
|8| Qwen-VL             | 54.25%  | 39.28%  | 40.43%  | 46.25%  |
|9| LLaVA               | 51.69%  | 48.00%  | 34.31%  | 45.96%  |
|10| LLaVA-1.5           | 50.08%  | 48.13%  | 34.97%  | 45.46%  |
|11| IDEFICS-Instruct    | 50.00%  | 47.76%  | 33.78%  | 45.00%  |
|12| Otter               | 49.20%  | 48.25%  | 34.04%  | 44.86%  |
|13| TinyGPT-V           | 44.06%  | 41.65%  | 44.81%  | 43.57%  |
|14| MiniGPT-4           | 41.65%  | 36.28%  | 35.90%  | 38.57%  |
|15| GLM                 | 38.92%  | 37.78%  | 35.90%  | 37.79%  |
|16| MiniGPT-v2          | 27.05%  | 31.92%  | 36.97%  | 31.11%  |


Here is the comparison of [GPT-4V](https://chat.openai.com), [Gemini Pro Vision](https://ai.google.dev/), and other OA MLLMs on AesI


|Rank | Model               | Relevance | Precision | Completeness | Overall | 
|:----:|:---------:|:-----:|:-----:|:-----:|:-----:|
|🥇|GPT-4V              | 1.385   | 1.151   | 1.366   | 1.301   |
|🥈| ShareGPT4V          | 1.440   | 1.117   | 1.331   | 1.296   |
|🥉| SPHINX-MoE   | 1.501   | 1.171   | 1.130   | 1.267   |
|4| Gemini Pro Vision   | 1.416   | 1.087   | 1.164   | 1.222   |
|5| Qwen-VL             | 1.393   | 1.006   | 1.175   | 1.192   |
|6| mPLUG-Owl2          | 1.402   | 1.016   | 1.130   | 1.182   |
|7| IDEFICS-Instruct    | 1.406   | 1.007   | 1.126   | 1.180   |
|8| LLaVA-1.5           | 1.397   | 0.953   | 1.120   | 1.157   |
|9| InstructBLIP        | 1.372   | 0.863   | 1.144   | 1.126   |
|10| LLaVA               | 1.374   | 0.918   | 1.084   | 1.125   |
|11| Otter               | 1.242   | 0.848   | 0.989   | 1.027   |
|12| Q-Instruct          | 1.222   | 0.939   | 0.898   | 1.020   |
|13| MiniGPT-v2          | 1.191   | 0.868   | 0.948   | 1.003   |
|14| MiniGPT-4           | 1.158   | 0.823   | 1.016   | 0.999   |
|15| GLM                 | 1.122   | 0.729   | 0.944   | 0.932   |
|16| TinyGPT-V           | 0.871   | 0.511   | 0.720   | 0.701   |


## Submission Guideline


- via GitHub Release: Please see our [release](https://github.com/yipoh/AesBench/tree/main/data_release) for details.





## Acknowledgement
We sincerely thank the 32 aesthetic experts who participated in the subjective experiments. Their rich aesthetic experience and responsible attitude make the benchmark results more reliable. We highlight partial contributors as follows:

>  **Wei Liu (educator), Xin Liu (researcher), Luxia Chen (educator), Tianjiao Gu (educator), Dahai Tian (educator), Ziyan Ou (art student)**

We extend our heartfelt thanks to our team members for their invaluable assistance in collecting data and deploying the MLLMs. We highlight partial collaborators as follows:
> **Zhichao Duan, Pangu Xie, Xinrui Xu, Yanxin Shi**


## Citation

If you find our work interesting, please feel free to cite our paper:

```bibtex
@article{AesBench,
    title={AesBench: An Expert Benchmark for Multimodal Large Language Models on Image Aesthetics Perception},
    author={Huang, Yipo and Yuan, Quan and Sheng, Xiangfei and Yang, Zhichao and Wu, Haoning and Chen, Pengfei and Yang, Yuzhe and Li, Leida and Lin, Weisi},
   journal={arXiv preprint arXiv:2401.08276},
    year={2024},
}
```
