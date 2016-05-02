import subprocess
import trainingSetGen

goodAllyPositions = []
goodEnemyPositions = []

for i in range(0, 100):
    sample = trainingSetGen.TrainingSetGen()
    allyPositions, enemyPositions = sample.writeOut()
    
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
    
    with open("exp_results_summary.txt", "r") as summary:
        if (float(summary.readline().strip()) > .5):
            goodAllyPositions.append(allyPositions)
            goodEnemyPositions.append(enemyPositions)
            
print(goodAllyPositions)