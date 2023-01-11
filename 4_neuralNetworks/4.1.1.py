# use logistic regression to calculate the predicted output value
	# linear formula: summation of coefficients * x[index]
	# logistic activation formula(sigmoid): s(z) = 1 / (1 + exp(-x))

import math
import numpy as np

x = np.array([4, 3, 0])
c1 = np.array([-.5, .1, .08])
c2 = np.array([-.2, .2, .31])
c3 = np.array([.5, -.1, 2.53])

def sigmoid(x):
	return 1 / (1 + math.exp(-x)) # returns logistic activation formula
				      # on every sum(linear formula)

# calculate the output of the sigmoid for x with all three coefficients
# initialize sum vars for each coefficient array
sum1 = 0
sum2 = 0
sum3 = 0
for xInd in range(len(x)): # loop through each index in x array
    sum1 = sum1 + (x[xInd] * c1[xInd]) # add in x[ind] * coeff[ind]
    sum2 = sum2 + (x[xInd] * c2[xInd])
    sum3 = sum3 + (x[xInd] * c3[xInd])

print(sigmoid(sum1)) # print out result of sigmoid func on sum
print(sigmoid(sum2))
print(sigmoid(sum3))
