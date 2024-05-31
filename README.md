e-mail: chs_3411@naver[dot]com<br/>
any feedback/request is always welcomed!


# About Tic-tac-toe

This project includes a classic 3x3 tic-tac-toe game where you play against an unbeatable AI computer. The algorithm is designed based on Newell and Simon's 1972 tic-tac-toe model.<br/>
(KOR) 이 프로젝트는 3x3 틱택토 게임에서 절대 지지 않는 인공지능 컴퓨터를 구현합니다. 뉴웰과 사이먼의 1972 틱택토 모델을 바탕으로 알고리즘을 제작하였습니다.

## Basic Rules

<img src="https://github.com/aravaca/tic-tac-toe/assets/157980478/181351bb-eb24-40f3-bfb3-2b71541fc30b" width="120">

Two players take turns putting their marks (either X or O) in empty squares. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner. Tic-tac-toe is a classic zero-sum game meaning that winning of a player automatically leads to losing of the other player. If that is not the case, it's a tie. <br/>
두 명의 선수가 번갈아가며 3x3 판 위 빈 사각형에 자신의 말(X 또는 O)을 넣습니다. 자신의 말 중 3개를 연속으로 연결시킨 첫 번째 선수가 승자입니다. 틱택토는 한 선수의 승리가 자동으로 다른 선수의 패배로 이어진다는 의미에서 고전적인 제로섬 게임입니다. 만약 누구 한 명이라도 이기거나 지지 않는다면 경기는 무승부입니다.

## How can the AI never lose?

The AI uses an algorithm that looks ahead a couple of moves and classifies all available moves in terms of priority. The AI will choose the first available move with the highest assigned priority so long as it does not present an opportunity for the human player to win. This allows the AI to tie in with the human player in the worst case. Although the code for minimax is more concise, the advantage of this algorithm over the minimax algorithm with heuristics is performance speed. The minimax algorithm employs a recursive function to look ahead at most nine moves and construct a complete game tree. This is inefficient as each recursion call is pushed onto the stack frame for later use. <br/>
인공지능은 몇 수 앞을 내다 보고 사용 가능한 모든 움직임을 우선순위에 따라 분류하는 알고리즘을 사용합니다. 인공지능은 인간 플레이어가 이길 수 있는 기회를 제공하지 않는 한 가장 높은 우선순위로 사용 가능한 첫 번째 움직임을 선택합니다. 이것은 최악의 경우 인공지능이 인간 플레이어와 동점을 만들 수 있도록 합니다. 휴리스틱이 있는 미니맥스 알고리즘에 비해 이 알고리즘의 장점은 효율성(속도)입니다. 미니맥스 알고리즘은 재귀를 사용하여 최대 9수를 내다 보고 게임 트리를 구축합니다. 이것은 매번 재귀 호출을 할 때 마다 스택 프레임에 푸시되기 때문에 분명히 비효율적입니다.

## Statistics

<img src="https://github.com/aravaca/tic-tac-toe/assets/157980478/ce26aeb3-ebca-46c6-a979-1dc178e30083" width="720">

The stats above demonstrate the win rates for each player in three distinct scenarios (AI vs Random, Random vs AI, and AI vs AI). The rates are computed from a sample of 100,000 randomly generated cases per scenario (so 300,000 cases in total!). It can be easily observed that the AI never loses regardless of the game configuration.
위의 통계는 다양한 시나리오에서 각 플레이어의 승률을 보여줍니다. 각 시나리오당 무작위로 생성된 100,000건의 사례 샘플(AI vs Random, Random vs AI, AI vs AI)에서 승률이 계산됩니다. 테이블을 보면 AI는 게임 구성에 관계없이 절대 지지 않는다는 것을 쉽게 관찰할 수 있습니다.

## How to play

To play the game on Windows, simply download and run the game.exe file in the dist folder. On other operating systems, assuming that you have Python installed, clone the repository and run the game using the command below in the terminal.<br/>
Windows에서 게임을 하려면 dist 폴더에서 game.exe 파일을 다운로드하여 실행하기만 하면 됩니다. 다른 운영 체제에서는 Python이 설치되어 있다고 가정하에, repository를 복제하고 터미널에서 다음 명령을 사용하여 게임을 실행합니다.<br/>
```bash
git clone https://github.com/aravaca/tic-tac-toe
cd tic-tac-toe\src
python game.py #or could be python3
```
Then, follow the instructions as you play on the console.<br/>
그런 다음 콘솔에서 플레이하며 게임 안내를 따르면 됩니다.

NOTE:
The grid uses 1-9 indexing from left to right in the following form:<br/>
판은 다음과 같은 형태로 왼쪽에서 오른쪽으로 1-9 인덱싱을 사용합니다. <br/>
1 | 2 | 3<br/>
4 | 5 | 6<br/>
7 | 8 | 9<br/>

## Acknowledgement
The source code for the basic version of the game is from Kylie Ying's GitHub (https://github.com/kying18). I want to give a special thanks to her YouTube tutorial. However, elements like class AI_Player in player.py, method get_owl and check_two_in_row in game.py, and the main method that contain all necessary logic and procedures for the AI and its algorithm are solely written on my own. I have also added features such as a scoreboard, choosing the order for which player goes first, and playing multiple times. For the perfect tic-tac-toe algorithm, I referred to K.Crowley and R.Siegler's research paper *Flexible Strategy Use in Young Children’s Tic-Tac-Toe* (Carnegie Mellon University, 1993).<br/>
게임의 기본 버전 소스 코드는 카일리 잉(Kylie Ying)의 깃허브(https://github.com/kying18) 에서 가져온 것입니다. 그녀의 유튜브 튜토리얼에 특별한 감사를 표하고 싶습니다. 그러나 player.py 의 AI_Player 클래스, game.py 의 get_owl 및 check_two_in_row 같은 몇몇 메소드들, 그리고 메인 메소드 등 AI와 그 알고리즘에 필요한 모든 논리와 절차가 포함된 구성 요소는 전적으로 스스로의 힘으로 작성되었음을 알리는 바입니다. 스코어보드, 선공 순서 선택, 여러 번 플레이 등의 편리기능도 추가했습니다. 완벽한 틱택토 알고리즘을 구현하기 위해 K.Crowley와 R.Siegler의 논문 *Flexible Strategy Use in Young Children’s Tic-Tac-Toe*(카네기 멜론 대학, 1993년)을 참고했습니다.


