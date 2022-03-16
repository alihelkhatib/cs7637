class MonsterClassificationAgent:

    def get_updated_generalization(self, generalization: dict, monster_attributes: dict):
        if len(generalization) == 0:
            generalization = monster_attributes
        else:
            for monster_attribute, value in monster_attributes.items():
                if generalization[monster_attribute] != value:
                    generalization[monster_attribute] = "any"
        return generalization

    def check_if_new_monster_matches_generalization(self, generalization: dict, new_monster_attributes: dict):
        for monster_attribute, value in new_monster_attributes.items():
            if generalization[monster_attribute] != value and generalization[monster_attribute] != "any":
                return False
        return True

    def solve(self, samples: list, new_monster: dict):
        generalization = dict()
        for monster, is_positive in samples:
            if is_positive:
                generalization = self.get_updated_generalization(generalization, monster)
        return self.check_if_new_monster_matches_generalization(generalization, new_monster)
