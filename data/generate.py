import numpy as np

def generate_circle_data(n=2000, r=0.5, seed=42):
    np.random.seed(seed)
    X = np.random.uniform(-1, 1, size=(n, 2))
    y = (X[:, 0]**2 + X[:, 1]**2 < r**2).astype(int)
    y = y.reshape(-1, 1)
    return X, y


def generate_nestedrings_data(n=2000 ,seed=42): 
    X = np.random.uniform(-1, 1, size=(n, 2))

    r = np.sqrt(X[:, 0]**2 + X[:, 1]**2)
    r1 = np.sqrt(2) / 3
    r2 = 2 * np.sqrt(2) / 3
    y = np.zeros(n, dtype=int)
    mask_middle = (r >= r1) & (r < r2)
    y[mask_middle] = 1.0

    return X, y.reshape(-1, 1)

    