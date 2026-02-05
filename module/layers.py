import numpy as np

class Linear:
    def __init__(self, in_dims, neurons_num):
        self.in_dims = in_dims
        self.neurons_num = neurons_num
        #He initialization
        W = np.random.randn(in_dims,neurons_num)*np.sqrt(2/in_dims)
        b = np.zeros((1,neurons_num))
        self.W = W 
        self.b = b

    def forward(self, X):
        self.X = X
        
        return X @ self.W + self.b

    def backward(self, dZ):
        self.dW = self.X.T @ dZ
        self.db = dZ.sum(axis=0,keepdims=True)
        return dZ @ self.W.T


