import random

def main():
    prob = 0.80 # 80% chance
    if random.random() < prob: # random.random() generates num between 0 and 1
        print('dog')
    else:
        print('cat')

main()
