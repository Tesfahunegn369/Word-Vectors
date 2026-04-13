from get_country import *

# Q4: Implement predict function
def predict(word_embeddings, data):
    '''
    Input:
        word_embeddings: a dictionary where the key is a word and the value is its embedding
        data: a pandas dataframe containing all the country and capital city pairs

    Output:
        prediction: list of the predicted country
    '''

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    # initialize predictions to empty list
    prediction = []

    # loop through the rows of the dataframe
    for i, row in data.iterrows():

        # get city1
        city1 = row['city1']

        # get country1
        country1 = row['country1']

        # get city2
        city2 = row['city2']

        # use get_country to find the predicted country2
        predicted_country2, _ = get_country(city1, country1, city2, word_embeddings)

        # append the predicted country to the prediction list
        prediction.append(predicted_country2)


    ### END CODE HERE ###
    return prediction
