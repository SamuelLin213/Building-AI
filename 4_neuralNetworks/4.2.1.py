# trained simple neural network with larger set of cabin price data
	# predicts price of cabin based on attributes of cabin
# input layer contains 5 nodes
# first hidden layer contains 2 nodes
# second hidden layer contains 2 nodes
# output layer contains 1 node
# there's a single bias node for each hidden layer and the output layer

# Uses weights of trained network to perform "foward pass" 
	# runs input variables through neural network to obtain output
import numpy as np

# set of weights for input layer
w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
                              [-2.75768443e-01,  3.43724167e-01],
                   [ 2.29138536e+01,  3.91783025e-01],
                   [-1.22397711e-02, -1.03029800e+00]])

# set of weights for hidden layer 1
w1 = np.array([[11.5631751 , 11.87043684],
                   [-0.85735419,  0.27114237]])

# set of weights for hidden layer 2
w2 = np.array([[11.04122165],
                   [10.44637262]])

# biases for each layer(note how biases are applied after
# linear combination of current layer is computed
b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

# input values(each array of size 5 is one input layer)
x = np.array([[111, 13, 12, 1, 161],
                 [125, 13, 66, 1, 468],
                 [46, 6, 127, 2, 961],
                 [80, 9, 80, 2, 816],
                 [33, 10, 18, 2, 297],
                 [85, 9, 111, 3, 601],
                 [24, 10, 105, 2, 1072],
                 [31, 4, 66, 1, 417],
                 [56, 3, 60, 1, 36],
                 [49, 3, 147, 2, 179]])
# expected output?
y = np.array([335800., 379100., 118950., 247200., 107950., 266550.,  75850.,
                93300., 170650., 149000.])

# rectified linear unit(ReLu): returns either input or 0, whichever is largest
def hidden_activation(z):
    temp = [] # temporary array to store new values
    for x in range(len(z)): # loop through each element in input z
        if z[x] > 0: # if current element is greater than 0, append it
            temp.append(z[x])
        else: # any negative value is converted to 0
            temp.append(0)

    return np.asarray(temp) # convert temp array back to np.array() and return

def output_activation(z): # returns input as output
    return z

# input test cases
x_test = [[72, 2, 25, 3, 450], [60, 3, 15, 1, 300], [74, 5, 10, 2, 100]]

# loops through every input array
for item in x_test:
    h1_in = np.dot(item, w0) # this calculates the linear combination of inputs and weights for input layer
    h1_in[0] = h1_in[0] + b0[0] # add bias to first node in hidden layer 1
    h1_in[1] = h1_in[1] + b0[1] # add bias to second node in hidden layer 2
    h1_out = hidden_activation(h1_in) # apply activation function

    h2_in = np.dot(h1_out, w1) # the output of the previous layer is the input for hidden layer 1.
    h2_in[0] = h2_in[0] + b1[0] # add bias to first node in hidden layer 2
    h2_in[1] = h2_in[1] + b1[1] # add bisa to second node in hidden layer 2
    h2_out = hidden_activation(h2_in) # apply activation function

    out_in = np.dot(h2_out, w2) + b2[0] # calcs linear combination of inputs and weights of hidden layer 2
    				# note how we only need to bias of dim 1
    out = output_activation(out_in) # apply activation function
    print(out) # prints expected outputs
