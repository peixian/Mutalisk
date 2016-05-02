import subprocess
import trainingSetGen
import glaiveNN
import pybrain

def makeTrainingDataset():
	"""Generates random enemy and ally positions, preserves the ones that are positive, this is the intial training sample (note this is very small)"""
	goodAllyPositions = []
	goodEnemyPositions = []

	for i in range(0, 100):
	    sample = trainingSetGen.TrainingSetGen()
	    allyPositions, enemyPositions = sample.writeOut()
	    
	    #writes the experiment launch file, see documentation @ https://github.com/davechurchill/ualbertabot/wiki/SparCraft-Simulation-Settings
	    with open("experiment.txt", "w") as exp:
	        expStates = 10
	        exp.write("Player 0 NOKDPS\nPlayer 1 NOKDPS\n")
	        #write out experiment count
	        exp.write("State StateDescriptionFile {} unitPos.txt\n".format(expStates))
	        #write out reults
	        results_name = "exp"
	        exp.write("ResultsFile {} false\n".format(results_name))
	        
	        exp.write("Display false starcraft_images\\")
	    
	    #call the simulator
	    subprocess.check_call(["C:\\sparcraft\Sparcraft.exe", "experiment.txt"])
	    
	    #if the experiment is actually good, then save it
	    with open("exp_results_summary.txt", "r") as summary:
	        if (float(summary.readline().strip()) > .5):
	            goodAllyPositions.append(allyPositions)
	            goodEnemyPositions.append(enemyPositions)
	            
	with open("goodAllyPositions.txt", "w") as out:
	    for item in goodAllyPositions:
	        out.write("{}\n".format(item))
	with open("goodEnemyPositions.txt", "w") as out:
	    for item in goodEnemyPositions:
	        out.write("{}\n".format(item))
