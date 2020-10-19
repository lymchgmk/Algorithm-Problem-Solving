import sys
import math
sys.stdin = open('3053_택시 기하학.txt', 'rt')


def euclid_geometry(R):
    return math.pi * R**2


def taxi_cab_geometry(R):
    return 2 * R**2


R = int(input())
print(f'{euclid_geometry(R): .6f}')
print(f'{taxi_cab_geometry(R): .6f}')