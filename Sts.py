import math

class Sts(object):
    def __init__(self):
        print("This is a customized statistic module")
        print("sts object has been created")

    
    def binom(self,p,n,k):
        """Exact probability calculation for binomial distribution i.e. P(X=k)
           p=prbability of success
           n=number of trials
           k=number of sccesses"""
        self.p=p
        self.n=n
        self.k=k
        self.q=1-self.p
        self.prob=(math.factorial(self.n)/(math.factorial(self.k)*math.factorial(self.n-self.k)))*(self.p**self.k)*(self.q**(self.n-self.k))
        print("probability of %d success=%f"%(self.k,self.prob))
        return self.prob

    def cbinom(self,p,n,k):
        """Cumulative probability calculation for binomial distribution i.e. P(X<=k)
           p=prbability of success
           n=number of trials
           k=number of sccesses"""
        self.p=p
        self.n=n
        self.k=k
        self.q=1-self.p
        self.prob=0
        for self.i in range((self.k+1)):
            self.prb=(math.factorial(self.n)/(math.factorial(self.i)*math.factorial(self.n-self.i)))*(self.p**self.i)*(self.q**(self.n-self.i))
            self.prob+=self.prb
        print("probability of less than and equal to %d success=%f"%(self.k,self.prob))
        return self.prob
    def poisson(self,lamda,X):
        """lamda=lamda usually is meu or pop mean or expected value
            X=prob that X things happen"""
        self.lamda=lamda
        self.X=X
        self.prob=((self.lamda**self.X)*(math.exp(-self.lamda)))/(math.factorial(self.X))
        print("probability that %d things happen=%f"%(self.X,self.prob))
        return self.prob
    def cpoisson(self,lamda,X):
        """lamda=lamda usually is meu or pop mean or expected value
            X=prob that X and less than X things happen"""
        self.lamda=lamda
        self.X=X
        self.prob=0
        for self.i in range((self.X+1)):
            self.prb=((self.lamda**self.i)*(math.exp(-self.lamda)))/(math.factorial(self.i))
            self.prob+=self.prb
        print("probability thatup to %d things happen=%f"%(self.X,self.prob))
        return self.prob
    

    def zscore(self,mean,std,*args):
        """calculates the z-score i.e. how much away from the mean is X per standard deviation"""
        self.mean=mean
        self.std=std
        self.args=args
        self.zlist=list()
        for self.X in self.args:
            self.z=(self.X-self.mean)/self.std
            print("Z-Score=%.2f"%self.z)
            self.zlist.append(self.z)
        return self.zlist
            
        

if __name__=="__main__":
    sts=Sts()
