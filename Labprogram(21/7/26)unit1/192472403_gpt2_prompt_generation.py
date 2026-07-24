from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompt = input("Enter Prompt: ")
result = generator(prompt, max_new_tokens=20)

print(result[0]["generated_text"])