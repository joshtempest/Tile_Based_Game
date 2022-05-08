import pygame as pg
import keyboard
import random
import time
from os import path
from settings import *

def combat():
    #A list of enemies to randomly be chosen when combat is called
    enemies = ["Atom", "Birb", "Python"]
    enemy = random.choice(enemies)
    #Depending on which enemy it is, health is defined to fit
    if enemy == "Atom":
        enemyHP = 120

    elif enemy == "Birb":
        enemyHP = 80

    elif enemy == "Python":
        enemyHP = 160

    #Shows on screen which enemy you're going to face
    appear = Text.render(("A wild " + enemy + " appeared"), True, pg.Color('white'))
    cscreen.blit(appear, (textW, textH))
    pg.display.flip()
    #After 2 seconds we "reset" the screen
    time.sleep(2)
    cscreen.fill(TRANSPARENT)
    pg.display.flip()
    #Starts combat running loop
    crunning = True
    #Makes enemy health
    currentEHP = enemyHP
    time.sleep(0.5)
    while crunning == True:
        #cscreen.blit(fimage, (WIDTH - 220, HEIGHT - 410))
        cscreen.blit(ENEMY_ASSET, (WIDTH - 1000, HEIGHT - 1000))
        pg.display.flip()
        currentEHP, DMGModifier = playerAttack(currentEHP)
        if currentEHP > 0:
            enemyAttack(enemy)

        else:
            cscreen.fill(TRANSPARENT)
            Vic = Text.render(("You have won! Congratulations!"), True, pg.Color('gold'))
            cscreen.blit(Vic, (textW, textH))
            pg.display.flip()
            time.sleep(2)
            Dead = True
            crunning = False

    #enemyAttack(enemy)

def playerAttack(currentEHP):
    print('playerAttack')
    playerDMG = 0
    enemyDMG = 0
    enemyHP = currentEHP
    while True:
        if keyboard.is_pressed('esc'):
            crunning = False
        moveChoice = Text.render(("Choose your move (1, 2, 3, 4)"), True, pg.Color('white'))
        ehp = Text.render((str(enemyHP)), True, pg.Color('white'))
        cscreen.blit(ehp, (textW, 100))
        cscreen.blit(moveChoice, (textW, textH))
        pg.display.flip()
        cscreen.fill(TRANSPARENT)
        cscreen.blit(ENEMY_ASSET,(WIDTH - 1000, HEIGHT - 1000))

        if keyboard.is_pressed("1"):
            playerMove = Text.render(("You punched"), True, pg.Color('white'))
            playerDMG = 30
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pg.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pg.display.flip()
            time.sleep(1)
            return enemyHP, 1

        elif keyboard.is_pressed("2"):
            playerMove = Text.render(("You kicked"), True, pg.Color('white'))
            playerDMG = 40
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True , pg.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pg.display.flip()
            time.sleep(1)
            return enemyHP, 1

        elif keyboard.is_pressed("3"):
            playerMove = Text.render(("You screamed"), True, pg.Color('white'))
            dmgreductext = Text.render(("Enemy will do 10% less dmg next attack"), True, pg.Color('white'))
            playerDMG = 15
            enemyHP = enemyHP - playerDMG
            dmgtext = Text.render(("It did " + str(playerDMG) + " dmg"), True, pg.Color('white'))
            dmgreduc = 0.9
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            cscreen.blit(dmgreductext, (textW, textH + 100))
            pg.display.flip()
            time.sleep(1)
            return enemyHP, dmgreduc

        elif keyboard.is_pressed("4"):
            playerMove = Text.render(("You defended yourself"), True, pg.Color('white'))
            dmgtext = Text.render(("You take 90% less dmg"), True, pg.Color('white'))
            cscreen.blit(playerMove, (textW, textH))
            cscreen.blit(dmgtext, (textW, textH + 50))
            pg.display.flip()
            dmgreduc = 0.1
            time.sleep(1)
            crunning = False
            return enemyHP, dmgreduc

def enemyAttack(enemy):
    if enemy == "Atom":
        moves = [2,3,4]
        move = random.choice(moves)

    elif enemy == "Birb":
        moves = [1,5]
        move = random.choice(moves)

    elif enemy == "Python":
        moves = [2,3,4]
        move = random.choice(moves)

    if move == 1:
        emove = Text.render((enemy + " used kick!"), True, pg.Color('white'))
        edmg = Text.render(('It dealt 20 dmg'), True, pg.Color('red'))
        enemyDMG = 20
        cscreen.blit(emove, (textW, textH))
        cscreen.blit(edmg, (textW, textH + 50))
        pg.display.flip()
        time.sleep(2)
        return enemyDMG
    elif move == 2:
        print(enemy + " used bug!")
        print("Does critical dmg")
        print('Took 40 dmg')

    elif move == 3:
        print(enemy + " crashed")
        print("You won the battle")

    elif move == 4:
        print(enemy + " used error")
        print("does 45 dmg")

    elif move == 5:
        print(enemy + " used schreech")
        print("You take 5 dmg")
        #print("You do 10% less dmg next attack")
