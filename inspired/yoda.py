"""This module contains yoda quotes."""
import random


def by_yoda():
    """Return a quote from Yoda

    Returns
    -------
    str
        A quote from Yoda
    """
    yoda_quotes = [
        "Fear is the path to the dark side. Fear leads to anger. Anger leads to hate. Hate leads to suffering.",
        "Once you start down the dark path, forever will it dominate your destiny. Consume you, it will.",
        "Always pass on what you have learned.",
        "Patience you must have my young Padawan.",
        "In a dark place we find ourselves, and a little more knowledge lights our way.",
        "Powerful you have become, the dark side I sense in you.",
        "Train yourself to let go of everything you fear to lose.",
        "Feel the force!",
        "Truly wonderful the mind of a child is.",
        "Do or do not. There is no try.",
        "You will find only what you bring in.",
    ]
    return random.choice(yoda_quotes)
