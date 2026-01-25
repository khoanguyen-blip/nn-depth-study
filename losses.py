import numpy as np 

#BCE dùng log cơ số e 
class BCE: #Binary Cross Entropy, hàm này đặc biệt hợp với sigmoid vì sigmoid generate xác suất còn BCE là likelihood
    def forward(self, y_hat,y): #định nghĩa hàm loss
        eps = 1e-8
        self.y_hat = np.clip(y_hat, eps, 1 - eps)
        self.y= y
        self.L = -(self.y*np.log(self.y_hat) + (1-self.y)*np.log(1-self.y_hat))
        return self.L 

    def backward(self): #dùng cache để tính đạo hàm của y_hat 
        self.dy_hat = (1-self.y)/(1-self.y_hat) - (self.y)/(self.y_hat)
        return self.dy_hat

        