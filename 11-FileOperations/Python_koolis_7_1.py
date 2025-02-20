"""
Loo fail tuttavad.txt ja lisa sinna vähemalt 6 tuttava perekonna- ja eesnimed
(iga tuttav uuele reale, perekonna- ja eesnimi tühikuga eraldatult).

Koosta programm, mis loeb failist andmed ja väljastab need ekraanile tähestikulises järjekorras.
Mõistlik on ilmselt kasutada järjendit ja sellega seonduvaid võimalusi (järjestamist).
Tähestikulises järjekorras salvestage tuttavate nimed ka uude faili sorteeritud_tuttavad.txt.
"""


def create_file(file_name: str, lines: list) -> None:
    """Write each value in lines to separate line in file."""
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")


def read_file(file_name: str) -> list:
    """Read all lines to a list and return that list."""
    result = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            result.append(line.rstrip())
    return result


def split_words(sentences: list) -> list:
    """
    Split sentences into tuple of words and return them.

    sentences:["See on sisend lause", "Siin on ka lause", "veel"]
    :return: [("See", "on", "sisend", "lause"), ("Siin", "on", "ka", "lause"), ("veel")]
    """
    result = []
    for sentence in sentences:
        result.append(tuple(sentence.split()))
    return result


if __name__ == '__main__':
    file_name = "tuttavad.txt"
    create_file(file_name,
                ["Tiit Sukk", "Armas Noole", "Elina Elli", "Joosep Juurikas",
                 "Õnne Kolmteist", "Jaana Järv"])
    names = read_file(file_name)
    print(names)
    split_names = split_words(names)
    print(split_names)
    sorted_names = map(lambda s: " ".join(s),
                       sorted(split_names, key=lambda n: n[-1]))
    for name in sorted_names:
        print(f"{' '.join(name)}")
    create_file("sorteeritud_tuttavad.txt", sorted_names)
