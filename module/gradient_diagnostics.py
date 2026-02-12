from module.layers import Linear  
import numpy as np 


def gradient_norm(model):
    """
    Compute L2 norm of weight gradients across all trainable layers.
    """
    sum_square = 0 
    for layer in model: 
        if hasattr(layer,"dW"):
            sum_square += np.sum((layer.dW)**2)
    return sum_square**(1/2)

def training_norm(
    model,
    loss_func,
    X,
    y,
    epochs=1000,
    batch_size = 32,
    lr=0.001):
    """
    Train model and record mean gradient norm per epoch.
    Returns
    -------
    list of float
        Mean gradient norm for each epoch.
    """
    num_samples = X.shape[0]
    epochs_norms = []
    for epoch in range(epochs):
        
        perm = np.random.permutation(num_samples)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        
        
        batch_norms = []
        for i in range(0,num_samples,batch_size):
            Xb = X_shuffled[i:i+batch_size]
            yb = y_shuffled[i:i+batch_size]
            
            
            A = Xb 
            for layer in model: 
                A = layer.forward(A)
            
            y_hat = A 
            
            
            loss = loss_func.forward(y_hat ,yb) 
            
            
            

            
            dA = loss_func.backward()
            
            for layer in reversed(model):
            
                dA = layer.backward(dA) 

            batch_norms.append(gradient_norm(model))

            for layer in model: 
                if hasattr(layer, "W"):
                    layer.W -= lr*layer.dW 
                    layer.b -= lr*layer.db

                
        epochs_norms.append(np.mean(batch_norms))

    return epochs_norms         



    


        

        
        
    