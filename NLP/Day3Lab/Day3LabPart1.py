
#Part 1
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score


corpus = [
    "the movie was fantastic and i loved every part of it",
    "an absolute masterpiece with brilliant acting",
    "the film was boring and too long",
    "i really enjoyed the story and the visuals",
    "the plot was terrible and the acting was even worse",
    "what a wonderful experience, highly recommend",
    "not worth my time, very disappointing",
    "a truly great film, i will watch it again",
    "the script was weak and the characters were flat",
    "an amazing journey from start to finish"
]

categories = [
    "Positive", "Positive", "Negative", "Positive", "Negative",
    "Positive", "Negative", "Positive", "Negative", "Positive"
]


# Correct test set
test_corpus = [
    "the movie was great",
    "i hated the film",
    "the movie was not good",
    "the acting was not bad",
    "visually impressive but boring",
    "i wanted to like it"
]

vectorizer = CountVectorizer(ngram_range=(1, 2))

X = vectorizer.fit_transform(corpus)
X_test = vectorizer.transform(test_corpus)

print(vectorizer.get_feature_names_out())


model = MultinomialNB()
model.fit(X, categories)


predictions = model.predict(X_test)

print("\n--- PART 1: CLASSICAL MODEL RESULTS ---\n")

for sentence, sentiment in zip(test_corpus, predictions):
    print(f"Text: {sentence}")
    print(f"Predicted Sentiment: {sentiment}\n")
    