import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#read data
path='C:\\Users\\sfahg\\OneDrive\\Desktop\\Bioinformatis\\Machine learning\\Assignment 1\\diabetic_kidney_disease.csv'
data=pd.read_csv(path)
data['FBG (mg/dL)']=(data['FBG (mg/dL)']-data['FBG (mg/dL)'].min())/(data['FBG (mg/dL)'].max()-data['FBG (mg/dL)'].min())
data['UACR (mg/g creatinine)']=(data['UACR (mg/g creatinine)']-data['UACR (mg/g creatinine)'].min())/(data['UACR (mg/g creatinine)'].max()-data['UACR (mg/g creatinine)'].min())
data.plot(kind='scatter',x='FBG (mg/dL)',y='UACR (mg/g creatinine)',figsize=(7,5))

#adding a new column called ones before the data
data.insert(0,'Ones',1)

#seperate X (training data) from y (target variable )
cols=data.shape[1]
X=data.iloc[ :91 ,0:2]
y=data.iloc[ :91,cols-1:cols]

X_test=data.iloc[91:,0:2]
y_test=data.iloc[91:,cols-1:cols]

#Convert from data frames to numpy matrices
X=np.matrix(X.values)
X_test=np.matrix(X_test.values)

y=np.matrix(y.values)
y_test=np.matrix(y_test.values)


theta=np.matrix(np.array([0,0]))    
print(theta)            

#cost function
def ComputeCost(X,y,theta):
    z=np.power(((X*theta.T)-y),2)
    return np.sum(z)/(2*len(X))

#gradientDescent function
def GradientDescent(X,y,theta,alpha,iters):
    temp=np.matrix(np.zeros(theta.shape))
    parameters=int(theta.ravel().shape[1])
    cost= np.zeros(iters)
    
    for i in range(iters):
        error=(X * theta.T)-y
        for j in range(parameters):
            term=np.multiply(error,X[:,j])
            temp[0,j]=temp[0,j]-((alpha/len(X))*np.sum(term))
        theta=temp
        cost[i]=ComputeCost(X,y,theta)
        #print(cost[i])
    return theta,cost



#initialize variables for learning rate and iterations
alpha=0.1
iters=1000

x=np.linspace(data['FBG (mg/dL)'].min(),data['FBG (mg/dL)'].max(),100)
f=theta[0,0]+(theta[0,1] * x)

#draw the line
fig,ax=plt.subplots(figsize=(7,5))
ax.plot(x,f,'r',label='Prediction')
ax.scatter(data['FBG (mg/dL)'],data['UACR (mg/g creatinine)'],label='Trianing Data')

#preform gradientDescent to 'fit' the model parameters 
g,cost=GradientDescent(X, y, theta, alpha, iters)


#get best fit line 
x=np.linspace(data['FBG (mg/dL)'].min(),data['FBG (mg/dL)'].max(),100)
f=g[0,0]+(g[0,1] * x)

#draw the line
fig,ax=plt.subplots(figsize=(7,5))
ax.plot(x,f,'r',label='Prediction')
ax.scatter(data['FBG (mg/dL)'],data['UACR (mg/g creatinine)'],label='Trianing Data')
ax.legend(loc=2)
ax.set_xlabel('FBG (mg/dL)')
ax.set_ylabel('UACR (mg/g creatinine)')

ax.set_title('Predicted UACR (mg/g creatinine) vs. FBG (mg/dL)')

#draw error graph
fig,ax=plt.subplots(figsize=(7,5))
ax.plot(np.arange(iters),cost,'r')
ax.set_xlabel('Iteration')
ax.set_ylabel('Cost')
ax.set_title('Error vs Training Data')

#Calculate Y_predict 
def Calc_y_predict (theta,X_test):
    return (X_test*theta.T)

print("The value of Y_predict of X_test :")
print(Calc_y_predict(g, X_test))