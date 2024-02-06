# %%
def merge_alternately(word1: str, word2: str) -> str:
    """
    Merge two strings
    """
    word1 = list(word1)
    word2 = list(word2)
    merged = []

    while len(word1) + len(word2) > 0:
        if len(word1) > 0:
            merged.append(word1.pop(0))
        if len(word2) > 0:
            merged.append(word2.pop(0))

    return "".join(merged)


merge_alternately("abc", "123")
