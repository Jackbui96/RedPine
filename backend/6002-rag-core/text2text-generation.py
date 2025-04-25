from transformers import pipeline

# Load model and tokenizer from your local directory
pipe = pipeline(
    "text2text-generation",
    model="./finetune-hf/models/customer-support-llm",
    tokenizer="./finetune-hf/models/customer-support-llm"
)

# Run inference
prompt = "i want to cancel my order #12345"
output = pipe(prompt, max_length=100, do_sample=False)

print("🧠 Response:", output[0]["generated_text"])

# Run inference
prompt = "i want to know why my order is too late?"
output = pipe(prompt, max_length=100, do_sample=False)

print("🧠 Response:", output[0]["generated_text"])
