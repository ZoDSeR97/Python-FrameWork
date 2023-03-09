from classes.deck import Deck

""" 
    Implement a simple blackjack card game
    Have not implemented split hand rule
"""


def blackJackPts(handList):
    totalPts = 0
    for card in handList:
        pts = card.getPts()
        if pts > 10:
            totalPts += 10
        elif pts == 1 and (pts+11) <= 21:
            totalPts += 11
        else:
            totalPts += pts
    return totalPts


def blackJack(deck):
    # Initial dealing
    turnList = [[deck.deal(), deck.deal()], [deck.deal(), deck.deal()]]
    pts = [0]*2
    str = ["Player", "House"]

    # Turn loop
    for i in range(2):
        if not i:
            print("----Player Turn----")
        else:
            print("\n\n----House Turn----")
        pts[i] = blackJackPts(turnList[i])
        if pts[i] == 21:
            print(f"Black Jack! {str[i]} Win!")
            return
        print(f"{str[i]} Hand:", turnList[i])
        cmd = input("Hit or Stay? ") if not i else "stay"
        while (cmd.lower() != "stay" or pts[i] < 18):
            if (not i) and cmd.lower() == "stay" and pts[i] < 18:
                print("Not meet requirement to stay!")
            turnList[i].append(deck.deal())
            print(f"{str[i]} Hand:", turnList[i])
            pts[i] = blackJackPts(turnList[i])
            if pts[i] > 21:
                print(f"{str[i]} Busted! {str[not i]} Win!")
                return
            if not i:
                cmd = input("Hit or Stay? ")

    # Checking final hand
    if (pts[0] < pts[1]):
        print("House Win!")
    elif (pts[0] > pts[1]):
        print("Player Win!")
    else:
        print("A Draw!")


if __name__ == "__main__":
    blackJack(Deck().shuffle())
