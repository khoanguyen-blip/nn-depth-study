import numpy as np

class Linear:
    def __init__(self, in_dims, neurons_num):
        self.in_dims = in_dims
        self.neurons_num = neurons_num

    def forward(self, X):
        self.X = X
        return X @ self.W + self.b

    def backward(self, dZ):
        self.dW = self.X.T @ dZ
        self.db = dZ.sum(axis=0,keepdims=True)
        return dZ @ self.W.T


class ReLU:
    def forward(self, Z):
        self.Z = Z
        return np.maximum(0, self.Z)

    def backward(self, dA):
        return dA * (self.Z > 0)
