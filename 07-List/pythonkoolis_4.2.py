"""
Koosta järjend vähemalt kümne Euroopa pealinnaga (suvalises järjekorras).

Väljasta linnad eraldi ridadena.
Järjesta need tähestikulisse järjekorda.
Lase kasutajal lisada kaks uut Euroopa pealinna ja järjesta uuesti.
Esita linnade nimed tähestikulises järjekorras,
lisades iga nime ette ka järjekorra numbri.
Lisa väljundile kokkuvõttev lause "Meie järjendis on 12 Euroopa pealinna",
kus linnade arv leitakse vastava funktsiooni abil.
"""


def print_list(capitals, numbered=False):
    for number, capital in enumerate(capitals):
        if numbered:
            print(f"{number + 1}. {capital}")
        else:
            print(f"{capital}")


if __name__ == '__main__':
    capitals = ["Tallinn", "Riia", "Helsinki", "Stockholm", "Vilnius",
                "Varssav", "Brüssel", "Pariis", "Lissabon", "Berliin"]

    for i in range(2):
        new_capital = input(f"Sisesta {i + 1}. lisa pealinn: ")
        capitals.append(new_capital)
    capitals.sort()
    print_list(capitals, numbered=True)
    print(f"Meie järjendis on {len(capitals)} Euroopa pealinna.")
