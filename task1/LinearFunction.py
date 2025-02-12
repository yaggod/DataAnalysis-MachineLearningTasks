

class LinearFunction:

    def __init__(self, k, b):
        self.k = k
        self.b = b
    
    def __call__(self, x):
        return self.k*x + self.b
    
    def FindApproximatedLinearFunction(originalX : list, originalY : list):
        k = 0
        
        xSum = sum(originalX)
        ySum = sum(originalY)
        xySum = 0
        xxSum = 0
        n = len(originalX)
        for i in range(n):
            xySum += originalX[i]*originalY[i]
            xxSum += originalX[i]**2

        k = (xSum*ySum/n - xySum)/(xSum**2/n - xxSum) 
        b = ySum/n - k*xSum/n

        return LinearFunction(k, b)