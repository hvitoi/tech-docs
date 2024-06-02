# %%
from subprocess import run, PIPE, CompletedProcess

res: CompletedProcess = run("ls -la", shell=True)

# %%
run(
    ["ioreg", "-alp", "IODeviceTree"],
    stdout=PIPE,
    check=True,
)
