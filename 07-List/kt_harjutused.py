"""
Koosta järjend loomad.

Küsi kasutajalt looma nimesid. Kui seda nime pole järjendis, siis lisa see.
Kui järjendis on loom, mis algab sama tähega kui sisestatud nimi lõppes,
siis kirjuta see ekraanile ja küsi uus loom,
kui ei ole, siis küsi kasutajalt uus loom,
mis algab tähega, millega eelmine lõppes.
"""


def loomad_list():
    loomad = []
    while True:
        sisesta_loom = input(
            "Sisesta looma nimi (lõpetamiseks kirjuta 'end'): ").lower()

        if sisesta_loom == "end":
            print("Mäng lõppenud.")
            print(loomad)
            break

        if sisesta_loom not in loomad:
            loomad.append(sisesta_loom)

        viimane_taht = sisesta_loom[-1]
        loom_listis = None

        for loom in loomad:
            if loom[0] == viimane_taht:
                loom_listis = loom
                break

        if loom_listis:
            print(
                f"Loom listis, mis algab '{viimane_taht}' tähega: {loom_listis}")
        else:
            print(f"Looma, mis algab '{viimane_taht}' tähega, ei leitud.")


"""
Küsi kasutajalt 3 arvu.

Väikseim arv korruta kahega
Küsi kasutajalt arvude ruute ühest kuni eelmise sammu tulemuseni (Kordus)
Teata kas kasutaja vastas õigesti või valesti
Teata mitu korda kasutaja vastas õigesti.
"""


def practice_math():
    numbers = [int(input(f"Sisestage {i + 1}. arv: ")) for i in range(3)]
    smallest_number = min(numbers) * 2

    correct = 0
    for i in range(1, smallest_number + 1):
        user_input = int(input(f"Mis on {i} ruut? "))
        if user_input == i ** 2:
            print("Õige!")
            correct += 1
        else:
            print("Vale!")
    print(f"Kokku vastasite õigesti {correct} korda.")


"""
Küsi kasutaja nime ja vanust.

Kui nime pikkus on väiksem kui vanus või vanus on alla 5 siis tervita nime pidi 3 korda (Kordus)
Muidu küsi kolm arvu ja nende summa
Teata kas said õige tulemuse.
"""


def name_and_age_greet():
    user_name = input("Sisesta oma nimi:")
    user_age = int(input("Sisesta oma vanus:"))

    if len(user_name) < user_age or user_age < 5:
        for _ in range(3):
            print(f"Ole sa tervitatud, {user_name}!")
    else:
        first_number = int(input("Sisesta esimene arv:"))
        second_number = int(input("Sisesta teine arv:"))
        third_number = int(input("Sisesta kolmas arv:"))
        user_sum = int(input(
            f"Kui palju on {first_number}+{second_number}+{third_number}?"))
        correct_sum = first_number + second_number + third_number
        if user_sum == correct_sum:
            print("Tubli! See oli õige vastus.")
        else:
            print("Kahjuks ei olnud see õige vastus.")


"""
Küsi kasutaja vanust ja nime.

Tervita kasutajat nime pidi niimitu korda kui mitu aastat ta on täisealine olnud.
Kirjuta ekraanile nime lõpust 3 tähte.
"""


def greet_adults():
    user_age = int(input("Sisesta oma vanus:"))
    user_name = input("Sisesta oma nimi:")
    adult_age = 18
    for _ in range(user_age - adult_age):
        print(f"Tere, {user_name}!")

    print(user_name[-3:])


"""
Küsi kasutaja sugu ja vanus.

Kasuta eale vastavaid tervitusi nii mehele kui ka naisele.
Korda tervitust ea suurendamisega kuni tervitus vahetub või 10 korda.
"""


def greet_depending_on_age():
    user_gender = input("Sisesta oma sugu (mees/naine):")
    user_age = int(input("Sisesta oma vanus:"))
    if user_gender == "mees" and user_age <= 18:
        for i in range(user_age, user_age + 10):
            print("Tere, poiss!")
    elif user_gender == "mees" and user_age > 18:
        print("Tere, mees!")
    elif user_gender == "naine" and user_age <= 18:
        for i in range(user_age, user_age + 10):
            print("Tere, tüdruk!")
    elif user_gender == "naine" and user_age > 18:
        print("Tere, naine!")
    else:
        print("Midagi läks valesti. Proovi palun uuesti.")


