import math
import random
import numpy as np



def distance(x, y, maxX, maxY):
    """get the euclidian distance"""
    xDis = (x-maxX/2)**2
    yDis = (y-maxY/2)**2
    distance = np.sqrt(xDis + yDis)
    return distance

#[Unit name(s), player number, unitMultiplyer]
ally = ["Zerg_Zergling", 0, 2]
enemy = ["Terran_Marine", 1, 1]
unitCount = 3
maxX = 1280
maxY = 720

#Map Limitations are 0-1280 for x, and 0-720 for y
with open("experiment.txt", "w+") as expFile:
    #player 0 positions are between (0-640, 0-720)
    enemyPositions = []
    for i in range(enemy[2]*unitCount):
        x = np.random.randint(maxX/4, 3*maxX/4)
        y = np.random.randint(maxY/4, 3*maxY/4)
        enemyPositions.append((x, y))
    
    enemyDistance = []
    for enemyPosition in enemyPositions:
        enemyDistance.append(distance(enemyPosition[0], enemyPosition[1], maxX, maxY))
    