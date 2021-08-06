from mehdi_lib.basics import prototype_, thing_
from mehdi_lib.generals import general_fields, general_editors, general_ui_titles
import pytest


pytestmark = pytest.mark.basics


# ===========================================================================
class TempThingPrototype(prototype_.ThingPrototype):
    pass


# ===========================================================================
class TempThing(thing_.Thing):
    pass


# ===========================================================================
def test_Prototype():
    assert TempThingPrototype.get_main_type() == TempThing
    assert prototype_.Prototype.get_prototype(TempThing) == TempThingPrototype
    assert TempThingPrototype.referencing_prototypes() == []