"""
Koosta programm, mis küsib kasutajalt klientide arvu (mittenegatiivne täisarv);

arvutab while-tsükli abil lillede koguarvu, mida pood kingib;
väljastab saadud lillede arvu ekraanile.
"""


def flowershop():
    client_amount = int(input("Kui palju kliente täna poes käis?"))
    flowers_given = 0
    counter = 1
    while counter <= client_amount:
        flowers_given += counter
        counter += 2
    print(f"Pood kingib klientidele {flowers_given} lille.")


"""
Koosta programm, mis

küsib kasutajalt klientide arvu (mittenegatiivne täisarv);
arvutab while-tsükli abil lillede koguarvu, mida pood klientidele kingib;
väljastab kingitavate lillede koguarvu.
"""


def another_flowershop():
    client_amount = int(input("Kui palju kliente täna poes käis?"))
    flowers_given = 0
    counter = 0
    paaritu_arv = 1

    while counter < client_amount:
        flowers_given += paaritu_arv
        paaritu_arv += 2
        counter += 1

    print(f"Pood kingib kokku {flowers_given} lille.")


"""
Tuttavad

Loo järjend 3 nimega
Küsi kasutajalt iga nime kohta kas ta tunneb teda, kui ei tunne lase uus nimi sisestada
Alamprogrammiga asenda jäejendis tundmatu nimi sisestatuga
Kirjuta ekraanile kõik nimed iga üks eraldi reale.
"""


def tuttavad():
    tuttavad = ["Kati", "Mati", "Pille"]
    for i in range(len(tuttavad)):
        tuttav = input(f"Kas sa tunned {tuttavad[i]} (jah/ei)?").strip().lower()
        if tuttav == "ei":
            new_name = input("Sisesta uus nimi: ")
            tuttavad[i] = new_name

    print("\nSinu tuttavad on nemad:")
    for name in tuttavad:
        print(name)


"""
Küsi kasutaja nime

Kui nime pikkus on vahemikus 5–10 (kaasa arvatud), siis tervita 3 korda
Muidu küsi kolm arvu ja tagasta nende summa. 
"""


def greet_three_times_or_more():
    name = input("Sisestage oma nimi: ")
    if 5 <= len(name) <= 10:
        for _ in range(3):
            print(f"Tere, {name}!")
    else:
        numbers = [int(input(f"Sisestage {i + 1}. arv: ")) for i in range(3)]
        print(f"Nende arvude summa on {sum(numbers)}.")


"""
Kasutajalt küsitakse sõna.

Kasutajalt küsitakse numbrit.
Konsool prindib antud sõna välja sisestatud number * 2 korda (kordus).
Juhul kui sisestatud number on suurem kui 10, tagastatakse „Viga“.
"""


def word_times_number():
    word = input("Sisestage sõna: ")
    number = int(input("Sisestage number: "))

    if number > 10:
        print("Viga")
    else:
        for _ in range(number * 2):
            print(word)


"""
Küsi kasutajalt 1 arv mille paned astmele 2,3,4 ja 5 kasutades kordust 
ning kuva tulemused ekraanile.

Peale seda küsi kasutajalt kas ta soovib teise arvuga seda teha või lõpetada.
"""


def astendamine():
    while True:
        number = int(input("Sisestage arv: "))
        for aste in range(2, 6):
            print(f"{number} astmel {aste} = {number ** aste}")

        again = input(
            "Kas soovite proovida teist arvu (jah/ei)?").strip().lower()
        if again != "jah":
            break


"""
Küsi kasutajalt arvu.

Kui arv on positiivne, ütle kasutajale, et ta prooviks pigem negatiivset arvu sisestada.
Kui arv on negatiivne, ütle kasutajale, et ta prooviks pigem positiivset arvu sisestada.
Kui arv on 0, õnnitlege kasutajat ja öelge, et olete mängule ära teinud 
ja pääsete igavesest kordusest.
"""


def trick_function():
    number = int(input("Sisestage arv: "))
    while True:
        if number > 0:
            print("Proovige pigem negatiivset arvu.")
        elif number < 0:
            print("Proovige pigem positiivset arvu.")
        else:
            print("Õnnitlen, pääsesite mängust!")
            break


if __name__ == '__main__':
    tuttavad()
