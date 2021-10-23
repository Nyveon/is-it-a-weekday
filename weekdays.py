"""
Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
Languages supported:
-English
-German
-Spanish
-French
"""


def weekday(day: str) -> bool:
    if day[-1] in "ghy":    # German and English
        return day[0] != "s"
    elif day[-1] in "ie":   # French
        return day[2] != "m"
    return day[-1] == "s"   # Spanish


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
        "dimanche"
    ]

    for i in range(len(days)):
        if i % 7 >= 5:
            assert weekend(days[i]), f"error with: {days[i]}, returned is weekend: {weekend(days[i])}"
        else:
            assert weekday(days[i]), f"error with: {days[i]}, returned is weekday: {weekday(days[i])}"
