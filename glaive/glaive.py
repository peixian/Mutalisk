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
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.xml.networkreader import NetworkReader

def lossCalculation(model):
    """Evaluates the total loss on the dataset"""
    w1, b1, w2, b2 = model["w1"], model['b1'], model["w2"], model["b2"]
    
    z1 = X.dot
    
def normalize(lst):
	"""Normalizes the list, reducing the x by 640 and y by 720"""
	normed = map(lambda p: (p[0]/640.0, p[1]/720.0), lst)
	return normed

def createNet():
	"""Create and seed the intial neural network"""
	#CONSTANTS
	nn_input_dim = 6 #[x_enemy1, y_enemy1, x_enemy2, y_enemy2, x_enemy3, y_enemy3]
	nn_output_dim = 6 #[x_ally1, y_ally1, x_ally2, y_ally2, x_ally3, y_ally3]

	allyTrainingPos, enemyTrainingPos = runExperiments.makeTrainingDataset()

	ds = SupervisedDataSet(nn_input_dim, nn_output_dim)

	#normalizes and adds it to the dataset
	for i in range(0, len(allyTrainingPos)):
		x = normalize(enemyTrainingPos[i])
		y = normalize(allyTrainingPos[i])
		x = [val for pair in x for val in pair]
		y = [val for pair in y for val in pair]
		ds.addSample(x, y)

	for inpt, target in ds:
		print inpt, target

	net = buildNetwork(nn_input_dim, 30, nn_output_dim, bias=True, hiddenclass=TanhLayer)
	trainer = BackpropTrainer(net, ds)
	trainer.trainUntilConvergence()
	NetworkWriter.writeToFile(net, "net.xml")
	enemyTestPos = runExperiments.makeTestDataset()
	print(net.activate([val for pair in normalize(enemyTestPos) for val in pair]))
	return ds

def startTrials(ds, maxTrials = 2, maxExperiments = 2):
	"""start and run the trials"""
	hpCount = []
	for i in range(0, maxExperiments):
		for j in range(0, maxTrials):
			enemyTestPos = runExperiments.makeTestDataset()
			net = NetworkReader.readFrom("net.xml")

			netResults = net.activate([val for pair in normalize(enemyTestPos) for val in pair])
			netIter = iter(netResults)
			allyTestPos = zip(netIter, netIter)
			#undo normalization
			allyTestPos = map(lambda p: (abs(p[0]*640), abs(p[1]*720)), allyTestPos)
			print(allyTestPos)
			runExperiments.writeTestData(allyTestPos)
			runExperiments.run()

			with open("exp_results_raw.txt", "r") as resultsFile:
				lines = resultsFile.readlines()
				if "Zerg_Zergling" in lines[1]:
					x = normalize(enemyTestPos)
					y = normalize(allyTestPos)
					x = [val for pair in x for val in pair]
					y = [val for pair in y for val in pair]
					ds.addSample(x, y)
					lineSplit = lines[1].split("Zerg_Zergling")[-1]
					hpCount.append(lineSplit.split(" ")[2])
		trainer = BackpropTrainer(net, ds)
		trainer.trainEpochs(20)
	return hpCount

ds = createNet()
hpCount = startTrials(ds, 30, 10)
print(hpCount)
fig, ax = plt.subplots()
ax.plot(range(0, len(hpCount)),hpCount)
plt.show()