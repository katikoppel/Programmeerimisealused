"""
Programm küsib kasutajalt lause.

Juhul, kui lauses on vähem kui 5 sõna, jätab programm lause meelde ja
küsib uue lause. (Kordus, järjend)
Pikas lauses (5 või rohkem sõna) olevad sõnad kuvatakse eraldi real.
"""


def long_sentence():
    saved_sentences = []  # Järjend lühikeste lausete salvestamiseks.
    sentence = input("Kirjuta palun üks lause.")  # Küsib kasutaja sisendit.
    sentence_list = sentence.split()  # Teeb lause järjendiks.
    while len(sentence_list) < 5:
        saved_sentences.append(sentence)
        sentence = input("Kirjuta palun üks lause.")  # Küsib kasutaja sisendit.
        sentence_list = sentence.split()
    saved_sentences.append(sentence)
    print(
        "Salvestatud lühikesed laused on siin:")  # Kõik salvestatud lühikesed laused kuvatakse siin.
    for s in saved_sentences:
        print(s)

    for word in sentence_list:  # Kui lause on pikem kui 5 sõna, siis otsitakse listist sentence_list kõik sõnad.
        print(word)  # Kõik listi sõnad kuvatakse eraldi ridadele.


if __name__ == '__main__':
    long_sentence()
