"""
Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
Languages supported:
-English
-German
-Spanish
-French
"""


def weekday(day: str) -> bool:
    day = day.lower()
    if day[-1] in "ghy":    # German and English
        return day[0] != "s"
    elif day[-1] in "ieso":  # French and Spanish, Portuguese Weekends
        return day[2] not in "mb"
    return True  # Unknown language, 5/7 chance to be a weekday


def weekend(day: str) -> bool:
    return not weekday(day)


if __name__ == "__main__":
    """ Mainly testing for new languages here """
    days = [
        # Spanish
        "lunes",
        "martes",
        "miercoles",
        "jueves",
        "viernes",
        "sabado",
        "domingo",

        # English
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday",

        # German
        "montag",
        "dienstag",
        "mittwoch",
        "donnerstag",
        "freitag",
        "samstag",
        "sonntag",

        # French
        "lundi",
        "mardi",
        "mercredi",
        "jeudi",
        "vendredi",
        "samedi",
        "dimanche",
        
        # Portuguese
        "segunda-feira",
        "terça-feira",
        "quarta-feira",
        "quinta-feira",
        "sexta-feira",
        "sábado",
        "domingo"
    ]

    for i in range(len(days)):
        if i % 7 >= 5:
            assert weekend(days[i]), f"error with: {days[i]}, returned is weekend: {weekend(days[i])}"
        else:
            assert weekday(days[i]), f"error with: {days[i]}, returned is weekday: {weekday(days[i])}"

    print("Tests ran successfully")