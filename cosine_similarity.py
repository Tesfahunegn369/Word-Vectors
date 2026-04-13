import numpy as np

# Q1: Implement cosine similarity function (10 pts)
def cosine_similarity(A, B):
    '''
    Input:
        A: a numpy array which corresponds to a word vector
        B: A numpy array which corresponds to a word vector
    Output:
        cos: numerical number representing the cosine similarity between A and B.
    '''

    ### START CODE HERE (REPLACE INSTANCES OF 'None' with your code) ###

    dot = np.dot(A, B)
    norma = np.linalg.norm(A)
    normb = np.linalg.norm(B)
    cos = dot / (norma * normb)

    ### END CODE HERE ###
    return cos

def cosine_similarity_test(word_embeddings):
    # Testing your function
    print("Q1: Implement cosine similarity function (10 pts)")
    if cosine_similarity(np.array([1, 0]), np.array([0, 1])) == 0.0:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    if cosine_similarity(np.array([0.1, 0.3]), np.array([-0.1, -0.3])) == -1.0:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    comp = cosine_similarity(word_embeddings['king'], word_embeddings['queen'])
    if abs(comp - 0.6510) < 0.001:
        print('SUCCESS')
    else:
        print('FAIL')
        exit(1)

    print('')

