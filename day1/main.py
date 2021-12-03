from numpy import loadtxt

def sonar_sweep(depths=None):
    if not depths:
        depths = loadtxt('day1/input.txt')
    count = 0
    for i in range(len(depths) - 1):
        count += bool(depths[i+1] > depths[i])
    return count

print(sonar_sweep())

def sonar_sweep3(depths=None):
    if not depths:
        depths = loadtxt('day1/input.txt')
    count = 0
    for i in range(len(depths) - 3):
        count += bool(depths[i+3] > depths[i])
    return count

print(sonar_sweep3())

