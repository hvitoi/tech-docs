import subprocess

# Submit shell commands

output = subprocess.check_output(
    "brightnessctl -l -m -c backlight",
    shell=True,
    encoding='utf-8',
)  # returns a string
