import numpy as np 
class ReLU:
    def forward(self, Z):
        self.Z = Z
        return np.maximum(0, self.Z)

    def backward(self, dA):
        return dA * (self.Z > 0)
