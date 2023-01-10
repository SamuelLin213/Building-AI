# input values for three mökkis: 
#  - size [m^2], 
#  - size of the sauna [m^2], 
#  - distance to water [m], 
#  - number of indoor bathrooms, 
#  - proximity of neighbors [m]
X = [[66, 5, 15, 2, 500], 
     [21, 3, 50, 1, 100], 
     [120, 15, 5, 2, 1200]]

# coefficient values
c = [3000, 200 , -50, 5000, 100]

def predict(X, c):
    # write a loop that goes over the cabin data and for each cabin prints out 
    # the predicted price of the cabin you can assume that the number of inputs
    # and the number of coefficients are the same
    for i in range(len(X)):
        price = c[0]*X[i][0] + c[1]*X[i][1] + c[2]*X[i][2] + c[3]*X[i][3] + c[4]*X[i][4] # use linear regression formula to get sum of x*c

        print(price)

predict(X, c)
