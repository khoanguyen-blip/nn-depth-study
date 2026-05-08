
import numpy as np

class SGD:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.velocities = {}

    def step(self, model):

        for i, layer in enumerate(model):

            if hasattr(layer, "W"):

                if i not in self.velocities:
                    self.velocities[i] = {
                        "vW": np.zeros_like(layer.W),
                        "vb": np.zeros_like(layer.b)
                    }

                vW = self.velocities[i]["vW"]
                vb = self.velocities[i]["vb"]

                vW = self.momentum * vW - self.lr * layer.dW
                vb = self.momentum * vb - self.lr * layer.db

                layer.W += vW
                layer.b += vb

                self.velocities[i]["vW"] = vW
                self.velocities[i]["vb"] = vb

    def update_lr(
        self,
        lr_start,
        lr_end,
        epoch,
        lr_decay_epochs
    ):

        if epoch < lr_decay_epochs:
            self.lr = (
                lr_start
                - ((lr_start - lr_end)
                * (epoch / lr_decay_epochs))
            )
        else:
            self.lr = lr_end

def train(
    model,
    loss_func,
    optimizer,
    X,
    y,
    lr_start,
    lr_decay_epochs,
    lr_end,
    epochs=1000,
    batch_size=32
):

    num_samples = X.shape[0]
    loss_history = []

    for epoch in range(epochs):

        optimizer.update_lr(
            lr_start,
            lr_end,
            epoch,
            lr_decay_epochs
        )

        perm = np.random.permutation(num_samples)

        X_shuffled = X[perm]
        y_shuffled = y[perm]

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

            dA = loss_func.backward()

            for layer in reversed(model):
                dA = layer.backward(dA)

            optimizer.step(model)

    return loss_history