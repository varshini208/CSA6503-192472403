from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

p1 = input("Enter Prompt 1: ")
p2 = input("Enter Prompt 2: ")

print("\nResponse 1:")
print(generator(p1, max_new_tokens=20)[0]["generated_text"])

print("\nResponse 2:")
print(generator(p2, max_new_tokens=20)[0]["generated_text"])