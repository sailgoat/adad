"""
Characters

Characters are (by default) Objects setup to be puppeted by Accounts.
They are what you "see" in game. The Character class in this module
is setup to be the "default" character type created by the default
creation commands.

"""

from evennia.objects.objects import DefaultCharacter
from evennia.contrib.rpg.traits import TraitHandler
from evennia.utils import lazy_property
from typeclasses.handlers.equipment import EquipmentHandler
from .objects import ObjectParent


class BaseCharacter(ObjectParent, DefaultCharacter):
    """
    The base character that PCs and NPCs will inherit functionality and attributes from.

    """

    is_player = False

    @lazy_property
    def stats(self):
        return TraitHandler(self, db_attribute_key="stats")
    
    @lazy_property
    def skills(self):
        return TraitHandler(self, db_attribute_key="skills")
    
    @lazy_property
    def equipment(self):
        return EquipmentHandler(self)
    
    def at_object_creation(self):
        """
        Initialize all general stats.
        """
        self.stats.add("hp", "Health", trait_type="gauge", base=100, min=0)
    

class Player(BaseCharacter):
    """
    Player character specific functionality and attributes.
    """
    is_player = True

class NPC(BaseCharacter):
    """
    NPC character specific functionality and attributes.
    """
    is_player = False

