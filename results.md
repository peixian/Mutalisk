# Ultralisk - Using Neural Networks for Small Scale Combat Optimization

About Starcraft: Brood War
-----
Starcraft: Brood War is a real time strategy game originally released in 1998. Brood War's complexity has enabled it to become one of the most popular video games every played, despite having Starcraft II released as a sequel. Brood War has a very basic routine that can be easily summed in 3 steps:

1. Gather resources (called Minerals and Vespene Gas)
2. Spend resources to build an army composed of a variety of units
3. Use the army to attack and ultimately destroy the opponent's units and base.

The actual game is far more nuanced, but the 3 steps are sufficient as a *very* high level overview. 

Abstract
-----
A major issue for players and AI in real time strategy games is the individual control of units. For Starcraft, a major portion of it is finding the right places of engagement for combat, choosing effective places to position units before an engagement with the opponent is a vital part of Starcraft. Ultralisk seeks to improve upon basic decision making by creating a bot that focuses on proper positioning of units before an engagement. 

![bot](plots/bot.gif)

Hypothesis
----
By limiting Ultralisk to a small subset of units (melee ground units called Zerglings), Ultralisk should be able to find accurate deployment positions for its units.

Experimental Design
----
A map of size `1280 x 720` is created, where the left half is deployable by Ultralisk and the right half is deployable by the computer, as shown below:

![DeploymentZone](plots/deploymentZones.png)

Within this zone, Ultralisk can deploy 3 Zerglings: a fast moving melee unit with small amounts of HP (max 35). The computer can within its zone deploy 3 Marines: a slower moving melee unit with modest amounts of HP (max 50).

By generating hundreds of scenarios with various deployments by the computer, a subset of results can be obtained where Ultralisk won. These results are marked as successful and are then gathered into a dataset where a neural network is trained on them. Using backprop, this neural network can then generate where each Zergling should be placed. The neural network topology is shown below:

![neural network layout](plots/nnLayout.png)

SparCraft
----
SparCraft is a tool built to simulate combat within Starcraft: Brood War. Because it can approximate combat to an extremely close degree, it was the chosen tool for Ultralisk to run its simulations in.

![SparCraft](plots/sparcraft.gif)

Results
----
As the number of training epochs increased for the neural network, it began to show more complex deployment strategies, such as grouping multiple Zerglings together. A plot of the HP of the lowest living Zergling is shown below:

![zerglingHP](plots/zerglingHP.png)


[UAlbertaBot]: https://github.com/davechurchill/ualbertabot
[BWAPI]: https://github.com/bwapi/bwapi
[replays]: http://www.starcraftai.com/wiki/StarCraft_Brood_War_Data_Mining
[scikit]: http://scikit-learn.org/stable/
[FANN]: http://leenissen.dk/fann/wp/
[Carbot]: http://carbotstarcrafts.tumblr.com/
[SparCraft]: https://github.com/davechurchill/ualbertabot/wiki/SparCraft-Home