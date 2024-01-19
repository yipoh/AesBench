## Data Release

### Step1: Download Dataset
- Option 1: through [BaiduYun](https://pan.baidu.com/s/1ghXunZJlIjhXGeSWeIl1sA?pwd=ippl).
- Option 2: through [Google Drive](https://drive.usercontent.google.com/download?id=1KsypUKfaFNNNdG995lUeDwOAu_xK8pax&export=download)
- Option 3: Through [HuggingFace](https://huggingface.co/datasets/qyuan/AesBench)

### Step2: Submit A Request For Access
The dataset is password protected. Please send a download application email to `huangyipo@stu.xidian.edu.cn` (Yipo Huang) together with ALL of the following contents:

- Your name
- Your affiliation
- Your purpose statement

We will send you the unzip password as soon as possible.  


## Evaluation 
Here is an example code for evaluating through API style, please fit the according lines for evaluating your own MLLMs.

### Evaluating AesA1
```python
python eval/eval_AesA1.py
```

### Evaluating AesE
```python
python eval/eval_AesE.py
```

### Evaluating AesI
```python
python eval/eval_AesI.py
```

### Evaluating AesP
```python
python eval/eval_AesP.py
```

### Submit results
After evaluation, you will get 4 files `(.json)`, please submit them to us together with the name of your tested MLLM through one of the following :

- Yipo Huang, `huangyipo@stu.xidian.edu.cn` (Primary)
- Quan Yuan, `dylan.yuanquan@outlook.com`,
- Xiangfei Sheng, `xiangfeisheng@gmail.com`,
- Zhichao Yang, `yangzhichao@stu.xidian.edu.cn`.

We will give you feedback on the evaluation result as soon as possible.

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
