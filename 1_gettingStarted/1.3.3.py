import random
import numpy as np

# simulated annealing equation: probability = exp(-(S_old - S_new)/T), where T is the temperature
	# exp(x) is equation e^x
	# In python, this would be represented by using the numpy library: numpy.exp()

def accept_prob(S_old, S_new, T):
    # this is the acceptance "probability" in the greedy hill-climbing method
    # where new solutions are accepted if and only if they are better
    # than the old one.
    # change it to be the acceptance probability in simulated annealing
    if S_new > S_old:
        return 1.0 # new value is better than old value, so probability of getting accepted is 100%
    else:
        return (np.exp(-(S_old - S_new)/T)) # calculate chance of new solution being accepted


# the above function will be used as follows. this is shown just for
# your information; you don't have to change anything here
def accept(S_old, S_new, T):
    if random.random() < accept_prob(S_old, S_new, T):
        print(True)
    else:
        print(False)