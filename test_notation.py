# test_notation.py
# Tests unitaires pour le module notation.py

import pytest
from notation import *

# -----------------------------
# TODO : Tests unitaires pour valider_notes()
# -----------------------------

@pytest.mark.parametrize("notes, resultat_attendu",[
    ([3,2,1,2,3,3,2,2,3], True),
    ([3,3,3,3,3,3,3,3,3], True),
    ([-2,-1,-3,-2,-1,-1,-2,-3,-3], True), # il faut revérifier
    ([2,3,1,2,3,1,1,2,2,3,2], False),
    ([5,6,7,8,4,8,9,4,5], False),
    ()
])




def test_valider_notes(notes, resultat_attendu):
    resultat_obtenu = valider_notes(notes)
    assert isinstance(resultat_obtenu, bool)
    assert resultat_obtenu == resultat_attendu


@pytest.mark.parametrize("vbase, notes, resultat_attendu", [
    (3.2, [3,2,1,2,3,3,2,2,3], 5.63),
    (2.5, [3,3,3,3,3,3,3,3,3],),
    (1.0, [-2,-1,-3,-2,-1,-1,-2,-3,-3],),
    (3.0, [2,3,1,2,3,1,1,2,2,3,2], "Erreur"),
    (2.5, [5,6,7,8,4,8,9,4,5], "Erreur"),
    (4.0, []),
    (),

])



def test_calculer_points(vbase, notes, resultat_attendu):
    resultat_obtenu = calculer_points(vbase, notes)
    assert isinstance(resultat_obtenu, float or str)
    assert resultat_obtenu == resultat_attendu


# -----------------------------
# TODO : Tests unitaires pour calculer_points()
# -----------------------------


