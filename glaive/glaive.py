import sklearn.cross_validation as cv
from sklearn import tree
import pandas as pd
import numpy as np
import os.path
import pprint 
import matplotlib.pyplot as plt
import seaborn as sns
import runExperiments
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import TanhLayer
from pybrain.tools.shortcuts import buildNetwork

def lossCalculation(model):
    """Evaluates the total loss on the dataset"""
    w1, b1, w2, b2 = model["w1"], model['b1'], model["w2"], model["b2"]
    
    z1 = X.dot
    
def normalize(lst):
	"""Normalizes the list"""
	s = float(sum(lst))
	return [v/s for v in lst]

#CONSTANTS
nn_input_dim = 6 #[x_enemy1, y_enemy1, x_enemy2, y_enemy2, x_enemy3, y_enemy3]
nn_output_dim = 6 #[x_ally1, y_ally1, x_ally2, y_ally2, x_ally3, y_ally3]

allyTrainingPos, enemyTrainingPos = runExperiments.makeTrainingDataset()

ds = SupervisedDataSet(nn_input_dim, nn_output_dim)

#normalizes and adds it to the dataset
for i in range(0, len(allyTrainingPos)):
	x = normalize([x for posPair in enemyTrainingPos[i] for x in posPair])
	y = normalize([y for posPair in allyTrainingPos[i] for y in posPair])
	ds.addSample(x, y)

for inpt, target in ds:
	print inpt, target

net = buildNetwork(nn_input_dim, 10, nn_output_dim, bias=True, hiddenclass=TanhLayer)
trainer = BackpropTrainer(net, ds)
trainer.trainUntilConvergence()

enemyTestPos = runExperiments.makeTestDataset()
print(net.activate(enemyTestPos))