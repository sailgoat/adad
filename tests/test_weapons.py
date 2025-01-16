from evennia.utils import create
from evennia.utils.test_resources import BaseEvenniaTest
from evennia.prototypes import spawner

from typeclasses.characters import Player
from world.prototypes.weapon import DERINGER
from world.enums import WieldLocation


class TestWeapons(BaseEvenniaTest):
    def setUp(self):
        super().setUp()
        self.character = create.create_object(Player, key="test_character")

    def test_spawn_weapon(self):
        weapon = spawner.spawn(DERINGER)[0]
        self.assertEqual(weapon.damage, 2)

    def test_equip_weapon(self):
        # Make sure we have nothing equipped first.
        self.assertTrue(
            self.character.equipment.is_empty(WieldLocation.LEFT_HAND)
            and self.character.equipment.is_empty(WieldLocation.RIGHT_HAND)
        )

        weapon = spawner.spawn(DERINGER)[0]
        self.assertTrue(self.character.equipment.equip(weapon))
        self.assertFalse(self.character.equipment.is_empty(WieldLocation.LEFT_HAND))

        off_hand_weapon = spawner.spawn(DERINGER)[0]
        self.assertTrue(self.character.equipment.equip(off_hand_weapon))

    def test_remove_weapon(self):
        weapon = spawner.spawn(DERINGER)[0]
        with self.assertRaises(Exception):
            # This should raise an error because we haven't equipped anything.
            self.character.equipment.unequip(weapon)

        self.assertTrue(self.character.equipment.equip(weapon))

        # With the weapon equipped, we should now be able to remove it.
        self.assertTrue(self.character.equipment.unequip(weapon))

    def test_remove_weapon_by_slot(self):
        weapon = spawner.spawn(DERINGER)[0]
        self.assertTrue(self.character.equipment.equip(weapon))
        self.assertTrue(self.character.equipment.unequip(weapon.eligible_slots[1]))
