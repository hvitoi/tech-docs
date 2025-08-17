# %%
import plistlib
import subprocess

result = subprocess.run(
    ["ioreg", "-alp", "IODeviceTree"],
    stdout=subprocess.PIPE,
    check=True,
)

plistlib.loads(result.stdout)
