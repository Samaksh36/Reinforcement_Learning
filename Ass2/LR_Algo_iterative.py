import numpy as np


labels=[]
features=[]

m= 500
n=3
lr=0.000000005

for i in range(m):
    features.append([])
    features[i].append(1)
    for j in range(1,n+1):       
        features[i].append(np.random.randint(1,10))

for i in range(m):
    labels.append((features[i][0])+(5*features[i][1])- (2*features[i][2])+(3*features[i][3]))

theeta=np.zeros(n+1)

# print(features)
# print()
# print(labels)
# print()

###########################################
H=[]
for ite in range(5000):
    

    for i in range(m):
        
        h=0
        for j in range(n+1):
            h= h+ (features[i][j]*theeta[j])

        H.append(h)
        
        
    for j in range(n+1):
        s=0
        for i in range(m):
            s= s+  (  (H[i]-labels[i])* features[i][j] )

        theeta[j]= theeta[j]- (lr*s) 
            
print('_____________________________________')
print(theeta)


predict=[]
for i in range(m):
    pred=0
    for j in range(n+1):
        pred= pred+(theeta[j]* features[i][j])

    predict.append(int(pred))

print()
print([1,5,-2,3])
print()
dif=[]
for x in range(len(predict)):
    dif.append(abs(predict[x]-labels[x]))

print(dif)