import numpy as np 
import numpy.linalg as linalg
import math

X=np.array([[3,6,5],[7,3,3],[10,9,8],[3,9,7],[10,6,5]])
print('\nGven Matrix is :\n{}'.format(X))
print('\nMean Values {}'.format(np.mean(X,axis=0)))
print('\nStandard Deviation values are {}'.format((np.std(X,axis=0)*math.sqrt(len(X)/(len(X)-1)))))

A = (X - np.mean(X, axis=0))/(np.std(X,axis=0)*math.sqrt(len(X)/(len(X)-1)))
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
for i in range(np.size(eigenValues)):
    l=list(eigenValues)
    numerator=sum(l[0:i+1])
    z=(numerator/s)*100
    if z<95:
        stoppoint=i+1
    t.append(z)
print('\nThreshold Table :\n{}'.format(t))


eigenValues=eigenValues.tolist()
eigenValues=eigenValues[0:stoppoint]
eigenVectors=eigenVectors[:,0:stoppoint]

print('\nRetained Eigen Values :\n{}'.format(eigenValues))
print('\nRetained Eigen Vectors: \n{}'.format(eigenVectors))



f1=eigenVectors[:,0]*math.sqrt(eigenValues[0])
f2=eigenVectors[:,1]*math.sqrt(eigenValues[1])
print('\nFactor Loadings are :')
for i in range(len(f1)):
    print("{} {}".format(f1[i],f2[i]))
    
Z=np.array([f1,f2])

angle=int(input('\nEnter the angle of rotation:'))
angle=math.radians(angle)
TransMat=np.array([[math.cos(angle),-math.sin(angle)],[math.sin(angle),math.cos(angle)]])
print('\nTransformation Matrix is \n{}'.format(TransMat))
print('\nEstimated actor Loadings is \n{}'.format(np.transpose(np.dot(TransMat,Z))))
