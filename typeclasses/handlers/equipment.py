from world.enums import WieldLocation


class EquipmentHandler:
    save_attribute = "inventory_slots"

    def __init__(self, obj):
        self.obj = obj
        self._load()

    def _load(self):
        # Retrieve the character's inventory from an attribute.
        self.slots = self.obj.attributes.get(
            self.save_attribute,
            category="inventory",
            default={
                WieldLocation.LEFT_HAND: None,
                WieldLocation.RIGHT_HAND: None,
            },
        )

    def _save(self):
        # Save the equipment to the character's attribute.
        self.obj.attributes.add(self.save_attribute, self.slots, category="inventory")

    def equip(self, obj):
        slots = self.slots
        equipped = False
        use_slots = getattr(obj, "eligible_slots")

        for slot in use_slots:
            if slots[slot] == None:
                slots[slot] = obj
                equipped = True
                return equipped

        return equipped

    def unequip(self, obj_or_slot):
        slots = self.slots
        unequipped = False

        if isinstance(obj_or_slot, WieldLocation):
            # Unequipping from an inventory slot.
            slots[obj_or_slot] = None
            unequipped = True
        elif obj_or_slot in self.slots.values():
            # Unequipping an equipped item.
            for slot, slot_object in slots.items():
                if slot_object is obj_or_slot:
                    slots[slot] = None
                    unequipped = True
        else:
            raise Exception("Invalid item or inventory slot.")

        if unequipped:
            self._save()
        return unequipped

    def is_empty(self, slot):
        # Determine if the given is a slot
        return self.slots[slot] is None
