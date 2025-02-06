"""
Tõlgi (väljasta ekraanile) järgmised sõnad:

tere -> inglise k, itaalia k
auto -> itaalia k
kass - > inglise k
üks -> itaalia k
kolm -> inglise k
"""
import Python_koolis_5_1_dictionary as dictionary

ONE_KEY = "üks"
THREE_KEY = "kolm"

if ONE_KEY not in dictionary.italian:
    dictionary.italian[ONE_KEY] = "uno"

if THREE_KEY not in dictionary.english:
    dictionary.english[THREE_KEY] = "three"

if __name__ == '__main__':
    print(
        f"'tere' -> inglise k '{dictionary.english['tere']}', itaalia k '{dictionary.italian['tere']}'.")
    print(dictionary.italian["auto"])
    print(dictionary.english["kass"])
    dictionary.italian["üks"] = "uno"
    print(dictionary.italian["üks"])
    dictionary.english["kolm"] = "three"
    print(dictionary.english["kolm"])
    print(dictionary.english)
    print(dictionary.italian)
