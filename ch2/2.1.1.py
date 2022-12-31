# counts the number of occurence of "11" in the string

def count11(seq):
    count = 0
   # define this function and return the number of occurrences as a number
    for i in range(len(seq)-1):
        if seq[i] == 1 and seq[i+1] == 1:
            count = count + 1
    return count


print(count11([0, 0, 1, 1, 1, 0])) # this should print 2
