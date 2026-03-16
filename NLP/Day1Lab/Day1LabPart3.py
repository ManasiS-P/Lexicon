
#Part 3
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import re


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

test_corpus = [
    "the movie was great",
    "i hated the film",
    "a boring and bad story",
    "absolutely loved it"
]

def clean_text(text):
    
    text = text.lower()                 
    
    text = re.sub(r'[^a-z\s]', '', text) 
    
    return text

clean_corpus = [clean_text(text) for text in corpus]
clean_test = [clean_text(text) for text in test_corpus]

vectorizer = CountVectorizer(stop_words="english")

X = vectorizer.fit_transform(clean_corpus)

X_test = vectorizer.transform(clean_test)

print(vectorizer.get_feature_names_out())
print(X.toarray())

model = SVC(kernel="linear")
model.fit(X, categories)

predictions = model.predict(X_test)
print("\nPredictions:\n")

for sentence, sentiment in zip(test_corpus, predictions):
    print(sentence, "->", sentiment)

true_labels = ["Positive", "Negative", "Negative", "Positive"]
accuracy = accuracy_score(true_labels, predictions)
print("\nAccuracy:", accuracy)


#Explaination for whether the result improved or not
# In this experiment, several improvements were tested, including cleaning the text, removing stop words, and using an SVC classifier instead of the Naive Bayes model. 
# However, the overall accuracy remained the same for both models on the test dataset.
# This is likely because the dataset used in the lab is very small, containing only ten training reviews and four test sentences. 
# With such a limited dataset, both models are able to easily learn the patterns needed to classify the test sentences correctly, resulting in the same accuracy.