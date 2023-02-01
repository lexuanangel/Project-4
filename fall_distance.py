# Author: Angel Le
# GitHub username: lexuanangel
# Date: 1/31/2023
# Description: Create a function that returns the distance in meters
# of an object that is falling due to gravity

# defining fall distance formula due to gravity
def fall_distance(t):
    g = 9.8
    d = (1/2) * g * (t ** 2)
    return d


# dist = fall_distance(4.5) to be able to test
# print(round(dist, 3)) for my own testing purposes
