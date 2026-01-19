import numpy as np 
class ReLU:
    def forward(self, Z):
        self.Z = Z
        return np.maximum(0, self.Z)

    def backward(self, dA):
        return dA * (self.Z > 0)
#cấu trúc chung của các activations : forward là định nghĩa toán học, backward là tính dL/dZ = dL/dA *dA/dZ(cũng chính là đạo hàm activation)

class Sigmoid:
    def forward(self,Z): 
        self.A = 1/(1 + np.exp(-Z) )
        return self.A

    def backward(self,dA): 
        return dA*self.A*(1-self.A)