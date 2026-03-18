
# PART 2 — HUGGING FACE MODEL
from transformers import pipeline


sentiment = pipeline("sentiment-analysis")

print("\n--- PART 2: HUGGING FACE RESULTS ---\n")


test_sentences = [
    "the movie was great",
    "i hated the film",
    "the movie was not good",
    "the acting was not bad",
    "visually impressive but boring",
    "i wanted to like it"
]

for text in test_sentences:
    result = sentiment(text)[0]

    print(f"Text: {text}")
    print(f"Predicted Sentiment: {result['label']}, Score: {result['score']:.4f}\n")
