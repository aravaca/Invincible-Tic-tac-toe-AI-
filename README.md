# About Tic-tac-toe

This project includes a classic 3x3 tic-tac-toe game where you play against an unbeatable AI computer. The AI uses Newell and Simon's 1972 tic-tac-toe model as its algorithm. 

## Description

To play the game on Windows, simply download the tic-tac-toe_AI.exe file in the dist folder and run it. On other operating systems, assuming that you have Python installed, copy the source code (or clone the repository) and run the game using the following command:
```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
cd tic-tac-toe
python game.py
```
Then, follow the instructions as you play.

NOTE:
The grid uses 1-9 indexing from left to right in the following form:<br/>
1 | 2 | 3<br/>
4 | 5 | 6<br/>
7 | 8 | 9<br/>

## Acknowledgement
The source code for the basic version of the game is from Kylie Ying's GitHub (https://github.com/kying18). I want to give a special thanks to her YouTube tutorial. However, the class AI_Player in player.py, method get_owl and check_two_in_row in game.py, and the main method, which contains all necessary logic and procedures for the AI and its algorithm, are solely written on my own. I have also added features such as a scoreboard, choosing the order for which player goes first, and playing multiple times. For the perfect tic-tac-toe algorithm, I referred to K.Crowley and R.Siegler's work from *Flexible Strategy Use in Young Children’s Tic-Tat-Toe* (Carnegie Mellon University, 1993).


