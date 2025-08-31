# %%
import unittest


def babylon_game(stacks, current_player=1):
    """
    1. Choice: combine 2 stacks together
    1. Constraint: the stacks height match OR the top color of the stacks match
    1. Goal: end game when a player can't combine stacks
    """

    for i in range(len(stacks)):
        for j in range(len(stacks)):
            if i != j and (
                len(stacks[i]) == len(stacks[j])  # same height
                or stacks[i][-1] == stacks[j][-1]  # same color
            ):
                stacks_for_next_turn = [
                    item for i, item in enumerate(stacks) if i not in {i, j}
                ] + [stacks[i] + stacks[j]]
                player_winner = babylon_game(stacks_for_next_turn, current_player * -1)
                if player_winner == current_player:
                    return current_player  # current player won

    # opposite player won
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
