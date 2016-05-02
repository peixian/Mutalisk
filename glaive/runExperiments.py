import subprocess
import trainingSetGen

sample = trainingSetGen.TrainingSetGen()
sample.writeOut()

with open("experiment.txt", "w") as exp:
    expStates = 10
    exp.write("Player 0 NOKDPS\nPlayer 1 NOKDPS\n")
    #write out experiment count
    exp.write("State StateDescriptionFile {} unitPos.txt\n".format(expStates))
    #write out reults
    results_name = "exp_results"
    exp.write("ResultsFile {} false\n".format(results_name))
    
    exp.write("Display false starcraft_images\\")

subprocess.check_call(["cd C:\\sparcraft"])
subprocess.check_call(["Sparcraft.exe", "experiment.txt"])