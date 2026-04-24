# %%


from unittest import TestCase


def flood_fill(
    image: list[list[int]], initial_row: int, initial_col: int, target_color: int
) -> list[list[int]]:
    """"""

    def ff(row, col):
        if not (0 <= row < len_rows):
            return

        if not (0 <= col < len_cols):
            return

        if image[row][col] != drive_color:
            return

        image[row][col] = target_color

        ff(row, col - 1)  # left
        ff(row, col + 1)  # right
        ff(row - 1, col)  # up
        ff(row + 1, col)  # down

    len_rows = len(image)
    len_cols = len(image[0])
    drive_color = image[initial_row][initial_col]

    ff(initial_row, initial_col)

    return image


test_case = TestCase()
test_case.assertEqual(
    flood_fill(
        [
            [1, 1, 1],
            [1, 1, 0],
            [1, 0, 1],
        ],
        1,
        1,
        2,
    ),
    [
        [2, 2, 2],
        [2, 2, 0],
        [2, 0, 1],
    ],
)
