import numpy as np 


def train(
    model,
    loss_func,
    X,
    y,
    epochs=1000,
    batch_size = 32,
    lr=0.01):
    """
    Mini-batch SGD training loop.
    
    Returns
    -------
    list of float
        Batch-wise loss values across training.
    """

    num_samples = X.shape[0]
    loss_history = []
    for epoch in range(epochs):
        
        perm = np.random.permutation(num_samples)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        current_batch = 0
        
        for i in range(0,num_samples,batch_size):
            Xb = X_shuffled[i:i+batch_size]
            yb = y_shuffled[i:i+batch_size]
            
            A = Xb 
            for layer in model: 
                A = layer.forward(A)
            
            y_hat = A 
            
            
            loss = loss_func.forward(y_hat ,yb) 
            batch_loss = loss.mean()
            loss_history.append(batch_loss)
            current_batch += 1

            
            dA = loss_func.backward()
            
            for layer in reversed(model):
            
                dA = layer.backward(dA) 

            
           

            for layer in model: 
                if hasattr(layer, "W"):
                    layer.W -= lr*layer.dW 
                    layer.b -= lr*layer.db

                
                

        
    return loss_history

def show_loss(epochs_loss,step = 50): 
    for i in range(0,len(epochs_loss),step): 
        print("EPOCHS :" ,i,"| LOSS: ",epochs_loss[i])
