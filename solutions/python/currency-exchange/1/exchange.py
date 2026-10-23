"""Fonction de conversion es devises"""

def exchange_money(budget, exchange_rate):
    """Conversion de devise"""
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """Calcul du reste d'argent apres conversion"""

    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """Calcul de la valeur totale des billets"""

    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calcul du nombre de billets """

    return amount // denomination


def get_leftover_of_bills(amount, denomination):
    """Calcul du montant restant apres retrait des billets"""

    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calcul de la nouvelle valeur de la devise apres retrait du % de change"""
    new_exchangeable_rate = exchange_rate*(1 + spread/100) # Ici on ajoute les frais de change pour obtenir une nouvelle valeur de change
    return (budget / new_exchangeable_rate) // denomination * denomination
    
