
# Q5: Implement accuracy function (50 pts)
def get_accuracy(prediction, data):
    '''
    Input:
        prediction: list of the predicted countries
        data: a pandas dataframe containing all the country and capital city pairs

    Output:
        accuracy: the accuracy of the model
    '''

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###
    # initialize num correct to zero
    num_correct = 0

    # loop through the rows of the dataframe
    for i, row in data.iterrows():
        # get country2
        country2 = row['country2']

        # if the predicted country2 is the same as the actual country2...
        if prediction[i] == country2:
            # increment the number of correct by 1
            num_correct += 1

    # get the number of rows in the data dataframe (length of dataframe)
    m = len(data)

    # calculate the accuracy by dividing the number correct by m
    accuracy = num_correct / m

    ### END CODE HERE ###
    return accuracy

def accuracy_test(prediction, data_Y):
    # Testing your function
    print("Q4-5: Implement predict and accuracy function (50 pts)")
    accuracy = get_accuracy(prediction, data_Y)
    print(f"Accuracy is {accuracy:.2f}")

    if abs(accuracy - 0.919) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    print('')




