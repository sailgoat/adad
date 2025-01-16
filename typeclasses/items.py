from typeclasses.objects import Object
from world.enums import WieldLocation
from evennia import AttributeProperty


class Item(Object):
    """
    Typeclass for items.
    """

    value = AttributeProperty(0, autocreate=False)

    def at_object_creation(self):
        super().at_object_creation()


class Equippable(Object):
    """
    Typeclass for equippable items.
    """

    def at_object_creation(self):
        super().at_object_creation()


class Weapon(Equippable):
    """Base class for all weapons."""

    slots_needed = AttributeProperty(1, autocreate=False)
    eligible_slots = AttributeProperty(
        [WieldLocation.LEFT_HAND, WieldLocation.RIGHT_HAND], autocreate=False
    )
    damage = AttributeProperty(1, autocreate=False)

    def at_object_creation(self):
        super().at_object_creation()


class Firearm(Weapon):
    def at_object_creation(self):
        super().at_object_creation()
