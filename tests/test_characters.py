from evennia.utils import create
from evennia.utils.test_resources import BaseEvenniaTest
from typeclasses.characters import Player, NPC
from world.enums import WieldLocation


class TestCharacters(BaseEvenniaTest):
    def setUp(self):
        super().setUp()
        self.player = create.create_object(Player, key="test_player")
        self.npc = create.create_object(NPC, key="test_npc")

    def test_created(self):

        # Test player and NPC classes with different default properties.
        self.assertTrue(self.player.is_player)
        self.assertFalse(self.npc.is_player)

        # Test basic attribute creation.
        self.assertEqual(self.player.stats.hp, 100)
        self.assertEqual(self.npc.stats.hp, 100)

        # Test basic equipment handler functionality.
        self.assertEqual(self.player.equipment.slots[WieldLocation.LEFT_HAND], None)
