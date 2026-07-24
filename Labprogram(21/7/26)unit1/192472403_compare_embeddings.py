from transformers import BertTokenizer, BertModel

tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
model = BertModel.from_pretrained("bert-base-uncased")

s1 = input("Enter Sentence 1: ")
s2 = input("Enter Sentence 2: ")

e1 = model(**tokenizer(s1, return_tensors="pt")).last_hidden_state.shape
e2 = model(**tokenizer(s2, return_tensors="pt")).last_hidden_state.shape

print("Sentence 1 Shape:", e1)
print("Sentence 2 Shape:", e2)