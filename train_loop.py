import numpy as np 


def train(
    model,
    loss_func,
    X,
    y,
    epochs=1000,
    batch_size = 32,
    lr=0.01):
    
    num_samples = X.shape[0]

    for epoch in range(epochs):
        #____Shuffle____
        perm = np.random.permutation(num_samples)
        X_shuffled = X[perm]
        y_shuffled = y[perm]
        current_batch = 0
        #SGD theo batch 
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
            batch_loss = loss.mean()
            current_batch += 1

            #____backward____
            dA = loss_func.backward()
            for layer in reversed(model):
                dA = layer.backward(dA) 

            #điểm cải tiến : update bằng loop

            for layer in model: 
                if hasattr(layer, "W"):
                    layer.W -= lr*layer.dW 
                    layer.b -= lr*layer.db 


        #____logging____
        if epoch%50 == 0   :
            print("Epoch " , epoch,"|",  " loss = ", batch_loss)


