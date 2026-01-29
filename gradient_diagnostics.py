from layers import Linear  
import numpy as np 
#mục tiêu : tạo ra hàm gradient_norm(model)

def gradient_norm(model):
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
    
    num_samples = X.shape[0]
    epochs_norms = []
    for epoch in range(epochs):
        #____Shuffle____
        perm = np.random.permutation(num_samples)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        
        #SGD theo batch 
        batch_norms = []
        for i in range(0,num_samples,batch_size):
            Xb = X_shuffled[i:i+batch_size]
            yb = y_shuffled[i:i+batch_size]
            
            #____Forward____
            A = Xb 
            for layer in model: 
                A = layer.forward(A)
            
            y_hat = A 
            
            #____Loss____
            loss = loss_func.forward(y_hat ,yb) #cái này đang là 1 vector
            
            
            

            #____backward____
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




        
        
    