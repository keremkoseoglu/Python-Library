# TIC TAC TO AI

This project is a simple and extendable AI 
demonstration. 
The code is written in Python.

The GUI is built on TK, and defensive programming
is mostly ignored. 

## How to use

To test the application, simply start main.py .

You can modify main.py to change the way the
application behaves. Sorry, I was too lazy
for command line support.

Currently, there are two supported modes:
* Training
* Execution

## AI architecture

### Abstract AI

ai.abstract_ai is the base class for any
AI code to play tic tac toe. You can add new
 AI implementations by inheriting a new class
 from ai.abstract_ai. 

The abstract class has methods for:
* Training itself & saving train data
* Loading train data
* Playing with humans & learning

### Q-Learning

#### Details

The debut release of this project includes a 
sample & simple Q-Learning implementation; which
conducts an unsupervised reinforcement 
learning effort.

If you don't know anything about Q-Learning,
you can get more info [here](http://mnemstudio.org/path-finding-q-learning-tutorial.htm).

In training mode, the program will play against
itself with purely random moves. When a game is
finished, the moves will be evaluated.
The number of games to be played can be 
modified in ai.qlearning. The initial number
is 1.000.000.

For the winner, the last move is worth n points, 
and former moves are worth n-1, n-2, ... points.

For the loser, the last move is worth -n points, 
and former moves are worth -(n-1), -(n-2), ...
points.

Evaluation of games are stored in the qlearning_memory.txt
file. A sample dump file is included. As the
code plays against humans, it keeps the file updated.

#### Possible improvements

In a semi-supervised training approach, I 
could have given the ability to foresee
obvious good / bad moves. 

During training, the program makes purely
random choices. No AI is included here.

It is possible to mirror previous board 
states horizontally & vertically during
the decision making process, but I neglected
this possible improvement.

It is also possible to re-play lost games
by changing one move at a time until the
game is won. That would improve
the learning effectiveness of the code.

The results are stored in a text file. For
larger projects, a database could have been
a more suitable choice.