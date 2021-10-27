"""
Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
Languages supported:
-English
-German
-Spanish
-French
"""

#todo: update diagram
def weekday(day: str) -> bool:
    day = day.lower()
    if day[-1] in "ghy":
        return day[0] != "s"
    elif day[-1] in "iesoa":
        return day[2] not in "mb"
    return True


def weekend(day: str) -> bool:
    return not weekday(day)


if __name__ == "__main__":
    """ Mainly testing for new languages here """
    days = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "montag", "dienstag", "mittwoch", "donnerstag", "freitag", "samstag", "sonntag", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo", "lunedì", "martedì", "mercoledì", "giovedì", "venerdì", "sabato", "domenica"]

    for i in range(len(days)):
        if i % 7 >= 5:
            assert weekend(days[i]), f"error with: {days[i]}, returned is weekend: {weekend(days[i])}"
        else:
            assert weekday(days[i]), f"error with: {days[i]}, returned is weekday: {weekday(days[i])}"

    print("Tests ran successfully")