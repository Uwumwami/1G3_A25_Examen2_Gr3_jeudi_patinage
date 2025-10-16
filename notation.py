# notation.py
# TODO : Version buggée — à corriger après exécution des tests unitaires
# TODO : Mettre des commentaires pour identifier les bugs trouvés et comment vous les avez corrigés.

def valider_notes(notes: list[int]) -> bool:
    """
    Vérifie que la liste de notes contient exactement 9 entiers entre -3 et +3.
    :param notes: liste de notes
    :returns: vrai si la liste est valide, sinon faux.
    """
    if len(notes) < 9 or len(notes) > 9:
        return False

    for n in notes:
        if n > 3 or n < -3:
            return False

    return True


def calculer_points(vbase: float, notes: list[int]) -> float:
    """
    Calcule la note finale d’un mouvement.
    :param vbase: valeur de base de la note
    :param notes: liste de notes
    :returns: valeur de la note finale
    """
    try:
        valider_notes(notes)

        note_max = max(notes)
        note_min = min(notes)

        for i in range(len(notes)):
            compteur = 0
            if notes[i] == note_max or note_min:
                compteur += 1
                if compteur == 1:
                    notes.remove(notes[i])
                    break

        moyenne = sum(notes) / len(notes)
        total = vbase + moyenne
        return total

    except ValueError:
        print("Erreur")
        return 0



