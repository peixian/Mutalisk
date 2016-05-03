import subprocess
import trainingSetGen
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
	        expStates = 2
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
	
	return goodAllyPositions, goodEnemyPositions             
	# with open("goodAllyPositions.txt", "w") as out:
	#     for item in goodAllyPositions:
	#         out.write("{}\n".format(item))
	# with open("goodEnemyPositions.txt", "w") as out:
	#     for item in goodEnemyPositions:
	#         out.write("{}\n".format(item))

def makeTestDataset():
	"""Makes a random enemy positions"""
	sample = trainingSetGen.TrainingSetGen()
	enemyPositions = sample.writeEnemyPositions()
	return enemyPositions

def writeTestData(allyPositions):
	"""Writes the data into the unitPos.txt file"""
	sample = trainingSetGen.TrainingSetGen()
	allyPositions = sample.writeAllyPositions(allyPositions)
	return allyPositions

def run(times = 2):
	for i in range(times):
		subprocess.check_call(["C:\\sparcraft\Sparcraft.exe", "experiment.txt"])
