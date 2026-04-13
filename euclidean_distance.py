import numpy as np
def euclidean(A, B):
    """
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        d: numerical number representing the Euclidean distance between A and B.
    """
    # euclidean distance
    d = np.linalg.norm(A - B)

    return d

def euclidean_distance_test(word_embeddings):
    # Testing your function
    print("Implement Euclidean distance function")
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
