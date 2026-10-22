EXPECTED_BAKE_TIME = 40

def bake_time_remaining( elapsed_bake_time ):
    """Calcul du temps restant"""
    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes( number_of_layers):
    """Calcul du temps de preparation"""
    return 2*number_of_layers
    
def elapsed_time_in_minutes( number_of_layers, elapsed_bake_time):
    """Calcul du temps total ecoule"""
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
