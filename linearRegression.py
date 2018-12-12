import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
import pandas as pd
 
# Load CSV and columns
df = pd.read_csv("regression.csv",delimiter=',')
 
X = df['Age']
Y = df['Height']
 
X= X.values.reshape(len(X),1)
Y=Y.values.reshape(len(Y),1)
 
# Split the data into training/testing sets


X_train = X
X_test = [[0.414]]
 
# Split the targets into training/testing sets
Y_train = Y
Y_test = [[245000
,312000
,279000
,308000
,199000
,219000
,405000
,324000
,319000
,255000
]]

# Create linear regression object
linearRegression = linear_model.LinearRegression()
#gradientDescent = linear_model.SGDClassifier()
 
# Train the model using the training sets
linearRegression.fit(X_train, Y_train)
#gradientDescent.fit(X_train, Y_train)
 
# Plot outputs

 
# Plot outputs
plt.scatter(X_train, Y_train,color = "m",marker = "o")
plt.plot(X_train,Y_train,color="blue")
plt.plot(X_test, linearRegression.predict(X_test),color="red")
print (linearRegression.predict(X_test))
#plt.plot(X_test, gradientDescent.predict(X_test),color="red")
plt.title('Test Data')
plt.xlabel('Age')
plt.ylabel('Height')
plt.xticks(())
plt.yticks(())
#print (gradientDescent.predict(X_test))
plt.scatter(X_test, linearRegression.predict(X_test), color='red',linewidth=3)
#for x in range(0,100):
 #   gradientDescent.fit(X_train, Y_train)
  #  plt.scatter(X_test, gradientDescent.predict(X_test), color='violet',linewidth=3)
 
plt.show()
