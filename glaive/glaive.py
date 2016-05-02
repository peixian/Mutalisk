import sklearn.cross_validation as cv
from sklearn import tree
import pandas as pd
import numpy as np
import os.path
import pprint 
import matplotlib.pyplot as plt
import seaborn as sns

def lossCalculation(model):
    """Evaluates the total loss on the dataset"""
    w1, b1, w2, b2 = model["w1"], model['b1'], model["w2"], model["b2"]
    
    z1 = X.dot
    
def predict(model, x):
    """predicts an outputs a decision"""
    pass

#CONSTANTS
nn_input_dim = 8 #[Ally Units, Enemy Units, x_enemy1, y_enemy1, x_enemy2, y_enemy2, x_enemy3, y_enemy3]
nn_output_dim = 6 #[x_ally1, y_ally1, x_ally2, y_ally2, x_ally3, y_ally3]

#Gradient Descent 
epsilon = 0.01
reg_lambda = 0.01