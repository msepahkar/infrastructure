# -*- coding: utf-8 -*-

import sys
sys.path.append('mehdi_lib')
sys.path.append('production_programming')

from mehdi_lib.basics import thing_, basic_types, editor_, prototype_, constants_
from mehdi_lib.generals import general_editors, general_fields, general_initial_values, general_ui_titles, general_enums
from mehdi_lib.basics import database_tools

from PyQt5 import QtWidgets


sample_sub_things_ui_titles_en = 'sample sub-things'
sample_sub_things_ui_titles_fa = 'جزءهای نمونه'

sample_sub_things_ui_titles = {
    basic_types.Language.AvailableLanguage.en: sample_sub_things_ui_titles_en,
    basic_types.Language.AvailableLanguage.fa: sample_sub_things_ui_titles_fa,
}

sample_things_ui_titles_en = 'sample things'
sample_things_ui_titles_fa = 'چیزهای نمونه'

sample_things_ui_titles = {
    basic_types.Language.AvailableLanguage.en: sample_things_ui_titles_en,
    basic_types.Language.AvailableLanguage.fa: sample_things_ui_titles_fa,
}


# ===========================================================================
class SuperThingPrototype(prototype_.ThingPrototype):
    pass


# ===========================================================================
class ThingPrototype(prototype_.ThingPrototype):
    pass


# ===========================================================================
class SubThingPrototype(prototype_.ThingPrototype):
    pass


# ===========================================================================
class SuperThing(thing_.Thing):
    """A Thing which has a ListOfThings field for things"""
    name = general_fields.NameField(initial_value=general_initial_values.name)
    things = general_fields.ListField(1, sample_things_ui_titles, 'things', ThingPrototype)


# ===========================================================================
class Thing(thing_.Thing):
    """A Thing which as a ListOfThings field for sub-things"""
    name = general_fields.NameField(initial_value=general_initial_values.name)
    version_number = general_fields.IntField(1, general_ui_titles.version_number, 'version_number', 1,
                                             constants_.Constants.MAX_INT, 1)
    amount_unit = general_fields.EnumField(2, general_ui_titles.amount_unit, 'amount_unit', general_enums.AmountUnit,
                                           general_enums.AmountUnit.number)
    sub_things = general_fields.ListField(11, sample_sub_things_ui_titles, 'sub_things', SubThingPrototype)
    super_thing = general_fields.ForeignKeyField(12, general_ui_titles.dummy, 'thing_parent', ThingPrototype,
                                                 SuperThingPrototype)


# ===========================================================================
class SubThing(thing_.Thing):
    name = general_fields.NameField(initial_value='sub-thing')
    sub_thing_parent = general_fields.ForeignKeyField(1, general_ui_titles.dummy, 'sub_thing_parent',
                                                      SubThingPrototype,
                                                      ThingPrototype)


basic_types.Language.set_active_language(basic_types.Language.AvailableLanguage.en)
app = QtWidgets.QApplication(sys.argv)

# create the things
super_things = thing_.ListOfThings(SuperThing)
super_thing_1 = SuperThing()
super_thing_2 = SuperThing()
super_thing_3 = SuperThing()
super_things.append(super_thing_1)
super_things.append(super_thing_2)
super_things.append(super_thing_3)

# create a list of things editor
super_things_editor = general_editors.TableOfThingsEditor(super_things, None)
sub_editor_1 = super_things_editor.sub_editors[super_thing_1]
sub_editor_2 = super_things_editor.sub_editors[super_thing_2]
sub_editor_3 = super_things_editor.sub_editors[super_thing_3]
sub_editor_1.set_selected(True)
widget = super_things_editor.widget
widget.setCurrentCell(2, 1)
print(widget.currentRow())
main_window = editor_.EditorDialog(super_things_editor, automatic_unregister=False)

main_window.show()
viewport = widget.viewport()
print(viewport.x(), viewport.y())
rect = widget.visualItemRect(widget.item(1, 1))
print(rect.center().x(), rect.center().y())




app.exec_()


