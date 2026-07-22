from transformers import pipeline
sentiment = pipeline("sentiment-analysis")
sentence = input("Enter a sentence: ")
output = sentiment(sentence)
print("Result:")
print(output)