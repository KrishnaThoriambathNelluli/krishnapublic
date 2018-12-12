from numpy import *
import matplotlib.pyplot as plt
import numpy as np

np.seterr(invalid='warn')

def gradientCalculator(a, b, points, learningRate):
    aGradient = 0
    bGradient = 0
    M=float(len(points))
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        yp=(b * x) + a
        a = np.array(a, dtype=np.float64)
        b = np.array(b, dtype=np.float64)
        aGradient = np.array(aGradient, dtype=np.float64)
        bGradient = np.array(bGradient, dtype=np.float64)
        aGradient += - (y - ((b * x) + a))
        bGradient += - x * (y - ((b * x) + a))
        #print('aGradient='+str(aGradient))
        #print('bGradient='+str(bGradient))

    new_aGradient = np.array((a - (learningRate * aGradient)), dtype=np.float64)
    new_bGradient = np.array((b - (learningRate * bGradient)), dtype=np.float64)
    
    return [new_aGradient, new_bGradient]

def gradientFinder(points, a, b, learning_rate, num_iterations):
    for i in range(num_iterations):
        a, b = gradientCalculator(a, b, array(points), learning_rate)
        #print ('A: '+str(round(a,3))+' B: '+str(round(b,3)))
    return [a, b]

def sseCalculator(a, b, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i, 0]
        y = points[i, 1]
        yp=a+b*x
        plt.plot(x,yp,color='red')
        print ("X Mean: "+str(points[i,0])+" |  Y Mean: "+str(points[i,1])+"  |  yp="+str(round(yp,2)))
        totalError+= (y - (round(yp,2))) ** 2
        #print ('SSE:'+str(round(totalError/2,3)))
        #print (yp)
    print ("SSE: "+str(totalError/2))

def run():
    points = genfromtxt("regression.csv", delimiter=",")
    learning_rate = 0.01
    a = 0.45 
    b = 0.75
    iterations = 800
    [a, b] = gradientFinder(points, a, b, learning_rate, iterations)
    print ("After "+str(iterations)+ " iterations a = "+str(a)+", b = "+str(b))
    sseCalculator(a, b, points)
    predictHeight=a+b*1555
    #print ("Predicted Price for house size 1555: "+ str(predictHeight))
    X_test=[0,0.22,0.24,0.33,0.37,0.44,0.44,0.57,0.93,1]
    Y_test=[0,0.22,0.58,0.20,0.55,0.39,0.54,0.53,1,0.61]
    plt.scatter(X_test, Y_test,  color='black', marker = "o", s = 30)
    plt.plot(X_test, Y_test,  color='blue')
    plt.scatter(0.337, predictHeight, color='red')
    Y_pred=[0.1522811083036935,0.302707535870297,0.31638266564907913,0.3779207496535988,0.40527100921116305,0.4531339634369005,0.4531339634369005,0.5420223069989843,0.7881746430170629,0.8360375972428002]
    plt.plot(X_test,Y_pred,color='red')
    plt.title('Test Data')
    plt.xlabel('Size')
    plt.ylabel('Price')
 

    
    plt.show()
    
if __name__ == '__main__':
    run()
