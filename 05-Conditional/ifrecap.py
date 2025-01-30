"""
Kirjuta programm, mis küsib kasutajalt ilma ja kuupäeva ning
olenevalt vastusest kirjutab erineva tegevuse ekraanile.

Kasutame liit tingimust ja vähemalt kolme erinevat tegevust.
"""
import datetime


def what_to_do():
    weather = input("Tänane ilm on: (päikseline, vihmane) ")
    currentmonth = int(datetime.date.today().month)

    if weather == "päikseline" and currentmonth in [5, 6, 7, 8]:
        print("Mine ujuma!")
    elif (weather == "päikseline" or weather == "vihmane") and currentmonth in [
        1, 2, 3, 4, 9, 10, 11, 12]:
        print("Pane kampsun selga!")
    else:
        print("Loe raamatut!")


if __name__ == '__main__':
    what_to_do()
