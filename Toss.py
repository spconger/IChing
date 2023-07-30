import random

class CoinToss:
    def __init__(self):
        self.total=0

    def toss(self):
        num = random.randint(0,1)
        return num
    
    #the problem with the tossResult is that 
    # 6 and 9 are rarer than thye should be
    # How do I compensate for that, so that they are
    # not too common, but not too rare
    
    def tossResult(self):
        self.total=0
        subtotal=0
        for i in range(1,4):
            value=0
            value = self.toss()
           
            if value==1:
                value=3
            else:
               value=2
            subtotal += value
        self.total=subtotal
        

    def getTotal(self):
        return self.total
        
