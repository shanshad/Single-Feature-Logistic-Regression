import numpy as np

X = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6]
])
Y=y = np.array([
    [0],
    [0],
    [0],
    [0],
    [1],
    [1],
])
m=X.shape[0]
Xn = np.hstack([np.ones((m,1)), X])
theta=np.zeros((Xn.shape[1],1))
alpha=0.1
def yhat(Xn,theta):
    Yhat=1/(1+np.exp(-(Xn@theta)))
    return Yhat
def cost(Xn,Y,theta):
    cost=0
    Yhat=yhat(Xn,theta)
    for i in range(m):
        cost+=((np.multiply(Y[i],np.log(Yhat[i]))+np.multiply((1-Y[i]),np.log(1-Yhat[i]))))
    return -(cost/m)
def gradient(Xn,theta):
    Yhat=yhat(Xn,theta)
    err=Yhat-Y
    gr=(Xn.T@err)/m
    return gr
prev_cost=cost(Xn,Y,theta)
for i in range(1000):
    theta=theta-alpha*gradient(Xn,theta)
    current_cost=cost(Xn,Y,theta)
    if abs(prev_cost.item()-current_cost.item())< 1e-6:
        print(i)
        break
    prev_cost=current_cost
print(f"the coefficients are {theta} ")
def prediction(x):
     k=(1/(1+np.exp(-(theta[0].item()+x*theta[1].item()))))
     print("the probability of input being in class 1 is :",k)
     if k>=0.5:
         print("since probability is more than or equals to 0.5 it is positive class ")
     else:
         print("since probability is less than 0.5 it is negative class ")
s=0
print("we have divided data into two classes, positive class and negative class"
      "\nwe will be predicting the probability of the given input being positive class  ")
print(f"from the given data the trsnsition almost occurs at x= {round(-(theta[0].item()/theta[1].item()),2)}")
while s==0:
    x=float(input("Enter a number: "))
    prediction(x)
    s=int(input("Enter 0 to predict more and 1 to exit : "))