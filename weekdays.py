"""
Meme-module for "efficiently" checking whether a given day is a weekday/weekend, with multi-language support.
Languages supported:
-English
-German
-Spanish
-French
"""


def weekday(day: str) -> bool:
    """
    Checks if a string is the name of a weekday in the supported languages.
    :param day: Any string, ideally one that actually represents a day
    :return: True if it is a weekday.
    """
    day = day.lower()
    if day[-1] in "ghy":
        return day[0] != "s"
    elif day[-1] in "iesoa":
        return day[2] not in "mb"
    return True


def weekend(day: str) -> bool:
    """
    Checks if a string is the name of a weekend in the supported languages.
    :param day: Any string, ideally one that actually represents a day
    :return: True if it is a weekend.
    """
    return not weekday(day)


