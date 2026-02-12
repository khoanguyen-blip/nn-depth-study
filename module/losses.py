import numpy as np 


class BCE: 
    """
    Binary Cross-Entropy loss for binary classification.

    Assumes predictions come from a Sigmoid activation.
    """
    def forward(self, y_hat,y): 
        """
        Compute per-sample BCE loss.

        Parameters
        ----------
        y_hat : ndarray
            Predicted probabilities.
        y : ndarray
            Ground truth labels (0 or 1).

        Returns
        -------
        ndarray
            Per-sample loss values.
        """
        eps = 1e-8
        self.y_hat = np.clip(y_hat, eps, 1 - eps)
        self.y= y
        self.L = -(self.y*np.log(self.y_hat) + (1-self.y)*np.log(1-self.y_hat))
        return self.L 

    def backward(self): 
        """
        Compute gradient of loss w.r.t. predictions.
        """
        self.dy_hat = (1-self.y)/(1-self.y_hat) - (self.y)/(self.y_hat)
        return self.dy_hat

        