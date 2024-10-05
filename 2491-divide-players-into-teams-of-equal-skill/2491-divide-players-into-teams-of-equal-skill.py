class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        total_skill = sum(skill)

        if total_skill % (n // 2) != 0:
            return -1

        target_skill = total_skill // (n // 2)
        skill_map = Counter(skill)
        total_chemistry = 0

        for curr_skill, curr_freq in skill_map.items():
            partner_skill = target_skill - curr_skill

            if (
                partner_skill not in skill_map
                or curr_freq != skill_map[partner_skill]
            ):
                return -1

            total_chemistry += curr_skill * partner_skill * curr_freq

        return total_chemistry // 2