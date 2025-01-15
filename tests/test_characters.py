from evennia.utils import create
from evennia.utils.test_resources import BaseEvenniaTest
from typeclasses.characters import Player, NPC

class TestCharacters(BaseEvenniaTest):
    def setUp(self):
        super().setUp()
        self.player = create.create_object(Player, key="test_player")
        self.npc = create.create_object(NPC, key="test_npc")
    
    def test_created(self):
        self.assertTrue(self.player.is_player)
        self.assertFalse(self.npc.is_player)
        self.assertEqual(self.player.stats.hp, 100)
        self.assertEqual(self.npc.stats.hp, 100)