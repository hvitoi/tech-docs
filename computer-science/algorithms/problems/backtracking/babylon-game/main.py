# %%
import unittest


def babylon_game():
    """
    1. Choice: combine 2 stacks together
    1. Constraint: the stacks height match OR the top color of the stacks match
    1. Goal: end game when a player can't combine stacks
    """

    def winner(stacks, current_player):
        for i in range(len(stacks)):
            for j in range(len(stacks)):
                if i != j and (
                    len(stacks[i]) == len(stacks[j])  # Same height
                    or stacks[i][-1] == stacks[j][-1]  # Same top color
                ):
                    stacks_for_next_turn = [
                        item for i, item in enumerate(stacks) if i not in {i, j}
                    ] + [stacks[i] + stacks[j]]
                    player_winner = winner(stacks_for_next_turn, current_player * -1)
                    if player_winner == current_player:
                        return current_player

        # If none of those movements is possible. Or if any of those movements makes the other player win, you lose
        return current_player * -1

    stacks = [
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
    # start game with player 1
    return winner(stacks, 1)


test_case = unittest.TestCase()
test_case.assertEqual(babylon_game(), None)
