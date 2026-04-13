import numpy as np

# Q2: Implement Euclidean distance function (10 pts)
def euclidean(A, B):
    """
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        d: numerical number representing the Euclidean distance between A and B.
    """

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    # euclidean distance
    d = np.linalg.norm(A - B)

    ### END CODE HERE ###

    return d

def euclidean_distance_test(word_embeddings):
    # Testing your function
    print("Q2: Implement Euclidean distance function (10 pts)")
    if abs(euclidean(np.array([0, 0]), np.array([1, 1])) - np.sqrt(2.0)) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    king = word_embeddings['king']
    queen = word_embeddings['queen']
    if abs(euclidean(king, queen) - 2.4796) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    print('')