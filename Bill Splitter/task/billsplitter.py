# Take user input — how many people want to join, including the user;
import random

def getGuests():

    print("Enter the number of friends joining (including you):")
    count = 0
    guests = {}
    n = int(input())
    if n <= 0:
        print("No one is joining for the party")
    else:
        print("Enter the name of every friend (including you), each on a new line:")
        while count < n:
            name = str(input())
            guests[name] = 0
            count += 1
    return n, guests


def getBill():

    print("Enter the total bill value:")
    bill = int(input())
    return bill


def splitBill(n, guests, bill):

    splittedBill = round(bill/n, 2)
    for key, value in guests.items():
        guests[key] = splittedBill
    return guests


def getLucky(guests):

    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    yesList = ["Yes", "YES", "yes", "y"]
    answer = input()
    if answer in yesList:
        lucky = random.choice(list(guests.keys()))
        print("{} is the lucky one!".format(lucky))
        return lucky
    else:
        print("No one is going to be lucky")
        return None


def recalBill(n, guests, bill, lucky):

    newbill = bill/(n-1)
    for key, value in guests.items():
            guests[key] = newbill
    guests[lucky] = 0
    return guests



def stage1():

    n, guests = getGuests()
    if n > 0:
        print(guests)
    else:
        exit()


def stage2():

    n, guests = getGuests()
    if n > 0:
        bill = getBill()
        print(splitBill(n, guests, bill))
    else:
        exit()


def stage3():

    n, guests = getGuests()
    if n > 0:
        bill = getBill()
        getLucky(guests)
    else:
        exit()


def stage4():

    n, guests = getGuests()
    if n > 0:
        bill = getBill()
        guests = splitBill(n, guests, bill)
        lucky = getLucky(guests)
        if lucky == None:
            print(guests)
        else:
            print(recalBill(n, guests, bill, lucky))
    else:
        exit()


if __name__ == "__main__":

    #stage1()
    #stage2()
    #stage3()
    stage4()