###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    dict_cow_data = {}
    file = open(filename,'r')
    lines = file.readlines()
    
    for i in lines:
        name,weight = i.split(',')
        dict_cow_data[name] = int(weight.strip())

    file.close()
    return dict_cow_data


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    list_of_trips = []
    sorted_copy_cows = [i for j,i in sorted([(j,i) for i,j in cows.items()], reverse = True)]
    cows_count = len(sorted_copy_cows)
    cows_used = []
    while cows_count > 0:
        trip = []
        weight_per_trip = 0
        for i in sorted_copy_cows:
            if i not in cows_used:
                if weight_per_trip + cows[i] <= limit:
                    trip.append(i)
                    cows_used.append(i)
                    weight_per_trip += cows[i]
                    cows_count -= 1
        list_of_trips.append(trip)
    return list_of_trips

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    list_cow_names = list(cows.keys())
    res = []
    minimum = 10000000000000000
    for i in get_partitions(list_cow_names):
        flag = 1
        for j in i:
            weight_per_trip = 0
            for k in j:
                weight_per_trip += cows[k]
            if weight_per_trip <= limit:
                flag *= 1
            else: flag *= 0
        if flag:
            if len(i) <= minimum:
                minimum = len(i)
                res.append(i)
    return res[-1]


# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows("ps1_cow_data.txt")
    greedy_start = time.time()
    greedy_list = greedy_cow_transport(cows,10)
    greedy_end = time.time()
    print("Greedy Time : ",greedy_end - greedy_start)
    brute_start = time.time()
    brute_list = brute_force_cow_transport(cows,10)
    brute_end = time.time()
    print("Brute Force Time : ",brute_end - brute_start)
    print("********************************************************************************************")
    print("Greedy Solution : ", greedy_list , "Number Of Trips : ", len(greedy_list))
    print("********************************************************************************************")
    print("Brute Force Solution : ", brute_list , "Number Of Trips : ", len(brute_list))


if __name__ == '__main__':compare_cow_transport_algorithms()