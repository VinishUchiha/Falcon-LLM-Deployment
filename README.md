# Falcon-LLM-Deployment

This Repository contains code to create an OpenAI Clone using OpenSource Models with commercial licenses.

Here We are going to use Falcon-7B-instruct and Falcon-40B-instruct models to generate words in a conversational manner.

## Google VM Setup

First, You need to create a Google VM instance with A100 GPU(or any GPU with higher Memory).
### Step 1: Click the create instance button
<p align="center"><img alt="GCP Instruction" src="imgs/Screenshot from 2023-06-21 23-11-25.png"/></p>

### Step 2: Name your Instance(openllm) and Choose the GPU type and Count
<p align="center"><img alt="GCP Instruction" src="imgs/Screenshot from 2023-06-21 23-12-07.png"/></p>

### Step 3: Click the Switch Image
<p align="center"><img alt="GCP Instruction" src="imgs/Screenshot from 2023-06-21 23-12-34.png"/></p>

### Step 4: Select Ubuntu Operating System and Version above 20.04
<p align="center"><img alt="GCP Instruction" src="imgs/Screenshot from 2023-06-21 23-13-22.png"/></p>

### Step 5: Click the Create Button
<p align="center"><img alt="GCP Instruction" src="imgs/Screenshot from 2023-06-21 23-26-41.png"/></p>

## GPU Driver and CUDA Installation

Run the below cmd
```bash
curl https://raw.githubusercontent.com/GoogleCloudPlatform/compute-gpu-installation/main/linux/install_gpu_driver.py --output install_gpu_driver.py
sudo python3 install_gpu_driver.py
```

## HuggingFace Text Generation Inference

```bash
# Run the text generation inference docker container
docker run --gpus all -p 8080:80 -v $PWD/data:/data ghcr.io/huggingface/text-generation-inference:0.8 --model-id tiiuae/falcon-7b-instruct
```
