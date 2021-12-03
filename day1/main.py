from os import pathconf
from numpy import loadtxt

def sonar_sweep(path: str):
    depths = loadtxt(path)
    count = 0
    for i in range(len(depths) - 1):
        count += bool(depths[i+1] > depths[i])
    return count

print('part 1')
print(sonar_sweep('day1/test_input.txt'))
print(sonar_sweep('day1/input.txt'))


def sonar_sweep3(path: str):
    depths = loadtxt(path)
    count = 0
    for i in range(len(depths) - 3):
        count += bool(depths[i+3] > depths[i])
    return count

print('part 2')
print(sonar_sweep3('day1/test_input.txt'))
print(sonar_sweep3('day1/input.txt'))