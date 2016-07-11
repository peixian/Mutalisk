# Ultralisk - Starcraft: Brood War Bot - Optimized for Small Scale Combat
![Ultralisk](ultralisk.png)

*Image from [Carbot][Carbot]*

## Paper Link - https://github.com/peixian/Ultralisk/blob/master/paper/paper.pdf


Ultralisk is a Starcraft: Brood War bot written in C++ on top of the [BWAPI][BWAPI] composed of two parts: 1) the actual AI (called Ultralisk) and 2) a neural network that creates stratagems (called Glaive). Using Glaive to decide on optimal build and unit composition after being trained on [replays][replays], Ultralisk seeks to accomplish a very modest goal of winning a majority of games against the built in Brood War AI. 


About Starcraft: Brood War
-----
Starcraft: Brood War is a real time strategy game originally released in 1998. Brood War's complexity has enabled it to become one of the most popular video games every played, despite having Starcraft II released as a sequel. Brood War has a very basic routine that can be easily summed in 3 steps:

1. Gather resources (called Minerals and Vespene Gas)
2. Spend resources to build an army composed of a variety of units
3. Use the army to attack and ultimately destroy the opponent's units and base.

The actual game is far more nuanced, but the 3 steps are sufficient as a *very* high level overview. 

Technology Stack
------
Ultralisk seeks to use the `CompleteMapInformation` flag within [BWAPI][BWAPI] to gain information through the fog of war without scouting (as scouting probably requires its own entire subroutine). Through the analysis of hundreds of small scale combat simulations in [SparCraft][SparCraft] and relearning through glaive, Ultralisk seeks to create an optimized deployment pattern for small scale combat. 


Implementation Details
-----
- Agent - Ultralisk itself is an agent that interacts directly with the Starcraft: Brood War environment, through knowledge gained from Glaive.
- Environment - The Brood War gameplay environment along with the SparCraft environment
- Sensors - `CompleteMapInformation` will be enabled to avoid writing a complete scouting bot (this is definitely cheating the game a bit, possibly revisit this later on)
- Actions - Ultralisk itself has access to all actions a normal player would, which is to mine minerals, acquire gas, build units, etc. 
- Controller - The controller will be information created by Glaive itself, passed into [UAlbertaBot][UAlbertaBot]
- Interaction & Analysis - SparCraft generates combat data for analysis, and Brood War generates replays


Roadmap:
---
- [x] Glaive build 0.0.1 - **April 27** - Functioning Glaive, should be able to read and sufficiently analyze replays
- [x] Glaive build 0.1 - **April 28** - Glaive should be able to generate and output responses to opponent's actions, should be ready to be implemented into Ultralisk
- [x] Ultralisk build 0.0.1 - **April 30** - Ultralisk should be a semi-functioning form, should exhibit the ability to follow various build commands and unit attacks
- [x] Ultralisk build 0.1 - **May 1** - Ultralisk should be able to follow a specific build path, and be able to see what the opponent is building
- [x] Ultralisk build 0.2 - **May 2** - Ultralisk should be able to read from Glaive outputs
- [x] Ultralisk build 0.3 - **May 3** - Minimum Viable Product


[UAlbertaBot]: https://github.com/davechurchill/ualbertabot
[BWAPI]: https://github.com/bwapi/bwapi
[replays]: http://www.starcraftai.com/wiki/StarCraft_Brood_War_Data_Mining
[scikit]: http://scikit-learn.org/stable/
[FANN]: http://leenissen.dk/fann/wp/
[Carbot]: http://carbotstarcrafts.tumblr.com/
[SparCraft]: https://github.com/davechurchill/ualbertabot/wiki/SparCraft-Home
