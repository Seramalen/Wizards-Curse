from gpiozero import Button,LED
import signal
import pygame
import glob
import random
import time
from threading import Timer
from threading import Thread
import sys
from subprocess import check_call

#Initializing audio channels, loading audio, etc.
#Progam is loaded in an autostart file
pygame.mixer.pre_init()
pygame.mixer.init()
pygame.init()
paintingSolve = '/home/exit/Desktop/exitScripts/Better Audio/paintingSolve.wav'
ScratchedNose = '/home/exit/Desktop/exitScripts/2. ScratchedNose.wav'
Riddle = '/home/exit/Desktop/exitScripts/3. Riddle.wav'
LoopInstructions = '/home/exit/Desktop/exitScripts/4. RiddleLoopInstructions.wav'
AllBGM = '/home/exit/Desktop/exitScripts/WizardSnippedMusic.wav'
noseFirstPress = '/home/exit/Desktop/exitScripts/Better Audio/noseFirstPress.wav'
noseLaterPresses = '/home/exit/Desktop/exitScripts/Better Audio/noseLaterPresses.wav'
doorCreak = '/home/exit/Desktop/exitScripts/DoorCreak.wav'

pygame.mixer.Channel(0)
pygame.mixer.Channel(1)
pygame.mixer.Channel(2)
pygame.mixer.music.load(AllBGM)
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(loops=-1)

#Painting Switches
paint1 = Button(20)
paint2 = Button(22)
paint3 = Button(27)
paint4 = Button(13)
paint5 = Button(19)
paint6 = Button(26)

#Banner Reed Switches
banner1 = Button(2)
banner2 = Button(3)
banner3 = Button(4)
banner4 = Button(14)
bannerMem = 0

#Nose Button & Mag Lock
button11 = Button(15)
magLock = LED(18)
noseMem = 0

#Sound lock vars
paintingsPlayed = 0
bannersPlayed = 0

#def b1on():
    #global b1mem
   # b1mem = 1
    #print('Painting 1')
    #if (b1mem + b2mem + b3mem + b4mem + b5mem + b6mem) == 6:
      #  pygame.mixer.Channel(1).play(pygame.mixer.Sound(BannerSolve))
       
#def b1off():
   # global b1mem
   # b1mem = 0
        
def PaintingOn():
    time.sleep(0.5)
    global paintingsPlayed
    if(CheckPaintings() >= 3):
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(paintingSolve))
        time.sleep(18)
        pygame.mixer.music.set_volume(0.4)
        paintingsPlayed = paintingsPlayed +1
    

#Helper function that returns the amount of paintings currently active at the time
def CheckPaintings():
    paintingMem = 0
    if(paint1.is_pressed):
        paintingMem = paintingMem +1
    if(paint2.is_pressed):
        paintingMem = paintingMem +1
    if(paint3.is_pressed):
        paintingMem = paintingMem +1
    if(paint4.is_pressed):
        paintingMem = paintingMem +1
    if(paint5.is_pressed):
        paintingMem = paintingMem +1
    if(paint6.is_pressed):
        paintingMem = paintingMem +1
    print(paintingMem)
    return paintingMem
    
    
def Nose():
    global noseMem
    if noseMem == 0:
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(noseFirstPress))
        time.sleep(17)
        pygame.mixer.music.set_volume(0.4)
    elif noseMem >0 and noseMem <5:
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.Channel(1).play(pygame.music.Sound(noseLaterPresses))
        time.sleep(11)
        pygame.mixer.music.set_volume(0.4)
    noseMem = noseMem +1

def BannerOn():
    global bannerMem
    global bannersPlayed
    bannerMem = bannerMem +1
    if bannerMem == 4 and bannersPlayed == 0:
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.Channel(1).play(pygame.mixer.Sound(doorCreak))
        magLock.on()
        time.sleep(5)
        pygame.mixer.music.set_volume(0.4)
        bannersPlayed = bannersPlayed +1

def BannerOff():
    global bannerMem
    bannerMem = bannerMem -1
    
   
#Painting Switches
#button1.when_pressed = b1on
#button1.when_released = b1off
paint2.when_pressed = PaintingOn
paint3.when_pressed = PaintingOn
paint4.when_pressed = PaintingOn
paint5.when_pressed = PaintingOn
paint6.when_pressed = PaintingOn
#Banner Reed Switches
banner1.when_pressed = BannerOn
banner1.when_released = BannerOff
banner2.when_pressed = BannerOn
banner2.when_released = BannerOff
banner3.when_pressed = BannerOn
banner3.when_released = BannerOff
banner4.when_pressed = BannerOn
banner4.when_released = BannerOff
#THE NOSE. Normaled to on.
button11.when_released = Nose

#Required to make launch at startup functional
while True:
    pass
