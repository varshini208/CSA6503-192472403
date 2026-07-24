from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import torch
model_name = "distilbert-base-cased-distilled-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
context = input("Enter Context: ")
question = input("Enter Question: ")
inputs = tokenizer(question, context, return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)

start = torch.argmax(outputs.start_logits)
end = torch.argmax(outputs.end_logits) + 1

answer = tokenizer.convert_tokens_to_string(
    tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start:end])
)

print("Answer:", answer)