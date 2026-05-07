"""if global_step < epsilon_decay_steps:
                epsilon = epsilon_start - (
                    (epsilon_start - epsilon_end)
                    * (global_step / epsilon_decay_steps)
                )

import numpy as np """
"""Epoch 0–200: LR = 0.01
Epoch 200–400: LR = 0.005
Epoch 400–500: LR = 0.001""" 


def train(
    model,
    loss_func,
    X,
    y,
    lr_start,
    lr_decay_epochs,
    lr_end,
    epochs=1000,
    batch_size=32
):
    
    lr = lr_start 
    num_samples = X.shape[0]
    loss_history = []
    
    for epoch in range(epochs):
        # Chỉnh lại logic để lr chạm đúng lr_end và dừng lại ở đó
        if epoch < lr_decay_epochs:
            lr = lr_start - ((lr_start - lr_end) * (epoch / lr_decay_epochs)) 
        else:
            lr = lr_end

        perm = np.random.permutation(num_samples)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        current_batch = 0
        
        for i in range(0, num_samples, batch_size):
            Xb = X_shuffled[i:i+batch_size]
            yb = y_shuffled[i:i+batch_size]
            
            A = Xb 
            for layer in model: 
                A = layer.forward(A)
            
            y_hat = A 
            
            loss = loss_func.forward(y_hat, yb) 
            batch_loss = loss.mean()
            loss_history.append(batch_loss)
            current_batch += 1

            dA = loss_func.backward()
            
            for layer in reversed(model):
                dA = layer.backward(dA) 

            for layer in model: 
                if hasattr(layer, "W"):
                    layer.W -= lr * layer.dW 
                    layer.b -= lr * layer.db
        
    return loss_history

