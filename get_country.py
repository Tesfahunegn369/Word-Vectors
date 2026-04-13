from cosine_similarity import *
from euclidean_distance import *

# Q3: Implement get_country function (30 pts)
def get_country(city1, country1, city2, word_embeddings):
    """
    Input:
        city1: a string (the capital city of country1)
        country1: a string (the country of capital1)
        city2: a string (the capital city of country2)
        embeddings: a dictionary where the keys are words and values are their embeddings
    Output:
        countries: a dictionary with the most likely country and its similarity score
    """
    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    # store the city1, country 1, and city 2 in a set called group
    group = {city1, country1, city2}

    # get embeddings of city 1
    city1_emb = word_embeddings[city1]

    # get embedding of country 1
    country1_emb = word_embeddings[country1]

    # get embedding of city 2
    city2_emb = word_embeddings[city2]

    # get embedding of country 2 (it's a combination of the embeddings of country 1, city 1 and city 2)
    # Remember: King - Man + Woman = Queen
    vec = country1_emb - city1_emb + city2_emb

    # Initialize the similarity to -1 (it will be replaced by a similarities that are closer to +1)
    similarity = -1

    # initialize country to an empty string
    country = ''

    # loop through all words in the embeddings dictionary
    for word in word_embeddings.keys():

        # first check that the word is not already in the 'group'
        if word not in group:

            # get the word embedding
            word_emb = word_embeddings[word]

            # calculate cosine similarity between embedding of country 2 and the word in the embeddings dictionary
            cur_similarity = cosine_similarity(vec, word_emb)

            # if the cosine similarity is more similar than the previous best similarity...
            if cur_similarity > similarity:

                # update the similarity to the new, better similarity
                similarity = cur_similarity

                # store the country as a tuple, which contains the word and the similarity
                country = (word, similarity)

    ### END CODE HERE ###

    return country

def get_country_test(word_embeddings):
    # Testing your function
    print("Q3: Implement get_country function (30 pts)")

    country_cairo = get_country('Athens', 'Greece', 'Cairo', word_embeddings)
    if country_cairo[0] == 'Egypt' and abs(country_cairo[1] - 0.7626) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    country_tokyo = get_country('Athens', 'Greece', 'Tokyo', word_embeddings)
    if country_tokyo[0] == 'Japan' and abs(country_tokyo[1] - 0.7413) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    print('')