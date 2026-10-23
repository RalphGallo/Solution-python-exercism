"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verification de la criticite d'un reacteur nucleaire"""

    return (temperature * neutrons_emitted) < 500000 and temperature < 800 and neutrons_emitted > 500

def reactor_efficiency(voltage, current, theoretical_max_power):
    """Determination de la plage de puissance"""

    generated_power = voltage * current # Puissance du generateur
    rendement = (generated_power/theoretical_max_power) * 100
    match rendement:
        case n if n >=80:
            return "green"
        case n if 60 <= n < 80:
            return "orange"
        case n if 30 <= n < 60:
            return "red"
        case n if n<30:
            return "black"

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Mecanisme a securite intregre pour eviter la surchage et la fusion du coeur """

    etat = temperature * neutrons_produced_per_second
    if etat < (90*threshold)/100:
        return "LOW"
        
    elif (threshold - (10*threshold)/100) <= etat <= (threshold + (10*threshold)/100):
        return "NORMAL"
    else:
        return "DANGER"