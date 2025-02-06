"""Lisa kõikidesse sõnastikesse järgmised sõnad:

headaega - goodbye - arrivederci
pott - pot - pentola
sõnastik - dictionary - dizionario
Tõlgi (väljastage ekraanile) järgmised sõnad:

üks -> itaalia
ciao - > eesti
dog -> itaalia
pentola - inglise
"""
from Python_koolis_5_3 import e_italian, e_english
from Python_koolis_5_3 import second


def add_new_word(estonian, english, italian):
    second.dictionary.english[estonian] = english
    second.dictionary.italian[estonian] = italian
    e_italian[italian] = estonian
    e_english[english] = estonian


add_new_word("headaega", "goodbye", "arrivederci")
add_new_word("pott", "pot", "pentola")
add_new_word("sõnastik", "dictionary", "dizionario")

if __name__ == '__main__':
    print(second.dictionary.english)
    print(second.dictionary.italian)
    print(e_english)
    print(e_italian)
    print(f"'Üks' itaalia keeles on {second.dictionary.italian["üks"]}.")
    print(f"'Ciao' eesti keeles on {e_italian["ciao"]}.")
    print(
        f"'Dog' itaalia keeles on {(second.dictionary.italian[e_english["dog"]])}.")
    print(
        f"'Pentola' inglise keeles on {(second.dictionary.english[e_italian["pentola"]])}.")
