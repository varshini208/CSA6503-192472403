from transformers import pipeline
generator = pipeline("text-generation", model="gpt2")
prompt = input("Enter a prompt: ")
result = generator(prompt, max_new_tokens=30)
print(result[0]["generated_text"])