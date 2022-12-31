# want to list out all possible routes between the ports in portnames array

def main():
    portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]

    # use brute force to iterate and print all combinations
    port1 = 0
    for port2 in range(1, 5):
        for port3 in range(1, 5):
            for port4 in range(1, 5):
                for port5 in range(1, 5):
                    route = [port1, port2, port3, port4, port5]

                    # Modify this if statement to check if the route is valid
                    if(0 in route and 1 in route and 2 in route and 3 in route and 4 in route):
                        # do not modify this print statement
                        print(' '.join([portnames[i] for i in route]))

main()
