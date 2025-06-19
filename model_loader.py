from dotenv import load_dotenv
import os
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline
import torch

# Load Hugging Face token
load_dotenv()
hf_api_key = os.getenv("HUGGINGFACE_API_KEY")

# model
model_id = "google/flan-t5-base"

device = 0 if torch.cuda.is_available() else -1
print(f"💻 Running on {'GPU' if device == 0 else 'CPU'}")

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

pipe = pipeline(
    "text2text-generation",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,
    device=device
)

class SimpleWrapper:
    def __init__(self, pipeline):
        self.pipeline = pipeline

    def invoke(self, prompt):
        result = self.pipeline(prompt)
        return result[0]["generated_text"].strip()

rf = SimpleWrapper(pipe)
