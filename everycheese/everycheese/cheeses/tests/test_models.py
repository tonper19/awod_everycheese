import pytest
from ..models import Cheese
# Connects our tests with our database
pytestmark = pytest.mark.django_db


def test__str__():
    cheese = Cheese.objects.create(
        name="Manchego",
        description=("Manchego has a firm and compact consistency and "
                     "a buttery texture, and often contains small, "
                     "unevenly distributed air pockets."),
        firmness=Cheese.Firmness.HARD,
    )
    assert cheese.__str__() == "Manchego"
    assert str(cheese) == "Manchego"
