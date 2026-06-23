# Software-dev-a2-ref-def

# Platformer-game

User Requirements ;

1) As a player, I want to move left and right so that I can explore the level. Priority - (High)

2) As a player, I want to jump so that I can reach platforms and avoid enemies. Priority - (High)

3) As a player, I want the character to fall when jumping so that the game feels realistic. Priority - (High)

4) As a player, I want enemies to damage me so that the game provides challenge. Priority - (High)

5) As a player, I want to collect coins so that I can increase my score. Priority - (Medium)

6) As a player, I want to reach the goal so that I can complete the level. Priority - (High)

7) As a player, I want the game to end when I hit an enemy so that failure is recognised. Priority - (Low)

8) As a player, I want a background image so that the game environment feels immersive. Priority - (Extremely High)

9) As a player, I want graphics and images so that the game looks interesting. Priority - (High)

10) As a player, I want simple keyboard controls so that the game is easy to play. Priority - (Low)


System Requirements ;

1) The system shall allow the player to jump when the spacebar is pressed.

2) The system shall allow the player to move left and right using keyboard input.

3) The system shall detect collisions between player and platform.

4) The system shall detect collision between player and enemy and trigger game over.

5) The system shall detect when the player collects a coin.

6) The system shall detect when the player reaches the goal.

7) The system should detect if the player reaches the end goal


Scrum Backlog ;

| ID   | Feature            | Priority | Description                                       | Testing                          |
| ---- | ------------------ | -------- | ------------------------------------------------- | ------------------------------------ |
| 1  | Player Movement    | High     | Player moves left and right using keyboard arrows | Press left/right keys - Movement |
| 2  | Jump System        | High     | Player jumps using spacebar                       | Press space - Movement           |
| 3  | Gravity System     | High     | Player falls back down after jumping              | Player jumps - Movement            |
| 4  | Platform Collision | High     | Player lands on platform without falling through  | Player lands on platform correctly   |
| 5  | Enemy Movement     | Medium   | Enemy moves back and forth                        | Enemy moves automatically            |
| 6  | Enemy Collision    | Medium   | Player loses if touching enemy                    | Touch enemy - Game End            |
| 7  | Coin Collection    | Medium   | Player collects coin and increases score          | Touch coin - Score        |
| 8  | Background Display | Low      | Background image loads in game                    | Background appears                   |
| 9  | Goal System        | High     | Player wins when reaching goal                    | Touch goal - End message           |
| 10 | Game Window        | High     | Game screen loads correctly                       | Game window opens                    |
| 11 | Score System       | Medium   | Score increases when coin collected               | Collect coin - Change of score         |
| 12 | Game Loop          | High     | Game continuously updates screen                  | Game runs smoothly                   |
| 13 | Keyboard Controls  | High     | Game responds to key input                        | Keys move player                     |
| 14 | Sprite Display     | Medium   | Player and enemy images load                      | Images appear correctly              |


Sprint Steps ;

1 - Enemy system
  - Platforming
  - Coin system

2 - Gravity
  - Player movement
  - Jump and end goal system

3 - Testing
  - Goal system
  - Background

<img width="798" height="402" alt="image" src="https://github.com/user-attachments/assets/efa20ca4-0c3d-442b-886c-36fd4079d345" />

Above is a image of the base level of the game and how it looks in its most simple and basic form 
As displayed in the image the requirements are fullfilled with the hero and enemy sprites and the coins to show there is something to gain in the game
In the future there is hopes to add other features and improve the game but for now there is many errors with the score not being in the correct locations and failure to load multiple levels after completing the first level. In different levels there will be different backgrounds and enemies with multiple enemies and multiple different enemy types. Also there may be chance to add a power up addition and enemies to shoot attacks that the hero has to dodge 


1) - Game title
  
Game Title: Hero Of Lys
Game Type: 2D Platformer 
Platform: PC/Laptop
Language: Python using Pygame
Target Audience: Casual players/Students

2) - Game story

The hero controls a hero character that has to get coins and get a minimum amount of coins to pass the level whilst dodging moving enemy combatants and making it to the end goal whilst maintaining their lives and the main goal. When multiple levels are added a life system will be added where the hero has 3 lifes for example and each time they die to the enemy they lose a life, as the levels get progressively harder more lifes can be added and a feature where there is an option to start with 1 life to make the game harder with each level passed giving the hero an extra life for the hero.

3) - Characters
  
Name: Hero
Type: Player-controlled character
Appearance: Small hero type character that is pixelated
Abilities:
- Move in all directions
- Jump
- Collect coins
- Dodging enemies to get to the end goal

Purpose:
The player controls this character to collect coins, dodge enemies and make it to the end goal with levels making it progressively harder level by level.

Name: Enemy
Type: Computer-controlled character
Appearance: Small enemy type pixelated character that deals damage to the hero when contact is made
Abilities:
- Moves left and right automatically
- Causes game over if touched

Purpose:
Acts as an obstacle to the hero and makes it difficult to reach the end goal.

4) - Gameplay design
Involves a hero and an enemy and the hero needing to dodge the enemy whilst collecting coins to reach the end goal and make it their safely in order to reach the end goal and progress through the levels

5) - Environment design
Game takes place in a side view 2d environment with trees and scenery that currently dont have an effect on the hero. However in future there is potential to add the background and make it interactive with the hero by adding jump ups and jump downs whilst the screen is moving simultaneously.

6) - Controls design

Keyboard Controls:

Left Arrow  → Move Left  
Right Arrow → Move Right  
Spacebar    → Jump  
Close Window → Exit Game

7) - Game rules

Game Rules:

1. The player can move left and right.
2. The player can jump using the spacebar.
3. The player must avoid and dodge enemies
4. Touching an enemy results in death and game over
5. Collecting coins increases the score.
6. Reaching the goal completes the level.

Backlog reviews 

Review 1

Completed

Created project structure
Installed Pygame

Next

Create player movement

Problems

Learning Pygame controls
Review 2

Completed

Movement
Jumping

Next

Enemy system

Problems

Collision detection
Review 3

Completed

Enemy movement
Coin collection

Next

Testing

Problems

Asset loading errors
Review 4

Completed

Testing
README

Next

Demo

Problems

None
