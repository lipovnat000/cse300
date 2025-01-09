import pytest

from pokemon_python_edition import determine_health_bar
from type_advantages import type_matchups

def test_determine_health_bar():
    assert determine_health_bar(75, 185) == "(=========-----------)"
    assert determine_health_bar(1, 100) == "(=-------------------)"


def test_type_matchups():
    assert type_matchups("Fire", "Grass") == 2
    assert type_matchups("Ground", "Flying") == 0
# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])