from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from gensim.models import Word2Vec
from gensim.models.keyedvectors import KeyedVectors
import numpy as np

# Обработка текста
with open("/mnt/data/Стругацкие Тестовая_2 вместе.txt", "r", encoding="utf-8") as file:
    text_data = file.read()

# Векторизация Bag-of-Words
vectorizer_bow = CountVectorizer(max_features=100)
bow_matrix = vectorizer_bow.fit_transform([text_data])

# Векторизация TF-IDF
vectorizer_tfidf = TfidfVectorizer(max_features=100)
tfidf_matrix = vectorizer_tfidf.fit_transform([text_data])

# Подготовка текста для word2vec (разбиение на предложения и токены)
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import string
nltk.download('punkt')

sentences = sent_tokenize(text_data.lower())
tokenized_sentences = [
    [word for word in word_tokenize(sent) if word.isalpha()] for sent in sentences
]

# Обучим модель Word2Vec (CBOW и Skip-gram для сравнения)
w2v_cbow = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=2, sg=0, epochs=10)
w2v_skipgram = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=2, sg=1, epochs=10)

# Получим усредненный вектор текста
def get_avg_vector(model, tokenized_sentences):
    vectors = []
    for sentence in tokenized_sentences:
        for word in sentence:
            if word in model.wv:
                vectors.append(model.wv[word])
    if vectors:
        return np.mean(vectors, axis=0)
    else:
        return np.zeros(model.vector_size)

avg_vec_cbow = get_avg_vector(w2v_cbow, tokenized_sentences)
avg_vec_skipgram = get_avg_vector(w2v_skipgram, tokenized_sentences)

# Соберем результаты
results = {
    "BoW features shape": bow_matrix.shape,
    "TF-IDF features shape": tfidf_matrix.shape,
    "CBOW avg vector shape": avg_vec_cbow.shape,
    "Skip-gram avg vector shape": avg_vec_skipgram.shape,
    "CBOW avg vector (preview)": avg_vec_cbow[:5],
    "Skip-gram avg vector (preview)": avg_vec_skipgram[:5]
}

results
