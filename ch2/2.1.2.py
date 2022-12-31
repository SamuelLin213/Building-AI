# Print out conditional probability of each nationality
# Winner works in fishing industry

def main():
    countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
    populations = [5615000, 5439000, 324000, 5080000, 9609000]
    fishers = [1891, 2652, 3800, 11611, 1757]

    total_fishers = sum(fishers)
    total_population = sum(populations)

    # write your solution here

    for country, population, fisher in zip(countries, populations, fishers):
        print("%s %.2f%%" % (country, fisher/total_fishers*100)) # modify this to print correct results

main()
