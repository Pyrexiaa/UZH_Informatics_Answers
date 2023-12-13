from q3_character import Character

class Mage(Character):

    def __init__(self):
        super().__init__()

    # A Mage has weak armor, so the damage they take from all kinds of sources is increased by 50%
    def _take_magical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        amount = int(amount * 1.5)
        self._health_cur = max(0, self._health_cur - amount)

    def _take_physical_damage(self, amount):
        assert isinstance(amount, int)
        assert amount >= 0
        amount = int(amount * 1.5)
        self._health_cur = max(0, self._health_cur - amount)
    
    # However, their damage is increased by 25% and the attacks are magical.
    def _get_caused_dmg(self, other):
        damage = max(1, self._lvl * 11 - other._lvl)
        return int(damage * 1.25)
    
    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_magical_damage(self._get_caused_dmg(other))