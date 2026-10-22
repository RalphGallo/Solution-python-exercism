def eat_ghost(power_pellet_active, touching_ghost):
    """Verification"""
    return (power_pellet_active and touching_ghost)



def score(touching_power_pellet, touching_dot):
    """Calcul de score"""
    return (touching_power_pellet or touching_dot)

def lose(power_pellet_active, touching_ghost):
    """Verification de l'echec"""
    return (not power_pellet_active and touching_ghost)


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Verifions s'il gagne"""

    return (has_eaten_all_dots and not lose(power_pellet_active, touching_ghost))
