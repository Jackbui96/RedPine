import pandas as pd
from datasets import Dataset
from transformers import (
    AutoModelForSeq2SeqLM, AutoTokenizer,
    TrainingArguments, Trainer
)

# Load CSV
df = pd.read_csv("Sample_Customer_Support_Training_Dataset.csv")
df["input"] = df["instruction"].astype(str)
df["output"] = df["response"].astype(str)
df = df[["input", "output"]]

# Hugging Face Dataset
dataset = Dataset.from_pandas(df)
dataset = dataset.train_test_split(test_size=0.1)

# Load model
model_name = "google/flan-t5-small"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name, from_tf=False)

# Tokenize
def preprocess(example):
    model_input = tokenizer(example['input'], truncation=True, padding="max_length", max_length=256)
    with tokenizer.as_target_tokenizer():
        labels = tokenizer(example['output'], truncation=True, padding="max_length", max_length=256)
    model_input["labels"] = labels["input_ids"]
    return model_input

tokenized_ds = dataset.map(preprocess, batched=True)

# Training args
training_args = TrainingArguments(
    output_dir="./models",
    learning_rate=2e-5,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    num_train_epochs=2,
    weight_decay=0.01,
    eval_strategy="epoch",
    save_strategy="epoch",
    logging_dir="./logs",
    logging_steps=10,
    load_best_model_at_end=True,
    fp16=False                          # disable AMP for GTX 960
)

# Train
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_ds["train"],
    eval_dataset=tokenized_ds["test"],
    tokenizer=tokenizer,
)
trainer.train()

# Save
trainer.save_model("./models/customer-support-llm")
tokenizer.save_pretrained("./models/customer-support-llm")
