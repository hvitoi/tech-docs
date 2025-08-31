# %%
import unittest


def babylon_game(stacks: list[list[str]], current_player: int = 1) -> int:
    """
    1. Choice: combine 2 stacks together
    2. Constraint: the stacks height match OR the top color of the stacks match
    3. Goal: end game when a player can't combine stacks
    """

    # try every possible move for this turn
    for i in range(len(stacks)):
        for j in range(i + 1, len(stacks)):
            # starting from i + 1 prunes symmetric moves - (i, j) and (j, i) - and avoid stacking a stack on top of itself
            if (
                len(stacks[i]) == len(stacks[j])  # same height
                or stacks[i][-1] == stacks[j][-1]  # same top color
            ):
                stacks_for_next_turn = [
                    stack for index, stack in enumerate(stacks) if index not in {i, j}
                ] + [stacks[i] + stacks[j]]
                player_winner = babylon_game(stacks_for_next_turn, current_player * -1)
                if player_winner == current_player:
                    return current_player

    return current_player * -1


test_case = unittest.TestCase()
test_case.assertEqual(
    babylon_game(
        [
            ["Y"],
            ["Y"],
            ["Y"],
            ["W"],
            ["W"],
            ["W"],
            ["G"],
            ["G"],
            ["G"],
            ["B"],
            ["B"],
            ["B"],
        ]
    ),
    1,
)
