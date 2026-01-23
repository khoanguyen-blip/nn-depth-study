from layers import Linear 
from activations import ReLU, Sigmoid
class Neural_Network:
    def __init__(self,layer_sizes):
        #layer_sizes sẽ là một tập các số hướng dẫn cách build các layers
        #nhớ : mọi layers trừ output đều có activation là ReLU , output có Sigmoid 
        self.layers = []

        for i in range(len(layer_sizes) -1):
            in_dims = layer_sizes[i]
            out_dims = layer_sizes[i+1]

            self.layers.append(Linear(in_dims,out_dims))

            if i < len(layer_sizes) -2:
                self.layers.append(ReLU()) 

            else:
                self.layers.append(Sigmoid())

