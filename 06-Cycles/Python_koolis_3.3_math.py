"""
Koosta programm, mis aitab lastel treenida liitmist.

Programm peaks pakkuma välja juhuslike arvudega liitmistehteid ning ootama kasutajalt vastust.
Kui vastus on õige, kiitma kasutajat, kui aga vale, andma õige vastuse ja esitama uue tehte.
Järjest esitatavate tehete hulk võib olla programmis ette antud (näiteks 10),
samuti võib olla ette antud piirid, kui suuri arve kasutajalt küsitakse (näiteks 1 kuni 50).

Programm peaks pidama arvestust ka õigete vastuste üle ning väljastama pärast viimast tehet tulemuse.
"""
from random import randint


def math_exercise():
    print("Tere! Õpime arvutama. Esitan tehted, püüa vastata õigesti.")
    correct_answers = 0
    for i in range(count):
        first_number = randint(lowest, highest)
        second_number = randint(lowest, highest)
        random_operator = randint(1, 3)
        if random_operator == 1:
            correct_answer = first_number + second_number
            correct_answers += show_equation("+", correct_answer, first_number,
                                             second_number)
        elif random_operator == 2:
            correct_answer = first_number - second_number
            correct_answers += show_equation("-", correct_answer, first_number,
                                             second_number)
        elif random_operator == 3:
            correct_answer = first_number * second_number
            correct_answers += show_equation("*", correct_answer, first_number,
                                             second_number)
    print(
        f"See oli viimane ülesanne. Kogusid {count} punktist {correct_answers}.")


def show_equation(operation_symbol, correct_answer, first_number,
                  second_number):
    user_answer = int(
        input(f"{first_number} {operation_symbol} {second_number} = ?"))
    correct_answer = first_number + second_number
    if user_answer == correct_answer:
        print("Tubli, õige vastus!")
        return 1
    else:
        print(f"Sinu vastus polnud õige. Õige vastus on {correct_answer}.")
    return 0


if __name__ == '__main__':
    lowest = int(input("Sisesta väikseim täisarv, mida kasutada: "))
    highest = int(input("Sisesta suurim täisarv, mida kasutada: "))
    count = int(input("Sisesta tehete arv: "))
    math_exercise()
