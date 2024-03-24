# Creates a translation table, tells what char is going to be replaced with what
# {"a": "b", "c": "d"}


# %%

# x -> y , a -> b
translation_table = str.maketrans("xa", "yb")
translation_table

"xaxaxa".translate(translation_table)
