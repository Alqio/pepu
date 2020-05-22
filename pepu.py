import random
from playsound import playsound
import sys
from time import sleep

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


# Vaihda tähän oikeat numerot 
#numbers = [1, 2, 4, 8, 9, 10, 14, 15, 16, 21, 22, 25, 27, 28, 30, 33, 42, 44, 53, 54, 55, 60, 69, 75]

numbers = [1,2,3,4,5]

def prob(nums):
    return 1 / len(numbers) * 100

sounds = ["pepu1.wav"]
pygame.mixer.init()
pygame.mixer.music.load(random.choice(sounds))

print("Pepu arvonta alkoi!")
print("Pelissä mukana", numbers, "yhteensä osallistujia", len(numbers))
print("Todennäköisyys voittaa: {0:.2f}".format(prob(numbers)))

while len(numbers) > 1:
    i = input("")
    
    pygame.mixer.music.play()
    
    t = 0
    i = 0
    while t < 3: 
        number = i % len(numbers)
        sleep(0.01)
        print("{}\r".format(number), end="")
        i += 1
        t += 0.008

    number = random.choice(numbers)
    print("Numero:", number)

    numbers.remove(number)

    if len(numbers) > 1:
        print("Pelissä vielä jäljellä:", numbers)
        print("Todennäköisyys voittaa: {0:.2f}".format(prob(numbers)))

number = numbers[0]

print()
print("Ja voittaja on...")
playsound("win.mp3")
print("Numero " + str(numbers[0]) + "!")
print()
