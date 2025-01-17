import numpy as np


# kPCA
def kPCA(K):
    """
    Function to perform a kernel PCA (kPCA).

    Input:
    ------
    K : np.array (N, N)
        Kernel matrix for which you want to
        perform a kPCA

    Returns:
    --------
    x1 : np.array, (N)
        PC1
    x2 : np.array, (N)
        PC2
    x3 : np.array, (N)
        PC3
    v_sort : np.array, (3)
        Three highest eigenvalues that
        correspond to PC1, PC2 and PC3
    """
    # centralize K - this is the equivalent of the mean shift
    one = 1.0/K.shape[0] * np.ones((K.shape[0], K.shape[1]))
    KK = K - np.matmul(one, K) - np.matmul(K, one) + np.linalg.multi_dot([one, K, one])

    # compute eigenvectors
    v, F = np.linalg.eigh(KK)

    # Sort eigenvalues to get the largest ones
    idx = np.argsort(v)[::-1]
    # coordinates are projections along first two eigenvectors
    x1 = np.matmul(-K, F[:, idx[0]])
    x2 = np.matmul(-K, F[:, idx[1]])
    x3 = np.matmul(-K, F[:, idx[2]])

    # Join three highest eigenvalues together in an array
    v_sort = v[idx[:3]]
    return x1, x2, x3, v_sort
