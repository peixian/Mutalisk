import sklearn.cross_validation as cv
from sklearn import tree
import pandas as pd
import numpy as np
import os.path
import pprint 
import matplotlib.pyplot as plt
import seaborn as sns

def readData(maxReplayCount = 749):
    """reads the data from .arff files (Weka Attribute-Relation files)
    
    maxReplayCount is <= 749
    
    returns:
    data - a list of dataframes containing replay build orders of the first 100 actions, indexed as ['frame', 'action', 'actionNumber']
    """
    filename = "data/pvt_{}_lifetimes.arff"
    range = np.arange(1, maxReplayCount)
    
    data = []
    buildList = set([])
    for replay in range:
        replayName = filename.format(str(replay).zfill(3))
        if (os.path.isfile(replayName)):
            with open(replayName, "r") as file:
                #read, strip, and remove unnecessary data
                lines = map(lambda x: x.rstrip().split(",")[:2], file.readlines()[11:111])
                #make and add a dataframe
                df = pd.DataFrame(lines, columns=("frame", "action"))
                df = df[df.frame != ""]
                df["frame"] = df["frame"].map(lambda x: int(x))
                df["action"] = df["action"].map(lambda x: str(x).replace("Protoss ", "").replace(" ", "_"))
                for action in list(df["action"].unique()):
                    buildList.add(action)
                data.append(df)
    
    # print(data)
    # print(type(data))
    # buildList = map(lambda x: list(x["action"].unique()), data)
    buildList = list(buildList)
    for df in data:
        df["actionNumber"] = df["action"].map(lambda x: buildList.index(x))
    return data, buildList
    
    
def createVectors(data):
    """iterates through data and creates a list of vectors of ['frame', 'buildID']
    refer to buildList for buildID
    """
    vec = []
    for df in data:
        subset = df[["frame", "actionNumber"]]
        vec.append(subset.values)
    vec = [item for sublist in vec for item in sublist]
    return vec

data, buildList = readData()
vectors = createVectors(data)
plt.scatter(*zip(*vectors))
plt.show()
# pprint.pprint(vectors)