import pickle
import pandas as pd
import matplotlib.pyplot as plt
from utils import get_vectors
from predict import *
from accuracy import *
from pca import *

data = pd.read_csv('capitals.txt', delimiter=' ')
data.columns = ['city1', 'country1', 'city2', 'country2']

# print first five elements in the DataFrame
print(data.head(5))


data_X = data[['city1', 'country1', 'city2']]
data_Y = data[['country2']]

word_embeddings = pickle.load(open("word_embeddings_subset.p", "rb"))
print(word_embeddings.keys())  # there are 243 words that will be used in this assignment

print(f"Dimension: {word_embeddings['Spain'].shape[0]}\n")

cosine_similarity_test(word_embeddings) 
euclidean_distance_test(word_embeddings) 

# feel free to try different words
word1 = 'gas'
word2 = 'oil'

print(f"Cosine similarity between {word1} and {word2}: {cosine_similarity(word_embeddings[word1], word_embeddings[word2])}")
print(f"Euclidean distance between {word1} and {word2}: {euclidean(word_embeddings[word1], word_embeddings[word2])}\n")

get_country_test(word_embeddings)

prediction = predict(word_embeddings, data_X)
data_X['predicted_country2'] = prediction
print(data_X[['city2', 'predicted_country2']])

accuracy_test(prediction, data_Y)

print("Congratulations! You have completed all tasks.\n")

# Plot the word embeddings using Principal Component Analysis (PCA)
words = ['oil', 'gas', 'happy', 'sad', 'city', 'town',
         'village', 'country', 'continent', 'petroleum', 'joyful']

# given a list of words and the embeddings, it returns a matrix with all the embeddings
X = get_vectors(word_embeddings, words)

print(f'You have {len(words)} word vectors with 300 dimensions thus X.shape is: {X.shape}')

# Plot the reduced word vectors using matplotlib.
result = compute_pca(X, 2) ## 300 dims -> the most informative 2 dims
plt.scatter(result[:, 0], result[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, xy=(result[i, 0] - 0.05, result[i, 1] + 0.1))

plt.show()
