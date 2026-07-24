from nltk.tokenize import sent_tokenize
text = input("Enter the paragraph: ")
sentences = sent_tokenize(text)
print(sentences)