import numpy as np

def generate_circle_data(n=2000, r=0.5, seed=42):
    np.random.seed(seed)
    X = np.random.uniform(-1, 1, size=(n, 2))
    y = (X[:, 0]**2 + X[:, 1]**2 < r**2).astype(int)
    y = y.reshape(-1, 1)
    return X, y

