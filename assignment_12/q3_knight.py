from q3_character import Character

class Knight(Character):

    def __init__(self, name, lvl):
        super().__init__(name, lvl)

    # Knights also deal physical damage. They have strong armor and can wear a shield that reduces any physical damage by 25%
    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        amount = amount * 0.75
        self._health_cur = int(max(0, self._health_cur - amount))

    # # Unfortunately, this comes at a price, their attacks deal 20% less damage than usual. 
    def _get_caused_dmg(self, other):
        damage = max(1, self._lvl * 11 - other._lvl)
        return int(damage * 0.8)
    
    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_physical_damage(self._get_caused_dmg(other))
