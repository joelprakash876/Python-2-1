import numpy as np 
import numpy.linalg as linalg
import math

X=np.array([[2,4],[1,3],[0,1],[-1,0.5]])
print('\nGven Matrix is :\n{}'.format(X))
print('\nMean Values {}'.format(np.mean(X,axis=0)))


A = (X - np.mean(X, axis=0))
print('\nStandardized Matrix is :\n {}'.format(A))

VarCov=np.dot(np.transpose(A),A)/len(X)
print('\nVariance Covariance Matrix is {}'.format(VarCov))


eigenValues, eigenVectors = linalg.eig(VarCov)

idx = eigenValues.argsort()[::-1]   
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:,idx]

print('\nEigen Values are {}'.format(eigenValues))
print('\nEigen Vectors are {}'.format(eigenVectors))


s=sum(list(eigenValues))
t=[]
stoppoint=0
for i in range(np.size(eigenValues)):
    l=list(eigenValues)
    numerator=sum(l[0:i+1])
    z=(numerator/s)*100
    if z<=100:
        stoppoint=i+1
    t.append(z)
print('\nThreshold Table :\n{}'.format(t))


eigenValues=eigenValues.tolist()
eigenValues=eigenValues[0:stoppoint]
eigenVectors=eigenVectors[:,0:stoppoint]

print('\nRetained Eigen Values :\n{}'.format(eigenValues))
print('\nRetained Eigen Vectors: \n{}'.format(eigenVectors))
print('\n PCA Matrix :\n{}'.format(np.dot(X,eigenVectors)))
