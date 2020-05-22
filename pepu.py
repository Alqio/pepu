import random
from playsound import playsound

def prob(nums):
    return 1 / len(numbers) * 100

numbers = [1,2,3]
sounds = ["pepu1.mp3", "pepu2.mp3"]

print("Pepu arvonta alkoi!")
print("Pelissä mukana", numbers)
print("Todennäköisyys voittaa: {0:.2f}".format(prob(numbers)))

while len(numbers) > 1:
    i = input("")
    playsound(random.choice(sounds))

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
