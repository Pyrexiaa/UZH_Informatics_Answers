from q3_character import Character

class Rogue(Character):

    def __init__(self):
        super().__init__()

    def attack(self, other):
        assert isinstance(other, Character)
        assert self is not other

        if not self.is_alive():
            raise Warning("Character is dead!")

        other._take_physical_damage(self._get_caused_dmg(other))

    def _get_caused_dmg(self, other):
        # 10 * self._lvl + (self._lvl-other._lvl) = 11 * self._lvl - other._lvl
        return max(1, self._lvl * 11 - other._lvl)