from module.layers import Linear 
from module.activations import ReLU, Sigmoid
class Neural_Network:
    def __init__(self,layer_sizes):
        """
        Fully connected neural network built dynamically from a list of layer sizes.
    
        Parameters
        ----------
        layer_sizes : list of int
            Example: [2, 16, 16, 1]
            Creates Linear layers between consecutive sizes.
            ReLU is applied to all hidden layers.
            Sigmoid is applied to the output layer.
        """
        self.layers = []

        for i in range(len(layer_sizes) -1):
            in_dims = layer_sizes[i]
            out_dims = layer_sizes[i+1]

            self.layers.append(Linear(in_dims,out_dims))

            if i < len(layer_sizes) -2:
                self.layers.append(ReLU()) 

            else:
                self.layers.append(Sigmoid())

