#Kullanıcıya kaç seferde random sayıyı bileceğini soruyor ve yanlış bildiği her sorudan (100/iddiası) kadar puanı 100 den çıkarıp puanınını hesaplıyor.
# Aynı zamanda girilen sayı ile randomun atadığıu sayı arasında arttır yada azalt gibi işlemleride yönelndiriyor 

import random

value = random.randint(1,100)
aim = int(input("Please entry in how much time you can now the random selected number : "))
chance = aim
count = 0


while chance > 0:
    chance -= 1
    count += 1
    point = 100 - ((count -1) * (100 / aim))
    guess = int(input("Entry a value : "))

    if value == guess :
        print(f"Congrulations you found on {count}. time and you have {point} points")
        break
    elif value > guess:
        print("Increase")
    else:
        print("Decrease")

    if chance == 0:
        print(f"Your chance is finished. Selected value was {value} and you have 0 points ")