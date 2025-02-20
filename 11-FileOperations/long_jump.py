"""
Koostada funktsioon, mis võtab argumentideks vigase tulemuse (meetrites) ja mõõteparanduse (sentimeetrites).

Funktsioon arvutab tegeliku tulemuse (meetrites) ning tagastab selle.
tegelikTulemus = viganeTulemus + mõõteparandus / 100

Koostada programm, mis küsib kasutajalt:
•	failinime,
•	mõõteparanduse (nt 35 näitab, et igale tulemusele tuleb liita 35 sentimeetrit (e 0,35 meetrit)),
•	meistrivõistluste normatiivi.
"""
from Cooper_test import read_file

with open("kaugus.txt", "w", encoding="utf-8") as file:
    file.write("""6.56
5.76
5.82
5.23
5.74
6.14
5.28
5.77
6.45
6.02
5.78""")
