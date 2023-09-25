import random

import requests as requests

player1score=0
player2score=0
currentRound=1
# Generated a random number between 1 and 151 to use as the Pokemon ID number
def getRandomNumber(minimum,maximum):
    return random.randint(minimum,maximum)

# Create a dictionary that contains the returned Pokemon's name, id, height and weight
def getpokemon(ID):
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(ID)
    response = requests.get(url)
    pokemon = response.json()
    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
    }
def round():
    global player1score
    global player2score
    global currentRound
    print("current round: "+ str(currentRound))
    number = getRandomNumber(1, 151)
    pokemon1 = getpokemon(number)
    print("user 1: " + str(pokemon1))
    number = getRandomNumber(1, 151)
    pokemon2 = getpokemon(number)

# Get a random Pokemon for the player and another for their opponent
    attr = ""
    while attr != "height" and attr != "weight" and attr != "id":

# Ask the user which stat they want to use (id, height or weight)
        attr = input("select attributes to compare, [height,weight,id]:  ")

    pokemon1attr = pokemon1[attr]
    pokemon2attr = pokemon2[attr]
    print(pokemon1attr)
    print(pokemon2attr)
    if pokemon1attr > pokemon2attr:
        player1score+=5
        print("you win round "+ str(currentRound))
    else:
        player2score += 5
        print("you lose round "+ str(currentRound))

# Compare the player's and opponent's Pokemon on the chosen stat to decide who wins
def init():
    global currentRound
    while currentRound < 4:
        round()
        currentRound = currentRound + 1
    if player1score > player2score:
        print("congratulations, you have won")
    else:
        print("you lose better luck next time")


if __name__ == '__main__':
    init()