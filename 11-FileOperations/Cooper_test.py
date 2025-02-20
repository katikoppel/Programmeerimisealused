"""
Cooper testis mõõdetakse, kui palju suudab inimene joosta 12 minutiga.
On määratud erinevad hindenormid meestele ja naistele.

Koostada programm, mis küsib kasutajalt:
•	failinime,

Programm peab:
•	lugema failist jooksutulemused (täisarvud) ja jooksjate sood (M või N);
•	funktsiooniga arvutama hinded ja väljastama need ekraanile
•	arvutama ja väljastama ekraanile sugude kaupa kõikide tulemuste täisarvuni
ümardatud keskmised ning funktsiooni abil keskmised hinded.

"""

with open("cooper.txt", "w", encoding="utf-8") as file:
    file.write("""1900 N
1800 M
2700 M
2600 N
1400 M
3801 N
1500 N
1800 N""")


def read_file(file_name: str) -> list:
    """Read all lines to a list and return that list."""
    result = []
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            result.append(line.rstrip())
    return result


def get_cooper_result(distance: int, is_male: bool) -> tuple[str, None]:
    """
    Return cooper test result "väga hea", "nõrk", "rahuldav" and distance to next up.

    :param distance: distance in meters ran in 12 minutes
    :param is_male: participant is male or not?
    :return: tuple where first value is the result and second distance remaining to get to next up.
    """

    result = "väga hea"
    distance_to_next = None
    if distance < 2000 and is_male or distance < 1800 and not is_male:
        result = "nõrk"
        distance_to_next = 2000 - distance if is_male else 1800 - distance
    elif distance < 2800 and is_male or distance < 2600 and not is_male:
        result = "rahuldav"
        distance_to_next = 2800 - distance if is_male else 2600 - distance
    return result, distance_to_next


def process_results(results_from_file: list[str]):
    """
    Split each element first value is integer distance, second gender "M" for male, "N" for female.
    :param results_from_file:
    :return: tuple list of each element's cooper result and average results for both genders.
    """
    results = []
    male_distance_count = 0
    male_distance_sum = 0
    female_distance_count = 0
    female_distance_sum = 0
    for line in results_from_file:
        distance_txt, gender_txt = tuple(line.split())
        distance = int(distance_txt)
        if gender_txt == "M":
            male_distance_sum += distance
            male_distance_count += 1
            cooper_result = get_cooper_result(distance, True) + (
            gender_txt, distance_txt)
        else:
            female_distance_sum += distance
            female_distance_count += 1
            cooper_result = get_cooper_result(distance, False) + (
            gender_txt, distance_txt)
        results.append(cooper_result)
    average_distance = round(male_distance_sum / male_distance_count)
    male_average_result = get_cooper_result(average_distance, is_male=True) + (
    "M", str(average_distance))
    average_distance = round(female_distance_sum / female_distance_count)
    female_average_result = get_cooper_result(average_distance,
                                              is_male=False) + (
                            "N", str(average_distance))
    return results, [male_average_result, female_average_result]


def display_cooper_results(cooper_results):
    for result, distance_to_next, gender, distance in cooper_results:
        if distance_to_next:
            print(
                f"{gender} {distance} m, {result}, järgmisest hindest puudu {distance_to_next} m.")
        else:
            print(f"{gender} {distance} m, {result}")


if __name__ == "__main__":
    filename = input("Sisesta cooper testi tulemuste faili nimi:")
    results_from_file = read_file(filename)
    cooper_results = process_results(results_from_file)
    display_cooper_results(cooper_results[0])
    print("Keskmised:")
    display_cooper_results(cooper_results[1])
