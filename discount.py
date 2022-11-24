

def dice_game(total):
    game = input("do you want to play a game for a discount? y for yes and no to cancel:")
    if game == "y":
        import random

        min = random.randint(1, 9)
        max = random.randint(1, 9)
        print(min)
        print(max)
        z = min * max

        print("The final result ", z, "%")
        print("discount amount ", total * (1 - (z / 100)), "$")
