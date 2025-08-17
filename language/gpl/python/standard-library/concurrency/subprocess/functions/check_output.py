# %%
from subprocess import check_output

# Submit shell commands (returns a string)
output = check_output(
    "brightnessctl -l -m -c backlight",
    shell=True,
    encoding="utf-8",
)
